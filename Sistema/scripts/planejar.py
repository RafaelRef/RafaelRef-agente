import json,sys
from datetime import datetime as DT, timedelta as TD, date, time
F=sys.argv[1]
ev=json.load(open(F))['events']
busy={}  # date -> list of (start,end) minutes
def add(d,a,b): busy.setdefault(d,[]).append((a,b))
for e in ev:
    if 'dateTime' in e['start']:
        s=DT.fromisoformat(e['start']['dateTime']); t=DT.fromisoformat(e['end']['dateTime'])
        add(s.date(), s.hour*60+s.minute-15, t.hour*60+t.minute+15)
# hoje 14/10: SisDig ate 18h
add(date(2026,10,14),0,18*60+15)
# dias bloqueados / parciais
add(date(2026,10,17),0,24*60)          # Meio Medico Bertioga
add(date(2026,10,16),19*60,24*60)      # Festa a noite
add(date(2026,10,30),12*60,24*60)      # Campos Bia e Isa
for d0 in range(0,22):
    d=date(2026,10,14)+TD(days=d0)
    add(d,12*60,13*60)                 # almoco
START=date(2026,10,14); END=date(2026,11,4)
load={}
def cap(d): return 360 if d.weekday()>=5 else 240
def free(d,a,b):
    if a<7*60 or b>22*60: return False
    for x,y in busy.get(d,[]):
        if a<y and x<b: return False
    return True
ORDER=list(range(18*60+30,22*60,15))+list(range(13*60+30,18*60,15))+list(range(9*60,12*60,15))+list(range(7*60,9*60,15))
def place(days,dur):
    for d in days:
        if d<START or d>END: continue
        if load.get(d,0)+dur>cap(d): continue
        for a in ORDER:
            if free(d,a,a+dur):
                add(d,a-15 if a>7*60 else a,a+dur+15); load[d]=load.get(d,0)+dur
                return d,a
    return None
S={ # nome, faculdade, dia da aula (0=seg), foco padrao
 'Sistemas Digitais':('Einstein',2), 'Física Médica':('Einstein',3), 'BSDigEH':('Einstein',4),
 'Biomateriais':('Einstein',0), 'Modelagem e Simulação':('Einstein',1), 'Bioética':('Einstein',1),
 'PTR3522 Gestão de Pavimentos':('Poli',3), 'PEF3401 Mecânica das Estruturas II':('Poli',3),
 'PEF3402 Estruturas de Aço':('Poli',4), 'PTR3534 Transporte Aéreo':('Poli',1), 'PCC3412 Real Estate':('Poli',1),
 'PTR3432 Aeroportos':('Poli',2), 'PTR3514 SIT':('Poli',2), 'Cidades Inteligentes':('Poli',0), 'TCC':('Poli',3)}
EVALS=[ # data, materia, tipo, nome
 (date(2026,10,16),'BSDigEH','P','P2 BSDigEH'),
 (date(2026,10,19),'Biomateriais','Lab','Lab BioMat'),
 (date(2026,10,20),'Modelagem e Simulação','TBL','TBL ModelS'),
 (date(2026,10,21),'Sistemas Digitais','TBL','Quiz SisDig'),
 (date(2026,10,27),'Bioética','TBL','TBL Bioética'),
 (date(2026,11,4),'PTR3514 SIT','P','Projeto Final SIT'),
 (date(2026,11,6),'BSDigEH','TBL','TBL BSDigEH'),
 (date(2026,11,9),'Biomateriais','TBL','TBL BioMat'),
 (date(2026,11,10),'Modelagem e Simulação','TBL','TBL ModelS'),
 (date(2026,11,11),'Sistemas Digitais','P','P3 SisDig'),
]
FOCO={'Sistemas Digitais':'Detecção e correção de erros: paridade, checksum, CRC, Hamming (resumo no Notion Estudos).',
      'PTR3522 Gestão de Pavimentos':'Aula 8: modelos de desempenho (empírico, M-E, Markov, ML). Resumo no Notion Estudos.'}
out=[]
pre_weeks=set()
for d,m,tp,nome in sorted(EVALS):
    fac=S[m][0]
    if tp=='P': offs,dur=([-6,-4,-2,-1] if fac=='Einstein' else [-5,-3,-1]),90; tipo='Pré-prova'
    elif tp=='TBL': offs,dur=[-2,-1],60; tipo='Pré-TBL/Quiz'
    else: offs,dur=[-1],30; tipo='Pré-lab'
    n=0
    for o in offs:
        tgt=d+TD(days=o)
        r=place([tgt,tgt-TD(days=1)],dur)
        if not r: continue
        n+=1; pre_weeks.add((m,r[0].isocalendar()[1]))
        out.append(dict(m=m,fac=fac,tipo=tipo,av=nome+' ('+d.strftime('%d/%m')+')',d=r[0],a=r[1],dur=dur,
          foco=FOCO.get(m,'Revisar todo o conteúdo da avaliação, listas e provas antigas.') if tp!='Lab' else 'Ler o roteiro do lab e revisar o procedimento.',
          chave=f"pre-{nome.replace(' ','')}-{d.isoformat()}-{n}"))
# manutencao semanal
wk=START-TD(days=START.weekday())
while wk<=END:
    for m,(fac,cd) in sorted(S.items(),key=lambda x:x[1][0]!='Einstein'):
        if (m,wk.isocalendar()[1]) in pre_weeks: continue
        cday=wk+TD(days=cd)
        days=[cday+TD(days=i) for i in range(0,5)]
        dur=60 if fac=='Einstein' or m=='TCC' else 45
        r=place(days,dur)
        if not r: continue
        out.append(dict(m=m,fac=fac,tipo='Manutenção',av='',d=r[0],a=r[1],dur=dur,
          foco=FOCO.get(m,'Revisar a aula da semana e fazer os exercícios.') if m!='TCC' else 'Avançar o TCC (logística humanitária).',
          chave=f"man-{m.split()[0]}-{wk.isocalendar()[1]}"))
    wk+=TD(days=7)
out.sort(key=lambda x:(x['d'],x['a']))
for o in out:
    s=DT.combine(o['d'],time(o['a']//60,o['a']%60)); e=s+TD(minutes=o['dur'])
    o['start']=s.strftime('%Y-%m-%dT%H:%M:00-03:00'); o['end']=e.strftime('%Y-%m-%dT%H:%M:00-03:00')
    print(s.strftime('%a %d/%m %H:%M'),o['dur'],o['tipo'],'|',o['m'],'|',o['av'])
print(len(out))
json.dump([{k:v for k,v in o.items() if k not in('d','a')} for o in out],open('plan.json','w'),ensure_ascii=False)
