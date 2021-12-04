from src.pieces.Piece import Piece
from typing import Tuple

class Bishop(Piece):
    def __init__(self, color: bool, position: Tuple[str, int], san_code: str):
        super().__init__(color, position, san_code)
    
    def set_movements(self,engine):
        matrix = engine.get_board()
        curr_pos = self.get_curr_pos()
        moves = []
        bounds= ['a','b','c','d','e','f','g','h']
        row= curr_pos[1] #0
        col= self.find_pos(curr_pos[0]) #3
        for i,j in zip(range(row-1,-1,-1),range(col-1,-1,-1)): # primeiro quadrante
            if matrix[i][j] == None:
                newmove = (i,j) # casa vazia, pode mover
                moves.append(newmove)
            elif matrix[i][j].get_color() == self.get_color(): #same color
                break; # aliado trava os movimentos subsequentes
            elif matrix[i][j].get_color() != self.get_color(): #diff color
                newmove = (i,j)
                moves.append(newmove) #pode comer peça
                break; #trava movimentos subsequentes

        for i,j in zip(range(row+1,engine.board_size) ,range(col-1,-1,-1)): # segundo quadrante
            if matrix[i][j] == None:
                newmove = (i,j) # casa vazia, pode mover
                moves.append(newmove)
            elif matrix[i][j].get_color() == self.get_color(): #same color
                break; # aliado trava os movimentos subsequentes
            elif matrix[i][j].get_color() != self.get_color(): #diff color
                newmove = (i,j)
                moves.append(newmove) #pode comer peça
                break; #trava movimentos subsequentes
        
        for i,j in zip(range(row+1,engine.board_size),range(col+1,engine.board_size)): # terceiro quadrante
            if matrix[i][j] == None:
                newmove = (i,j) # casa vazia, pode mover
                moves.append(newmove)
            elif matrix[i][j].get_color() == self.get_color(): #same color
                break; # aliado trava os movimentos subsequentes
            elif matrix[i][j].get_color() != self.get_color(): #diff color
                newmove = (i,j)
                moves.append(newmove) #pode comer peça
                break; #trava movimentos subsequentes
        
        for i,j in zip(range(row-1,-1,-1),range(col+1,engine.board_size)): # quarto quadrante
            if matrix[i][j] == None:
                newmove = (i,j) # casa vazia, pode mover
                moves.append(newmove)
            elif matrix[i][j].get_color() == self.get_color(): #same color
                break; # aliado trava os movimentos subsequentes
            elif matrix[i][j].get_color() != self.get_color(): #diff color
                newmove = (i,j)
                moves.append(newmove) #pode comer peça
                break; #trava movimentos subsequentes

        self.set_poss_moves(moves)
