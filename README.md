# Algoritmo A* (A-estrela) para a obtenção de um caminho ótimo

## O que é o A* (A-estrela)?
A-estrela é um algoritmo de busca de caminho, ou seja, tem o objetivo de determinar um caminho entre um vértice inicial e um vértice final. Para a determinação do caminho, é utilizada uma combinação de aproximações heurísticas e do Algoritmo de Dijkstra.

## Aplicação
Nesta aplicação, o algoritmo desenvolvido tem como objetivo determinar o melhor caminho entre as posições final e inicial em um tabuleiro. 

### Regras
Para sair da posição inicial para a final, o jogador deve respeitar as seguintes regras:
- O jogador só pode se mover dentro dos limites do tabuleiro;
- Paredes são intransponíveis e posições inválidas;
- Só é possível se movimentar para: cima, baixo, direita e esquerda.

### Formatação do Tabuleiro
O tabuleiro deve ser formatado em um arquivo texto chamado ```board.txt``` baseado no exemplo abaixo:
```
s 1 0 0 0 0
0 0 0 0 0 0
0 1 0 1 0 0
0 1 0 0 1 0
0 0 0 0 1 e
```
Em que:
- ```s```: posição inicial;
- ```e```: posição final;
- ```1```: posições inválidas (paredes);
- ```0```: posições válidas.
