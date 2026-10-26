# Aula 11: Priorização, otimização e decisão multicritério em Gestão de Pavimentos

Fonte: e-Disciplinas, PTR3522 Gestão de Pavimentos (curso 145852; mesmo material no 146072 como 6620003), recurso 6620007 (https://edisciplinas.usp.br/mod/resource/view.php?id=6620007). 32 slides, Profas. Kamilla Vasconcelos e Andréia Cargnin. Lido em 2026-10-26.

## Conceitos-chave
- Problema motivador: rede de 500 km, 180 km precisam de intervenção, custo R$ 60 mi, orçamento R$ 20 mi. Priorizar (ordenar trechos) não é o mesmo que otimizar (escolher a carteira que maximiza o benefício sob restrição).
- Critérios: condição técnica, econômico, social e operacional, ambiental.
- "Pior primeiro": corretivo e reativo, intervenções tardias e caras, gasta o orçamento em poucos trechos. Preventivo/estratégico: age antes da deterioração severa e atende mais trechos com o mesmo orçamento.
- Índice de condição x índice de priorização (este junta condição, tráfego, classe funcional, segurança, B/C).
- Modelos simplificados:
  - Extinto DNER (1994), rodovias federais: IP = (2·ICO + 3·IES)/5. IES vem de tabela conceito IGG x VSA; ICO vem de tabela QI x VDM (IRI ≈ (QI+10)/14, ou QI/13).
  - Tavakoli (1989), vias urbanas EUA: PI = (1/PCI)·TF·FC·TR·MF. TF fator de tráfego (10 a 100 por VDM), FC classe (1,0 local; 1,1 coletora; 1,2 arterial), TR 1,1 se rota de ônibus ou polo (escola, hospital), MF = 1 + IM/10 (IM de 0 nada a fazer até 5 reconstrução, pela faixa de PCI).
  - Bodi e Balbo (1998), vias de SP com base no HDM-3: B/C em função de VDM e VSA para três soluções de reforço (10 cm; fresagem 3 cm + 4 cm; 5 cm).
  - Vantagens: fácil, cabe em planilha. Limitações: calibrar escalas e pesos para a rede; ordem de prioridade não garante a melhor combinação de investimentos nem representa orçamento e dependências.
- MCDA (análise de decisão multicritério), três famílias:
  - Agregação por valor: SAW (soma ponderada S_i = Σ w_j·r_ij, com r normalizado 0 a 100) e AHP.
  - Solução ideal: TOPSIS.
  - Sobreclassificação: PROMETHEE (comparação par a par; evita que ótimo desempenho econômico compense segurança inaceitável).
- AHP: escala de Saaty (1 igual, 3 moderada, 5 forte, 7 muito forte, 9 extrema). Exemplo condição x tráfego x ambiental dá pesos 0,648, 0,230, 0,122. Consistência: CI = (λmax − n)/(n − 1); CR = CI/RI (RI depende do tamanho da matriz).
- TOPSIS: normalização vetorial r_ij = x_ij/√Σx², aplica pesos, distâncias às soluções ideal positiva e negativa, coeficiente de proximidade relativa. Exemplo com 4 projetos e critérios custo (minimizar, 30%), ganho de condição (45%), segurança (25%).
- Otimização: minimizar LCCA, maximizar condição da rede em 20 anos com orçamento anual, maximizar benefício ao usuário (redução de VOC). Prática: ranking multicritério e, quando cabe, otimização para escolher a carteira.
- Seleção de projetos como programação inteira binária (y_j = 1 se faz o projeto). Restrições típicas: excludentes x1 + x2 ≤ 1; dependência xA ≤ xB; no máximo n projetos Σx ≤ n; orçamento por ano Σ C_it·x_i ≤ O_t.
- Exemplo final: US$ 100 mi, 7 projetos (A a G). VPL aponta C (duplicação), B/C e TIR apontam G (ponte). A melhor carteira por soma de VP de benefícios é B + D + G (147). Depois entram benefícios não monetários (equidade, segurança, resiliência) para decidir.

## Pré-requisitos e o que revisar
- Aula 10 (`edisciplinas-6620005.md`) e Aula 8 (`edisciplinas-6599742.md`): índices de condição (IGG, VSA, PCI, IRI/QI).
- Engenharia econômica: VPL, B/C, TIR e por que rankings por indicador isolado divergem.
- Programação linear inteira (variável binária, restrição de orçamento).
- Autovalor/autovetor para o AHP.

## Observação
Slides 6, 7, 24, 26 a 28 são basicamente figuras (fluxo avaliação-seleção, tabela de investimentos do Prof. Barbieri). O slide 15 traz um exemplo para calcular PI e B/C de 11 vias (A a K), sem resposta nos slides: bom treino.
Junto no curso: "LTPP_BOOK" (6620006), livro FHWA-HRT-15-049 "The Long-Term Pavement Performance Program", 335 páginas, referência da Aula 10. Só registrado.
