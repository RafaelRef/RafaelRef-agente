"""Planeja manutenção semanal (v1, 2026-10-18). Substitui planejar.py (que tinha datas fixas de 14/10).
Uso: python3 -I planejar_man.py <agenda.json> --existentes existing.json --hoje AAAA-MM-DDTHH:MM --semanas 43,44,45 --out pages.json
Existentes: lista [chave, inicioUTC, fimUTC]. Cria só chaves man-<matéria>-<semana ISO> ausentes e
pula a matéria na semana em que ela já tem sessão pré-avaliação.
"""
import json, sys
from datetime import datetime as DT, timedelta as TD, date, time, timezone
TZ = timezone(TD(hours=-3))
args = sys.argv[1:]
def opt(n):
    i = args.index(n); v = args[i+1]; del args[i:i+2]; return v
existentes = json.load(open(opt('--existentes')))
hoje = DT.fromisoformat(opt('--hoje')).replace(tzinfo=TZ)
semanas = [int(x) for x in opt('--semanas').split(',')]
out = opt('--out')
busy, load = {}, {}
def add(d, a, b): busy.setdefault(d, []).append((a, b))
for f in args:
    for e in json.load(open(f))['events']:
        if 'dateTime' in e['start']:
            s = DT.fromisoformat(e['start']['dateTime']).astimezone(TZ); t = DT.fromisoformat(e['end']['dateTime']).astimezone(TZ)
            add(s.date(), s.hour*60+s.minute-15, t.hour*60+t.minute+15)
chaves = set(); pre_sem = set()
MAT = {  # chave curta -> (matéria, faculdade, dia da aula 0=seg)
 'Sistemas':('Sistemas Digitais','Einstein',2), 'Física':('Física Médica','Einstein',3), 'BSDigEH':('BSDigEH','Einstein',4),
 'Biomateriais':('Biomateriais','Einstein',0), 'Modelagem':('Modelagem e Simulação','Einstein',1), 'Bioética':('Bioética','Einstein',1),
 'PTR3522':('PTR3522 Gestão de Pavimentos','Poli',3), 'PEF3401':('PEF3401 Mecânica das Estruturas II','Poli',3),
 'PEF3402':('PEF3402 Estruturas de Aço','Poli',4), 'PTR3534':('PTR3534 Transporte Aéreo','Poli',1), 'PCC3412':('PCC3412 Real Estate','Poli',1),
 'PTR3432':('PTR3432 Aeroportos','Poli',2), 'PTR3514':('PTR3514 SIT','Poli',2), 'Cidades':('Cidades Inteligentes','Poli',0), 'TCC':('TCC','Poli',3)}
PRE2MAT = {'BSDigEH':'BSDigEH','BioMat':'Biomateriais','ModelS':'Modelagem','SisDig':'Sistemas','Bioética':'Bioética','SIT':'PTR3514',
           'PEF3401':'PEF3401','PTR3522':'PTR3522','PCC3412':'PCC3412','PTR3432':'PTR3432','FisMed':'Física','PEF3402':'PEF3402',
           'Cidades':'Cidades','TransporteAéreo':'PTR3534'}
for ch, s, e in existentes:
    chaves.add(ch)
    s = DT.fromisoformat(s.replace('Z', '+00:00')).astimezone(TZ); e = DT.fromisoformat(e.replace('Z', '+00:00')).astimezone(TZ)
    add(s.date(), s.hour*60+s.minute-15, e.hour*60+e.minute+15)
    load[s.date()] = load.get(s.date(), 0) + int((e-s).total_seconds()//60)
    if ch.startswith('pre-'):
        for k, m in PRE2MAT.items():
            if k in ch: pre_sem.add((m, s.isocalendar()[1]))
BLOQ = {date(2026,10,17): (0,1440), date(2026,10,16): (19*60,1440), date(2026,10,30): (12*60,1440),
        date(2026,11,13): (19*60,1440), date(2026,11,21): (16*60,1440)}
for d,(a,b) in BLOQ.items(): add(d,a,b)
for i in range(80):
    dd = date(2026,10,14)+TD(days=i); add(dd, 12*60, 13*60)
    if dd.weekday() == 3: add(dd, 9*60, 13*60)
PROVA = {date(2026,11,11),date(2026,11,24),date(2026,11,26),date(2026,11,27),date(2026,12,1),date(2026,12,2),
         date(2026,12,3),date(2026,12,4),date(2026,12,7),date(2026,12,8)}
def cap(d):
    reta = date(2026,11,16) <= d <= date(2026,12,8)
    if d.weekday() >= 5: return 420 if reta else 360
    return 300 if reta else 240
def free(d, a, b):
    if a < 7*60 or b > 22*60: return False
    if DT.combine(d, time(a//60, a%60), TZ) < hoje + TD(minutes=30): return False
    return all(not (a < y and x < b) for x, y in busy.get(d, []))
ORDER = list(range(18*60+30, 22*60, 15)) + list(range(13*60+30, 18*60, 15)) + list(range(9*60, 12*60, 15)) + list(range(7*60, 9*60, 15))
pages = []; semlugar = []
ordem = sorted(MAT, key=lambda k: MAT[k][1] != 'Einstein')
for w in semanas:
    seg = date.fromisocalendar(2026, w, 1)
    for k in ordem:
        m, fac, cd = MAT[k]; ch = f"man-{k}-{w}"
        if ch in chaves or (k, w) in pre_sem: continue
        dur = 60 if fac == 'Einstein' or k == 'TCC' else 45
        r = None
        for i in range(5):
            d = seg + TD(days=cd+i)
            if d in PROVA or load.get(d,0)+dur > cap(d): continue
            for a in ORDER:
                if free(d, a, a+dur):
                    r = (d, a); break
            if r: break
        if not r: semlugar.append(ch); print('SEM ESPAÇO', ch); continue
        d, a = r; add(d, a-15, a+dur+15); load[d] = load.get(d,0)+dur
        s = DT.combine(d, time(a//60, a%60), TZ); e = s+TD(minutes=dur)
        foco = 'Avançar o TCC (logística humanitária).' if k == 'TCC' else 'Revisar a aula da semana e fazer os exercícios.'
        pages.append({"properties": {"Sessão": f"{m}: manutenção", "date:Quando:start": s.isoformat(), "date:Quando:end": e.isoformat(),
            "date:Quando:is_datetime": 1, "Matéria": m, "Faculdade": fac, "Tipo": "Manutenção", "Foco": foco, "Duração (min)": dur,
            "Status": "A fazer", "Chave": ch, "Criada pelo agente": "__YES__"}})
        print(s.strftime('%a %d/%m %H:%M'), dur, ch)
json.dump(pages, open(out, 'w'), ensure_ascii=False)
print(len(pages), 'sessoes')
