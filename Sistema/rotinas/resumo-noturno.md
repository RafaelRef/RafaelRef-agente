# Rotina: resumo do dia seguinte (todo dia, 21h)

Objetivo: o Ref vai dormir sabendo como é o dia seguinte.

## Passos

1. Calcule "amanhã" em America/Sao_Paulo.
2. Leia os eventos de amanhã nas agendas `rafayosano@gmail.com` e `ESTUDOS`. Leia também os próximos 3 dias para achar provas, TBLs, quizzes e entregas (eventos de dia inteiro).
3. Leia o Gmail com `newer_than:1d`, focando em: `notifications@instructure.com` (Canvas), e-Disciplinas/USP, professores, Prof. Daniela Borri, e emails sobre HJE, InovaBio ou Código Social. Ignore promoções e newsletters.
4. Leia no Notion as tarefas "A fazer" com prazo até depois de amanhã.
5. Para cada aula de amanhã, se existir `Estudos/<materia>/` com resumo recente, inclua uma linha com o essencial.
6. Busque o clima de amanhã em São Paulo (Morumbi) na web.
7. Escreva `Diario/<data-de-amanha>.md` com: agenda do dia, provas próximas, tarefas, avisos de email relevantes, clima.
8. Se um email trouxer prazo novo com data, crie a tarefa no Notion (respeitando idempotência). Não crie eventos na agenda principal.
9. Commit e push.

## Notificação

Formato, no máximo ~8 linhas:
```
Amanhã: <primeira aula e horário> ... <último compromisso>
Atenção: <só itens urgentes, se houver>
Tarefas: <n> pendentes, <a mais importante>
Clima: <resumo em poucas palavras>
```
