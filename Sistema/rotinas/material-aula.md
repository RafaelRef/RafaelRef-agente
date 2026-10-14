# Rotina: material de aula (todo dia, 20h30)

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
- O ícone do recurso na página do curso (`li.activity.modtype_resource img`, ex.: `f/pdf`) diz o tipo antes de abrir. `core_course_get_contents` NÃO está disponível.
- `mod/resource/view.php` redireciona para `pluginfile.php/...`. PDF abre no visualizador do Chrome (testado 2026-10-14, não baixou). O Ref liberou download em 2026-10-14, mas prefira o método abaixo, que não salva nada.

## Método preferido para PDF: extrair texto na própria página (testado, rápido)

Com a aba numa página HTML do mesmo site (ex.: a página do curso), rode no javascript_tool:
1. `const pdfjs = await import('https://cdnjs.cloudflare.com/ajax/libs/pdf.js/4.2.67/pdf.min.mjs'); pdfjs.GlobalWorkerOptions.workerSrc='https://cdnjs.cloudflare.com/ajax/libs/pdf.js/4.2.67/pdf.worker.min.mjs';`
2. Pegue a URL do pluginfile (abra o view.php uma vez e leia a URL da aba, ou procure `pluginfile.php` no HTML), faça `fetch(url).then(r=>r.arrayBuffer())`, `getDocument({data})`, junte `getTextContent()` de cada página e guarde em `window.__txt`.
3. NÃO retorne o texto inteiro: a extensão bloqueia respostas com URLs e trunca respostas longas. Remova links (`/\S*(https?:|www\.|\?|=|&)\S*/g`), remova o rodapé repetido e devolva em blocos de 6 páginas, até ~1900 caracteres por chamada, usando browser_batch.
4. Páginas sem texto são imagens/gráficos: anote e, se forem importantes, leia por screenshot.
No Canvas, o link de download redireciona para outro domínio; testar o mesmo método antes de usar, senão manter a leitura por screenshot.
PPTX: não testado. Mesma ideia com JSZip (cdnjs) lendo `ppt/slides/slide*.xml`.

## Passos

1. Liste material novo nas duas plataformas (máximo 6 por execução, prioridade para aulas dos próximos 2 dias e Einstein).
2. Leia cada um no visualizador. Não baixe arquivos.
3. Escreva `Estudos/<materia>/<chave>.md`: conceitos-chave curtos, pré-requisitos e o que revisar, link para o original. Lista de exercício: o que cada questão pede, sem resolver. Prova antiga: atualize `Estudos/<materia>/topicos-mais-cobrados.md`.
4. Espelhe no Notion: na página "Estudos" (id `3f91f5b2-a2e4-81a3-8569-d5cf89035d29`) existe uma subpágina por matéria (veja `Sistema/notion.md`). Acrescente o resumo como uma seção `## <título da aula>` no TOPO da subpágina da matéria; se a matéria ainda não tiver subpágina, crie e registre o id em `Sistema/notion.md`. Antes de acrescentar, confira se a seção já existe (idempotência).
5. Tarefas: tudo no material que pede ação do Ref (instalar programa, entregar, ler antes, levar algo) vira tarefa no banco "Tarefas do Agente", com Tipo "Ação", Frente, Origem, Link, Prazo quando houver e Chave `<plataforma>-<id>-<assunto>`. Busque a Chave antes de criar.
6. Registre em `Sistema/material-visto.md` (plataforma, curso, id, nome, data).
7. Commit e push.

## Notificação

```
Material: <n> novos lidos (<matérias>)
Tarefas: <n> criadas (<a mais urgente>)
<falhas em uma linha, se houver>
```
Se o Chrome não estiver disponível: uma linha dizendo que pulou o dia.

## Decisões

- 2026-10-14: Ref liberou download no e-Disciplinas. Mesmo assim, extrair texto na página é o padrão, porque não deixa arquivo no computador dele.
