# Aula 8: Modelos de desempenho e ciência de dados

Fonte: e-Disciplinas, PTR3522 Gestão de Pavimentos (curso 145852), recurso 6599742 (https://edisciplinas.usp.br/mod/resource/view.php?id=6599742). 45 slides. Lido em 2026-10-14. Aula de 15/10, 7h30.

## Conceitos-chave
- Modelo de desempenho prevê como o pavimento se deteriora no tempo. É a base do SGP para orçar manutenção e reabilitação e alocar recursos.
- Desempenho tem quatro aspectos: qualidade de rolamento, segurança, defeitos e capacidade estrutural. Depende de tráfego, clima, construção, drenagem e materiais.
- Determinístico (resultado único, ignora incerteza) x probabilístico (variáveis aleatórias, intervalos de confiança).
- Empírico: ajuste estatístico a dados observados (ex.: equação da AASHTO com log N, SN e perda de serventia).
- Empírico-mecanicista: calcula tensões, deformações e deslocamentos (TSCE, MEF) e liga isso a fadiga e deformação permanente por modelos calibrados em campo (NCHRP 1-37A; hoje se fala em calibração local).
- Probabilísticos: cadeias de Markov (transição depende só do estado atual, matriz de transição), semi-Markov (tempo em cada estado com qualquer distribuição) e análise de sobrevivência.
- ML: supervisionado (regressão para prever IRI em 5 anos; classificação para prever se passa de 3,5 m/km) x não supervisionado (clustering, componentes principais, detecção de anomalias).
- Pré-processamento: normalizar para métodos baseados em distância ou gradiente (redes neurais, SVM, kNN), o que árvores não exigem; Spearman é mais robusto a outliers que Pearson; correlação não é causalidade; multicolinearidade atrapalha a regressão linear.

## Pré-requisitos e o que revisar
- Serventia e IRI.
- Número estrutural (SN) e a lógica do método AASHTO.
- Probabilidade básica: matriz de transição e distribuições.

## Observação
Os slides 40 a 45 não têm texto extraível (provavelmente gráficos ou imagens).
