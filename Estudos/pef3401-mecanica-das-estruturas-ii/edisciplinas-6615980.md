# Enunciado do T2: pórtico de 1 GL com excitação de suporte

Fonte: e-Disciplinas, PEF3401 (curso 143508), recurso 6615980 (https://edisciplinas.usp.br/mod/resource/view.php?id=6615980). 6 páginas. Lido em 2026-10-26.

## Prazo e regras
- O enunciado diz entrega até 23h59 de 12/11/2026 via Moodle. A agenda tem "Entrega do Trabalho 2" em 05/11 (evento de agosto). Pela regra a agenda vence; vale confirmar com o professor.
- Grupos de até 4, podem ser de turmas diferentes. Um membro digita os valores no Moodle. Correção automática, sem revisão nem análise de memória de cálculo. Respeitar as casas decimais do formulário.
- Valores de s0 (mm) e frequência f (Hz) dependem do número do grupo (Tabela 1, grupos 1 a 27). Dados de cada grupo nos recursos "G<n>-Dados", com script Python de leitura e vídeo do ensaio.

## Contexto
Pórtico sobre mesa vibratória, alvos refletivos (7) filmados por câmeras de captura de movimento, posições em mm. Modelo analítico: shear building de 1 GL, viga rígida, colunas inextensíveis, m = 0,473 kg. Três ensaios: estático (posição dos alvos), vibração livre, excitação de suporte s(t) = s0 sen(ωt).

## O que cada item pede (sem resolver)
- a) Taxa de amortecimento ξ, usando o decremento logarítmico entre dois picos e a fórmula exata ξ = δ / sqrt((2π)² + δ²).
- b) Frequência natural não amortecida (rad/s), rigidez equivalente (N/m) e constante de amortecimento (Ns/m).
- c) Deslocamento máximo experimental do Alvo 5 em relação ao suporte (mm).
- d) Deslocamento máximo analítico da massa em relação ao suporte (mm), com a) e b).
- e) Aceleração máxima experimental do Alvo 5 em relação ao suporte (m/s²).
- f) Aceleração máxima analítica da massa em relação ao suporte (m/s²).
- g) Fator de transmissibilidade TR e deslocamento máximo absoluto da massa (mm).
- h) Ângulo de fase entre excitação e deslocamento relativo (graus).
- Observação: usar regime permanente, descartando transitórios.

## Pré-requisitos e o que revisar
- Vibração livre amortecida e decremento logarítmico.
- Excitação de base: fator de amplificação dinâmica, transmissibilidade e fase em função de β = ω/ωn e ξ.
- Derivar aceleração a partir de posição medida (diferenças finitas ou ajuste senoidal).
