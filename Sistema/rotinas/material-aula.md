# Rotina: material de aula (fase 2, ainda não agendada)

Depende do Chrome do Ref ligado com a extensão Claude in Chrome e logado no Canvas e no e-Disciplinas. Nunca digite senha; se pedir login, pare e avise.

## Canvas (Einstein) — testado em 2026-10-14, funciona

- Base: `https://einstein.instructure.com`. A API responde com a sessão do navegador, sem token.
- Cursos: `GET /api/v1/courses?enrollment_state=active&per_page=50` (ler com get_page_text).
  Ids atuais: Bioética 46174, Bio Sist. Digestório/Endócrino/Hemato (BSDigEH) 46178, Biomateriais 45055, Física Médica 46179, Modelagem e Simulação 46180, Sistemas Digitais 46181. Ignorar 24756 (CPA), 31026 (Graduação), 46393 (Código Social, Ref é professor).
- Arquivos novos: `GET /api/v1/courses/<id>/files?sort=updated_at&order=desc&per_page=10`. Compare com `Sistema/material-visto.md`.
- Leitura: abra `/courses/<id>/files/<file_id>` (visualizador, NÃO o link `download`). O texto fica dentro do visualizador e get_page_text não pega; leia por screenshot: clique em tela cheia, diminua o zoom 2x e role, usando zoom na região do documento.
- Arquivos `.cv` (CircuitVerse) e `.csv` não são slides: só registre que existem.

## e-Disciplinas (Poli) — login ok, leitura pendente

- Base: `https://edisciplinas.usp.br`. A lista em /my/courses.php carrega vazia para o leitor; use a AJAX do Moodle via javascript na página:
  `core_course_get_enrolled_courses_by_timeline_classification` (classification inprogress) e `core_courseformat_get_state` (courseid) para listar recursos.
- Ids 2sem2026: TCC 144956, Cidades Inteligentes 142512, PCC3412 145010, PEF3401 143508, PEF3402 144954, PTR3432 144264, PTR3514 145054, PTR3522 145852 e 146072, PTR3534 144092.
- PROBLEMA: `mod/resource/view.php` redireciona direto para o arquivo, que pode ser baixado em vez de exibido. Não abrir até o Ref decidir como tratar (ver decisão abaixo).

## Passos

1. Liste material novo nas duas plataformas (máximo 6 por execução, prioridade para aulas dos próximos 2 dias e Einstein).
2. Leia cada um no visualizador. Não baixe arquivos.
3. Escreva `Estudos/<materia>/<chave>.md`: conceitos-chave curtos, pré-requisitos e o que revisar, link para o original. Lista de exercício: o que cada questão pede, sem resolver. Prova antiga: atualize `Estudos/<materia>/topicos-mais-cobrados.md`.
4. Registre em `Sistema/material-visto.md` (plataforma, curso, id, nome, data).
5. Commit e push.

## Decisão pendente

- e-Disciplinas: como ler sem baixar.
