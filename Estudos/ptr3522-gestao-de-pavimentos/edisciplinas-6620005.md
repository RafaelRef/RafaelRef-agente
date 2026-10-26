# Aula 10: Sistemas de gerência viária, banco de dados e SIG

Fonte: e-Disciplinas, PTR3522 Gestão de Pavimentos (curso 145852; mesmo arquivo no 146072 como 6619994), recurso 6620005 (https://edisciplinas.usp.br/mod/resource/view.php?id=6620005). 34 slides. Lido em 2026-10-26. Junto vieram "LTPP_BOOK" e "Aula 11" (não lidos ainda).

## Conceitos-chave
- As cinco perguntas do gestor: que ativos temos e onde; em que condição estão e estarão; quanto valem; o que fazer e quanto custa manter; o que acontece sem recurso.
- SGP nasceu nos anos 1960 (falhas não previstas nos EUA e Canadá, pós AASHO Road Test).
- Dois níveis: rede (administrativo; necessidades da rede, previsão, priorização, orçamento; produto = programa plurianual) e projeto (técnico; alternativas num trecho, deflexão, sondagens, custo no ciclo de vida; produto = melhor alternativa).
- Componentes do SGP: banco de dados (inventário, trechos, condição e histórico, tráfego, intervenções, custos), modelos de desempenho, regras de tratamento, benefício/custo e otimização, relatórios e mapas.
- Dados por nível: rede usa IRI, afundamento, trincas, remendos, textura, em velocidade de tráfego; projeto usa mapeamento de trincas, FWD, transferência de carga, GPR e sondagens, a pé ou devagar. Exemplo de classe por IRI: bom < 1,5; regular 1,5 a 2,7 m/km.
- Banco de dados: usuários, aplicações (formulários, módulo de análise, QGIS), SGBD (SQL, regras, concorrência, segurança, backup), base de tabelas ligadas por chaves, DBA. Exemplos: Oracle, SQL Server, PostgreSQL/PostGIS, SQLite/GeoPackage.
- LTPP: criado em 1987 pelo SHRP (FHWA e AASHTO), coleta de desempenho por pelo menos 20 anos; módulos de estrutura e materiais, clima, tráfego, desempenho.
- O que padronizar: localização (coordenadas, via + km), ID da seção e do ativo (chave única entre tabelas), unidades, datas, situação da obra, arquivos.
- Referenciamento linear e segmentação dinâmica para juntar dados de fontes diferentes no SIG.
- Governança: dado é ativo. Relevância (finalidade definida), confiabilidade (representatividade, integridade, atualização), viabilidade (custo de coletar e manter).

## Pré-requisitos e o que revisar
- Aula 8 (modelos de desempenho, `edisciplinas-6599742.md`) e IRI.
- Noções de banco relacional (tabela, chave primária e estrangeira).

## Observação
Slides 9, 10, 12, 14, 16, 18 a 26 e 28 a 33 são figuras, sem texto extraível.
