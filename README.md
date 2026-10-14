# Agente pessoal

Memória e "código" do agente pessoal do Ref. Cada rotina agendada é uma sessão nova do Claude que lê `CLAUDE.md`, `Perfil.md` e o prompt em `Sistema/rotinas/`, usa os conectores e faz commit do que mudou. Para desfazer qualquer coisa: `git revert`.

## Estrutura

- `CLAUDE.md`: regras globais (autonomia, segurança, fontes da verdade).
- `Perfil.md`: preferências explícitas e aprendidas.
- `Sistema/rotinas/`: um arquivo por rotina.
- `Sistema/log.md`, `Sistema/suspeitos.md`, `Sistema/observacoes.md`: falhas, conteúdo hostil, observações para aprendizado.
- `Diario/`: um arquivo por dia.
- `Revisoes/`: revisões semanais.
- `Estudos/<materia>/`: resumos de aula e tópicos mais cobrados.

## Rotinas

| Quando | Rotina | Status |
|---|---|---|
| Todo dia 21h | Resumo do dia seguinte | ativa |
| Domingo 18h | Revisão semanal + blocos de estudo | ativa |
| Todo dia 20h30 | Material de aula (Canvas, e-Disciplinas) + Notion | ativa (precisa do computador ligado) |
| Diária | Triagem de email | fase 2 |
| Semanal | Entidades (HJE, InovaBio, IC) | fase 3 |

## Para mudar algo

Edite o arquivo da rotina ou `Perfil.md` aqui mesmo, ou peça ao Claude no chat.
