# Trabalho Prático Teste de Software: Jogo de Xadrez

### Nomes:

 - Guilherme Drummond Lima
 - Gabriel Lucas Freire Martins e Silva

## Sistema:

 - O sistema implementado consiste em um jogo de xadrez completo, possuindo todas as peças do jogo clássico. O sistema possui 9 classes no total, sendo 7 classes de peça, uma classe Board e uma classe ChessEngine.

### Piece:

- É a classe genérica para as peças de xadrez. Todas as demais classes de peça herdam de Piece e implementam seus respectivos movimentos. A classe armazena as informações da peça que serão usadas pela engine, como cor, código, posição e a lista de possíveis movimentos da peça

#### Classes filhas de Piece (Bishop, King, Knight, Pawn, Queen, Rook):

- Usam a estrutura básica de Piece, e implementam a função set_movements(), que gera os possíveis movimentos da peça dado a posição atual da peça e o tabuleiro.

### Board:

- Classe auxiliar de ChessEngine, focada em criar um tabuleiro a partir de uma FEN string. A notação Forsyth–Edwards (FEN) é uma notação padrão que descreve um estado particular de um tabuleiro de xadrez. Este [site](http://www.netreal.de/Forsyth-Edwards-Notation/index.php) cria FEN strings a partir de um tabuleiro customizado. O tabuleiro criado por essa classe é usado pelo ChessEngine para criar peças e manipulá-las.

### ChessEngine:

- Classe "principal" do sistema, usa o tabuleiro criado por Board para criar uma matriz de Pieces. Essa classe também realiza as movimentações das peças no tabuleiro, atualizando os possíveis movimentos de cada peça a cada jogada. Quando um King é comido, a Engine declara vitória ao outro jogador. A cada jogada, a engine também imprime o estado atual do tabuleiro.


