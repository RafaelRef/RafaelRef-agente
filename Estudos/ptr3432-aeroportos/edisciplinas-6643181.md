# Aula 09: Terminais de passageiros

Fonte: e-Disciplinas, PTR3432 Aeroportos (curso 144264), recurso 6643181 (https://edisciplinas.usp.br/mod/resource/view.php?id=6643181), "09 - Terminais 202602". Lido em 2026-11-26 por mapa de seções e leitura dos slides de dimensionamento (118 slides; muitos são fotos históricas). Cai na P2 de 02/12.

## Mapa
- 1 a 29: história dos terminais (Hamburgo 1928, Tempelhof, Zurique, Le Bourget, CDG T1) e Congonhas em detalhe (concepção original, ala norte, píer, arte do terminal).
- 30 a 54: tipos de terminal: finger/píer, satélite, transporter (Dulles), linear, unidades; exemplos GIG, DFW, CDG, AMS, ATL, IAH, LGA.
- 55 a 70: relação terminal x pátio; estacionamento power-in/power-out x power-in/tow-out; píer com satélite (Chek Lap Kok, Kansas City).
- 71 a 80: redes de transporte aéreo (hub e conexões).
- 81 a 102: componentes e dimensionamento.
- 105 a 108: exercícios de nível de serviço.
- 110 a 115: caso do novo terminal de Congonhas (Aena, entrega jun/2028) e Fator Q da 7ª rodada.

## Conceitos-chave
- Processamento: lado terra (meio-fio, saguão), check-in, segurança e passaporte, espera de embarque, embarque; no desembarque, restituição de bagagem e saída.
- Nível de serviço: IATA antiga (1996) com letras A a F; IATA atual (ADRM, desde 2014) com dois eixos, espaço por passageiro e tempo máximo de fila, e faixas superdimensionado, ótimo e subótimo.
- PEA da ANAC: demanda de projeto na 30ª hora mais movimentada do ano, janelas de 60 min sem sobreposição. Congonhas 2025: cerca de 2.286 pax/h de origem e destino no embarque.
- Equações: saguões com acompanhantes (fator 1 + v.a.); demais componentes sem esse termo. Em áreas de espera To é tempo médio; em filas, tempo máximo. Tempo de serviço de referência: check-in 150 s (dom.) e 180 s (int.); inspeção 25 s e 37 s.
- Meio-fio: vagas por modal, arredondadas pra cima; comprimento = vagas x comprimento da vaga (Manual de Anteprojeto da ANAC, 2023). Esteiras de bagagem: cada voo numa só esteira, só conta frente acessível.
- Capacidade horária CHp = Ad x 60 / (Emp x To). Gatilho de investimento (7ª rodada) quando a demanda na hora-pico chega a 85% da capacidade do componente.
- Exercício da aula: sala de 25 m x 8 m (200 m²), LOS C com 1 m²/pax e permanência de 30 min dá a capacidade horária; se um voo de 300 pax atrasa e a espera vai pra 1 h, o espaço cai pra 0,67 m²/pax, entre LOS D e E.

## Pré-requisitos e o que revisar
- Aula 05 (cadeia de dimensionamento e hora-pico).
- Refazer o exercício da sala de embarque e saber usar CHp com os tempos de referência. Tem também o "Teste em Sala - Terminais" no e-Disciplinas.
