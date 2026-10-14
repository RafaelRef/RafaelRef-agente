# Rotina: revisão semanal e plano de estudos (domingo, 18h)

Objetivo: manter o "Plano de Estudos" do Notion sempre cobrindo as próximas 3 semanas, com manutenção semanal de todas as matérias e intensificação antes de cada avaliação.

O plano vive no Notion, banco "Plano de Estudos" (data source `collection://e98bd3cf-c3e8-4745-a336-c82a1cd26fc9`, visão Calendário). A agenda Google `ESTUDOS` é só espelho para lembrete no celular.

## Passos

1. Avaliações: leia a agenda principal de hoje até o fim do semestre e atualize `Sistema/avaliacoes.md`. Avaliação = evento cujo título contém `P1`, `P2`, `P3`, `PSUB`, `SUB`, `TBL`, `QUIZ`, `Prova`, `Projeto Final`, `Entrega`, `Lab`, `Seminário`. Confira também prazos no Canvas (`/api/v1/courses/<id>/assignments?bucket=upcoming`) quando o Chrome estiver disponível. Ignore SUB (só se precisar) a menos que o Ref diga o contrário.
2. Leia o que já existe no banco para as próximas 3 semanas (query pela data). Respeite o Ref:
   - Sessão com Status "Feito" ou "Pulei": não mexa.
   - Sessão cujo horário não bate mais com o que o agente criou (o Ref moveu): mantenha onde ele pôs e registre em `Sistema/observacoes.md`.
   - Sessão "Pulei" de Pré-prova: tente repor uma sessão antes da avaliação.
3. Gere as sessões que faltam:
   - Manutenção semanal (próximas 3 semanas) com `Sistema/scripts/planejar.py`: 1 sessão por matéria por semana, dentro de 5 dias após a aula. Einstein 60 min, Poli 45 min, TCC 60 min. Sem manutenção da matéria na semana em que ela tem sessões pré-avaliação.
   - Pré-avaliação (TODAS as avaliações até o fim do semestre, não só 3 semanas) com `Sistema/scripts/planejar_pre.py`. Regra espaçada, começando cedo:
     - Prova Einstein: D-14, D-10, D-7, D-4, D-2, D-1 (90 min). Prova Poli: D-10, D-7, D-4, D-2, D-1 (90 min).
     - TBL e quiz: D-7 (ler a pré-aula), D-4, D-2, D-1 (60 min).
     - Lab: D-3 (60 min, roteiro e teoria) e D-1 (30 min).
     - Projeto/trabalho/apresentação: D-10, D-7, D-4, D-2 (90 min).
     - Cada sessão pode recuar até 5 dias se o dia-alvo estiver cheio. Não pula uma avaliação se já existe sessão dela a ±1 dia do alvo.
   - Restrições: 7h às 22h, 15 min de folga, almoço 12h-13h, quinta de manhã livre (o Ref apagou sessão ali), nada no dia de prova exceto a véspera de outra avaliação no dia seguinte. Teto diário: 4h dia útil e 6h fim de semana; na reta final (16/11 a 8/12) 5h e 7h.
   - Prioridade em conflito: avaliação mais próxima primeiro; pré-avaliação > manutenção Einstein > manutenção Poli.
   - Sessão que não coube: liste na notificação ("sem espaço: P2 X D-7").
4. Crie no banco só as sessões cuja Chave ainda não existe (Chave `man-<matéria>-<semana ISO>` ou `pre-<avaliação sem espaços>-<data>-d<dias antes>` (as antigas terminadas em `-1`, `-2` também contam)). Campo Foco: use o resumo mais recente em `Estudos/<materia>/` quando houver; senão "Revisar a aula da semana e fazer os exercícios."
4b. Tarefas de avaliação: toda avaliação com nota (prova, TBL, quiz, lab, projeto, entrega) tem UMA tarefa no banco "✅ Tarefas DB" (banco do Ref) com `Date` na data da avaliação, `Prioridade` (Urgente se faltam 48h ou menos, Alta para prova/projeto, Média para TBL/quiz/lab), `Áreas`, `Matéria`, `Faculdade`, `Avaliação` e Chave (campos e ids em `Sistema/notion.md`) `aval-<tipo>-<matéria>-<data>`. Crie as que faltam (inclusive avaliações novas que aparecerem na agenda ou no Canvas) e preencha a relação "Sessões de estudo" com todas as sessões pré-avaliação daquela avaliação. Nunca crie uma tarefa por sessão. Se a data mudou na agenda, atualize `Date`. Suba para Urgente quando entrar nas 48h. Nunca marque `Status`; isso é do Ref.
5. Espelho: para cada sessão das próximas 7 dias, crie/atualize evento na agenda `ESTUDOS` com título igual à Sessão e descrição `[agente] chave=<Chave>`. Apague só eventos `[agente]` cuja sessão não existe mais.
6. Escreva `Revisoes/<AAAA>-S<semana>.md`: sessões feitas x puladas na semana que passou (por matéria), avaliações das próximas 3 semanas, dias mais pesados.
7. Commit e push.

## Notificação

```
Semana: <n> avaliações (<lista curta>)
Estudo: <n> sessões, <h> horas; mais pesado <dia>
Semana passada: <feitas>/<total> sessões
```
