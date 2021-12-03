from pieces.Piece import Piece
from Board import Board, classic
from ChessEngine import ChessEngine

def print_board(tab: Board):
    bounds = ['a','b','c','d','e','f','g','h']
    for i in range(tab.size):
        print(str(i+1)+"| ",end="")
        for j in range(tab.size):
            print('{:>3}'.format(tab.get_position(i-1, j))+" ",end="")
        print("\n",end="")
    print("0| ",end="")
    for i in range(tab.size):
        print('{:>3}'.format(bounds[i])+" ",end="")
    print("\n",end="")


if __name__ == "__main__":
    tab = Board("8/3R4/8/8/R2r2R1/8/8/3R4")
    B = ChessEngine(tab)
    B.update_movements()
    B.print_board()

    color =1
    lose = 0
    strcolor = 'White'
    while lose != 220:
        if color == 1: strcolor = "White"
        else: strcolor = "Black"
        print(strcolor+" player's turn")
        play = input()
        curr,dest =play.split(' ')
        try:
            lose = B.move_piece(curr, dest, color)
        except Exception as e:
            print("erro:",e)
            color = -color
        color = -color
        B.print_board()
    if lose == 1:
        print("Black win!")
    elif lose == -1:
        print("White win!")

