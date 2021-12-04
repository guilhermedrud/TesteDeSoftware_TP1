from pieces.Piece import Piece
from typing import Tuple

class Pawn(Piece):
    def __init__(self, color: bool, position: Tuple[str, int], san_code: str):
        super().__init__(color, position, san_code)
    
    def set_movements(self,engine):
        matrix = engine.get_board()
        curr_pos = self.get_curr_pos()
        moves = []
        bounds= ['a','b','c','d','e','f','g','h']
        row= curr_pos[1] #0
        col= self.find_pos(curr_pos[0]) #3
        
        color = self.get_color()
        if color == 1:
            if (row+1 < engine.board_size) & (col-1 >= 0):
                if (matrix[row+1][col-1] != None):
                    if ( matrix[row+1][col-1].get_color() != self.get_color()):
                        newmove = (row+1,col-1) # com inimigo, pode mover
                        moves.append(newmove)
            
            if (row+1 < engine.board_size) & (col+1 < engine.board_size):
                if (matrix[row+1][col+1] != None):
                    if( matrix[row+1][col+1].get_color() != self.get_color()):
                        newmove = (row+1,col+1) # com inimigo, pode mover
                        moves.append(newmove)
            
            if (row+1 < engine.board_size) & (matrix[row+1][col] == None):
                newmove = (row+1,col) # frente livre, pode mover
                moves.append(newmove)
            
            if row == 1:
                if (matrix[row+2][col] == None) & (matrix[row+1][col] == None):
                    newmove = (row+2,col) # frente livre, pode mover
                    moves.append(newmove)
            
        else:
            if (row-1 >=0 & col-1 >= 0):
                if(matrix[row-1][col-1] != None):
                    if (matrix[row-1][col-1].get_color() != self.get_color()):
                        newmove = (row-1,col-1) # com inimigo, pode mover
                        moves.append(newmove)
            
            if (row-1 >=0) & (col+1 < engine.board_size):
                if(matrix[row-1][col+1] != None):
                    if ( matrix[row-1][col+1].get_color() != self.get_color()):
                        newmove = (row-1,col+1) # com inimigo, pode mover
                        moves.append(newmove)
            
            if (row-1 >= 0) & (matrix[row-1][col] == None):
                newmove = (row-1,col) # frente livre, pode mover
                moves.append(newmove)
            
            if row == 6:
                if (matrix[row-2][col] == None) & (matrix[row-1][col] == None):
                    newmove = (row-2,col) # frente livre, pode mover
                    moves.append(newmove)

        self.set_poss_moves(moves)
