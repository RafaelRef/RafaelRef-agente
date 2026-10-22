# Log de falhas
- 2026-10-15 00:2x UTC | material-aula | extensão do Chrome desconectou uma vez no meio da leitura ("Browser extension is not connected"); voltou após ~30 s, sem perda.
- 2026-10-15 20:3x | material-aula | e-Disciplinas com sessão expirada (painel como "Visitante", AJAX do Moodle dá erro). Pulado sem login.
- 2026-10-18 18:0x | revisao-semanal | Prazos do Canvas não conferidos: execução em nuvem sem Chrome do Ref. Só agenda usada.
- 2026-10-18 18:0x | revisao-semanal | planejar_pre.py recriava sessões cuja chave já existia quando a sessão original tinha recuado mais de 1 dia do alvo. Corrigido (pula chave existente). planejar.py tem datas fixas de 14/10; substituído por planejar_man.py.
- 2026-10-22 11:4x UTC | material-aula | e-Disciplinas com sessão expirada de novo (painel "Visitante", userId 1, timeline AJAX devolve 0 cursos). Pulado sem login. Rodada atrasada (agendada 21/10 20h28 BRT, disparou 22/10 08h41 BRT).
- 2026-10-22 11:4x UTC | material-aula | Bioética não tem aba Arquivos nem itens File nos módulos: material vem linkado na descrição das Assignments "Aula N". Achado por /api/v1/courses/46174/assignments/<id>.
