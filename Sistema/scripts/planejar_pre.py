"""Planeja sessões pré-avaliação espaçadas (v2, 2026-10-14).
Uso: python3 -I planejar_pre.py <agenda1.json> [agenda2.json ...] --existentes existing.json --hoje AAAA-MM-DDTHH:MM --out pages.json
Agenda: JSON do list_events. Existentes: lista [chave, inicioUTC, fimUTC].
"""
import json, sys
from datetime import datetime as DT, timedelta as TD, date, time, timezone
TZ = timezone(TD(hours=-3))
args = sys.argv[1:]
def opt(n):
    i = args.index(n); v = args[i+1]; del args[i:i+2]; return v
existentes = json.load(open(opt('--existentes')))
hoje = DT.fromisoformat(opt('--hoje')).replace(tzinfo=TZ)
out = opt('--out')
busy = {}
def add(d, a, b): busy.setdefault(d, []).append((a, b))
eventos = []
for f in args:
    eventos += json.load(open(f))['events']
prova_dias = {}
for e in eventos:
    if 'dateTime' in e['start']:
        s = DT.fromisoformat(e['start']['dateTime']).astimezone(TZ); t = DT.fromisoformat(e['end']['dateTime']).astimezone(TZ)
        add(s.date(), s.hour*60+s.minute-15, t.hour*60+t.minute+15)
