from pieces.Piece import Piece
from typing import Tuple

class King(Piece):
    def __init__(self, color: bool, position: Tuple[str, int], san_code: str):
        super().__init__(color, position, san_code)
    
    def set_movements(self,engine):
        matrix = engine.get_board()
        curr_pos = self.get_curr_pos()
        moves = []
        bounds= ['a','b','c','d','e','f','g','h']
        row= curr_pos[1] #0
        col= self.find_pos(curr_pos[0]) #3
        for i in range(row-1,row+2):
            if (i >= engine.board_size) | (i < 0): continue
            for j in range(col-1,col+2):
                if (j >= engine.board_size) | (j < 0): continue
                if (i == row) & (j == col): continue
                if matrix[i][j] == None:
                    newmove = (i,j) # casa vazia, pode mover
                    moves.append(newmove)
                elif matrix[i][j].get_color() == self.get_color(): #same color
                    pass
                elif matrix[i][j].get_color() != self.get_color(): #diff color
                    newmove = (i,j)
                    moves.append(newmove) #pode comer peça

        self.set_poss_moves(moves)
