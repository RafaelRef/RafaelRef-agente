# Ids do Notion usados pelo agente

- Banco de tarefas "✅ Tarefas DB" (banco do Ref): data source `collection://3dd1f5b2-a2e4-8074-887c-000b271727ff`
- Página "Estudos": `3f91f5b2-a2e4-81a3-8569-d5cf89035d29`

## Subpáginas de Estudos (uma por matéria)

| Matéria | Pasta no repo | Id da página |
|---|---|---|
| Sistemas Digitais (Einstein) | Estudos/sistemas-digitais | 3f91f5b2-a2e4-818d-8dd0-fb05fcbc26fb |
| PTR3522 Gestão de Pavimentos (Poli) | Estudos/ptr3522-gestao-de-pavimentos | 3f91f5b2-a2e4-817c-bf6d-eb5702c14236 |
| BSDigEH (Einstein) | Estudos/bsdigeh | 3fa1f5b2-a2e4-8123-9837-e0b4b00cd7fb |
| Modelagem e Simulação (Einstein) | Estudos/modelagem-e-simulacao | 3fa1f5b2-a2e4-8150-9be3-f0d6576fd945 |
| PTR3432 Aeroportos (Poli) | Estudos/ptr3432-aeroportos | 3fa1f5b2-a2e4-813e-bd4f-c4caf75f96c2 |

- Banco "Plano de Estudos": data source `collection://e98bd3cf-c3e8-4745-a336-c82a1cd26fc9`, database `27248603c73143eca1700beb40cdaeac`, visão Calendário. Fica dentro da página "Estudos" (o Ref renomeou para "Guia de Estudos").

## Tarefas: usar SEMPRE o banco do Ref "✅ Tarefas DB"

- Data source `collection://3dd1f5b2-a2e4-8074-887c-000b271727ff` (página "Tarefas"). É o banco pessoal do Ref, com tarefas dele de HJE, InovaBio, TCC etc. Nunca mexa em tarefas que não têm "Criada pelo agente" marcado.
- Campos ao criar: `Name` (título), `Date` (prazo, data), `Prioridade` (Urgente se vence em até 48h; Alta para prova/projeto; Média para TBL/quiz/lab/ação), `Status` (checkbox; desmarcado = aberta; nunca marque), `Áreas` (relação: Faculdade Einstein `3dc1f5b2-a2e4-80fd-bf37-ecca47092b97`, Escola Politécnica `3dc1f5b2-a2e4-80ed-a1d4-e8a1c2a74009`, HJE `3dc1f5b2-a2e4-80a4-88d2-ea9883960550`, InovaBio `3dc1f5b2-a2e4-8045-97c9-c1e6b08b14a0`, Código Social `3dc1f5b2-a2e4-8049-b2ea-e00d1a089bd9`, IC `3dc1f5b2-a2e4-8044-84d4-f6a038ce5662`, TCC - Poli `3dc1f5b2-a2e4-8063-85ef-ff38ad1182c9`), `Matéria`, `Faculdade`, `Avaliação`, `Link`, `Chave`, `Criada pelo agente`.
- Relação `Sessões de estudo` liga a tarefa às sessões do Plano de Estudos (no Plano aparece como "Tarefa").
- Ao atualizar Prioridade: quando uma avaliação entra na janela de 48h, suba para Urgente.
- O banco antigo "Tarefas do Agente" (`collection://3e8ef189-f8e4-48e5-a034-83a9ae4b277b`) está DESCONTINUADO. Não leia nem escreva nele.