load = {}
pre_existentes = {}  # aval -> datas
for ch, s, e in existentes:
    s = DT.fromisoformat(s.replace('Z', '+00:00')).astimezone(TZ); e = DT.fromisoformat(e.replace('Z', '+00:00')).astimezone(TZ)
    add(s.date(), s.hour*60+s.minute-15, e.hour*60+e.minute+15)
    load[s.date()] = load.get(s.date(), 0) + int((e-s).total_seconds()//60)
# bloqueios pessoais e almoço
BLOQ = {date(2026,10,17): (0,1440), date(2026,10,16): (19*60,1440), date(2026,10,30): (12*60,1440),
        date(2026,11,13): (19*60,1440), date(2026,11,21): (16*60,1440)}
for d,(a,b) in BLOQ.items(): add(d,a,b)
d0 = date(2026,10,14)
for i in range(70):
    dd = d0+TD(days=i); add(dd, 12*60, 13*60)
    if dd.weekday() == 3: add(dd, 9*60, 13*60)  # Ref apagou sessão de quinta de manhã (14/10)
def cap(d):
    reta = date(2026,11,16) <= d <= date(2026,12,8)
    if d.weekday() >= 5: return 420 if reta else 360
    return 300 if reta else 240
def free(d, a, b):
    if a < 7*60 or b > 22*60: return False
    if DT.combine(d, time(a//60, a%60), TZ) < hoje + TD(minutes=30): return False
    for x, y in busy.get(d, []):
        if a < y and x < b: return False
    return True
ORDER = list(range(18*60+30, 22*60, 15)) + list(range(13*60+30, 18*60, 15)) + list(range(9*60, 12*60, 15)) + list(range(7*60, 9*60, 15))
def place(dias, dur, vespera=False):
    for d in dias:
        if d in PROVA_DAY_BLOCK and not vespera: continue
        if load.get(d, 0) + dur > cap(d): continue
        for a in ORDER:
            if free(d, a, a+dur):
                add(d, a-15, a+dur+15); load[d] = load.get(d, 0) + dur
                return d, a
    return None
# avaliações: data, matéria, faculdade, tipo, nome, tarefa_id
A = [
 ('2026-10-16','BSDigEH','Einstein','P','P2 BSDigEH','3f91f5b2-a2e4-811d-bf40-c3cb95a6f8fd'),
 ('2026-10-19','Biomateriais','Einstein','Lab','Lab BioMat','3f91f5b2-a2e4-814a-bd9b-f09f2b5d2b8a'),
 ('2026-10-20','Modelagem e Simulação','Einstein','TBL','TBL ModelS','3f91f5b2-a2e4-811b-9c6c-e5c766868422'),
 ('2026-10-21','Sistemas Digitais','Einstein','TBL','Quiz SisDig','3f91f5b2-a2e4-8193-a8b6-f5d75df0b651'),
 ('2026-10-27','Bioética','Einstein','TBL','TBL Bioética','3f91f5b2-a2e4-8181-b533-cbcb1a88e039'),
 ('2026-11-04','PTR3514 SIT','Poli','Proj','Projeto Final SIT','3f91f5b2-a2e4-819f-8b98-f41764006f75'),
 ('2026-11-05','PEF3401 Mecânica das Estruturas II','Poli','Proj','Trabalho 2 PEF3401',None),
 ('2026-11-06','BSDigEH','Einstein','TBL','TBL BSDigEH','3f91f5b2-a2e4-8185-840e-ffa37996eae1'),
 ('2026-11-09','Biomateriais','Einstein','TBL','TBL BioMat','3f91f5b2-a2e4-81eb-9d0c-dde346d08dfc'),
 ('2026-11-10','Modelagem e Simulação','Einstein','TBL','TBL ModelS','3f91f5b2-a2e4-81a8-bdc7-f89c6d9ed4e0'),
 ('2026-11-11','Sistemas Digitais','Einstein','P','P3 SisDig','3f91f5b2-a2e4-8139-af51-df76d2da5b82'),
 ('2026-11-13','BSDigEH','Einstein','TBL','TBL BSDigEH','3f91f5b2-a2e4-811b-9e53-d0a651877148'),
 ('2026-11-16','Biomateriais','Einstein','Lab','Lab BioMat','3f91f5b2-a2e4-81f7-b1cb-fd3f86d5f0bf'),
 ('2026-11-23','Cidades Inteligentes','Poli','Proj','Apresentação Cidades Inteligentes',None),
 ('2026-11-24','Bioética','Einstein','P','P2 Bioética','3f91f5b2-a2e4-81fd-98c3-c4c6477d2e25'),
 ('2026-11-26','PEF3401 Mecânica das Estruturas II','Poli','P','P2 PEF3401','3f91f5b2-a2e4-8197-b470-fbd227412424'),
 ('2026-11-26','PTR3522 Gestão de Pavimentos','Poli','P','P2 PTR3522','3f91f5b2-a2e4-8128-b13b-eb9bec17c994'),
 ('2026-11-27','BSDigEH','Einstein','P','P3 BSDigEH','3f91f5b2-a2e4-8100-921b-e9a6b3fc7bf4'),
 ('2026-12-01','PCC3412 Real Estate','Poli','P','P2 PCC3412','3f91f5b2-a2e4-812d-a726-d229fff74c8a'),
 ('2026-12-02','PTR3432 Aeroportos','Poli','P','P2 PTR3432','3f91f5b2-a2e4-8167-a619-c3e9ee518b9c'),
 ('2026-12-03','Física Médica','Einstein','P','P2 FisMed','3f91f5b2-a2e4-81f3-b728-e2154c4f0aa7'),
 ('2026-12-04','PEF3402 Estruturas de Aço','Poli','P','P2 PEF3402','3f91f5b2-a2e4-8185-85e6-cf52254ec039'),
 ('2026-12-07','Biomateriais','Einstein','P','P2 BioMat','3f91f5b2-a2e4-811e-86d0-f70e1cdf2279'),
 ('2026-12-07','Cidades Inteligentes','Poli','P','Prova final Cidades','3f91f5b2-a2e4-8165-a454-d22801a5cfa3'),
 ('2026-12-08','PTR3534 Transporte Aéreo','Poli','P','Prova final Transporte Aéreo','3f91f5b2-a2e4-81ea-9c22-ff1021eb30c7'),
]
PROVA_DAY_BLOCK = set()  # dia de prova: sem sessão depois dela -> simplificação: dia inteiro livre
for ds,m,fac,tp,nome,tid in A:
    if tp == 'P': PROVA_DAY_BLOCK.add(date.fromisoformat(ds))
REGRA = {('P','Einstein'): ([-14,-10,-7,-4,-2,-1],90), ('P','Poli'): ([-10,-7,-4,-2,-1],90),
         ('TBL',None): ([-7,-4,-2,-1],60), ('Lab',None): ([-3,-1],None), ('Proj',None): ([-10,-7,-4,-2],90)}
FOCO = {'P': {14:'Mapear o conteúdo da prova e montar o resumo geral.',10:'Teoria: revisar os resumos das aulas.',7:'Exercícios e listas.',4:'Provas antigas e tópicos mais cobrados.',2:'Refazer os exercícios que errou.',1:'Revisão leve dos pontos fracos.'},
        'TBL': {7:'Ler a pré-aula com calma.',4:'Fazer as questões/quiz da pré-aula.',2:'Revisar os conceitos-chave.',1:'Revisão rápida para o iRAT.'},
        'Lab': {3:'Ler o roteiro e revisar a teoria do lab.',1:'Revisão rápida do procedimento.'},
        'Proj': {10:'Planejar entregáveis e dividir tarefas.',7:'Desenvolver o projeto.',4:'Desenvolver e revisar.',2:'Fechar e revisar a entrega.'}}
TIPO = {'P':'Pré-prova','TBL':'Pré-TBL/Quiz','Lab':'Pré-lab','Proj':'Pré-prova'}
# datas já cobertas por sessões existentes da mesma avaliação
cob = {}
for ch, s, e in existentes:
    if ch.startswith('pre-'):
        k = ch.rsplit('-', 1)[0][4:]; dd = DT.fromisoformat(s.replace('Z','+00:00')).astimezone(TZ).date()
        cob.setdefault(k, []).append(dd)
chaves = {ch for ch, s, e in existentes}
pages = []; tot = 0
# ordem: avaliações mais próximas primeiro, offsets mais tardios primeiro (garante a reta final)
for ds,m,fac,tp,nome,tid in sorted(A):
    d = date.fromisoformat(ds)
    offs, dur = REGRA.get((tp,fac)) or REGRA[(tp,None)]
    k = nome.replace(' ','') + '-' + ds
    for o in sorted(offs, reverse=True):
        alvo = d + TD(days=o)
        if f"pre-{k}-d{-o}" in chaves: continue  # chave já existe (v3, 2026-10-18)
        if any(abs((c-alvo).days) <= 1 for c in cob.get(k, [])): continue
        du = dur or (60 if o == -3 else 30)
        if alvo < hoje.date(): continue
        dias = [alvo - TD(days=i) for i in range(0, 6) if alvo - TD(days=i) >= hoje.date()]
        if o == -1: dias = [alvo, alvo - TD(days=1)]
        r = place(dias, du, vespera=(o == -1))
        if not r: print('SEM ESPAÇO', nome, o); continue
        cob.setdefault(k, []).append(r[0])
        s = DT.combine(r[0], time(r[1]//60, r[1]%60), TZ); e = s + TD(minutes=du)
        props = {"Sessão": f"{m}: {TIPO[tp].lower()}", "date:Quando:start": s.isoformat(), "date:Quando:end": e.isoformat(), "date:Quando:is_datetime": 1,
                 "Matéria": m, "Faculdade": fac, "Tipo": TIPO[tp], "Avaliação": f"{nome} ({d.strftime('%d/%m')})",
                 "Foco": FOCO[tp][-o], "Duração (min)": du, "Status": "A fazer", "Chave": f"pre-{k}-d{-o}", "Criada pelo agente": "__YES__"}
        if tid: props["Tarefa"] = [tid]
        pages.append({"properties": props}); tot += du
        print(s.strftime('%a %d/%m %H:%M'), du, nome, f'D{o}')
json.dump(pages, open(out, 'w'), ensure_ascii=False)
print(len(pages), 'sessoes', round(tot/60,1), 'h')
