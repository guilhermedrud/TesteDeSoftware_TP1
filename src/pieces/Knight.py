from src.pieces.Piece import Piece
from typing import Tuple

class Knight(Piece):
    def __init__(self, color: bool, position: Tuple[str, int], san_code: str):
        super().__init__(color, position, san_code)
    
    def set_movements(self,engine):
        matrix = engine.get_board()
        curr_pos = self.get_curr_pos()
        moves = []
        bounds= ['a','b','c','d','e','f','g','h']
        row= curr_pos[1] #0
        col= self.find_pos(curr_pos[0]) #3
        
        if col+2 < engine.board_size: #leste
            if row+1 < engine.board_size: #cima
                if matrix[row+1][col+2] == None:
                    newmove = (row+1, col+2) # casa vazia, pode mover
                    moves.append(newmove)
                elif matrix[row+1][col+2].get_color() != self.get_color(): #diff color
                    newmove = (row+1,col+2)
                    moves.append(newmove)
            if row-1 >= 0: #baixo
                if matrix[row-1][col+2] == None:
                    newmove = (row-1, col+2) # casa vazia, pode mover
                    moves.append(newmove)
                elif matrix[row-1][col+2].get_color() != self.get_color(): #diff color
                    newmove = (row-1,col+2)
                    moves.append(newmove)
        
        if col-2 >= 0: #oeste
            if row+1 < engine.board_size: #cima
                if matrix[row+1][col-2] == None:
                    newmove = (row+1, col-2) # casa vazia, pode mover
                    moves.append(newmove)
                elif matrix[row+1][col-2].get_color() != self.get_color(): #diff color
                    newmove = (row+1,col-2)
                    moves.append(newmove)
            if row-1 >= 0: #baixo
                if matrix[row-1][col-2] == None:
                    newmove = (row-1, col-2) # casa vazia, pode mover
                    moves.append(newmove)
                elif matrix[row-1][col-2].get_color() != self.get_color(): #diff color
                    newmove = (row-1,col-2)
                    moves.append(newmove)
        
        if row+2 < engine.board_size: #norte
            if col+1 < engine.board_size: #dir
                if matrix[row+2][col+1] == None:
                    newmove = (row+2, col+1) # casa vazia, pode mover
                    moves.append(newmove)
                elif matrix[row+2][col+1].get_color() != self.get_color(): #diff color
                    newmove = (row+2,col+1)
                    moves.append(newmove)
            if col-1 >= 0: #esq
                if matrix[row+2][col-1] == None:
                    newmove = (row+2, col-1) # casa vazia, pode mover
                    moves.append(newmove)
                elif matrix[row+2][col-1].get_color() != self.get_color(): #diff color
                    newmove = (row+2,col-1)
                    moves.append(newmove)
        
        if row-2 < engine.board_size: #sul
            if col+1 < engine.board_size: #dir
                if matrix[row-2][col+1] == None:
                    newmove = (row-2, col+1) # casa vazia, pode mover
                    moves.append(newmove)
                elif matrix[row-2][col+1].get_color() != self.get_color(): #diff color
                    newmove = (row-2,col+1)
                    moves.append(newmove)
            if col-1 >= 0: #esq
                if matrix[row-2][col-1] == None:
                    newmove = (row-2, col-1) # casa vazia, pode mover
                    moves.append(newmove)
                elif matrix[row-2][col-1].get_color() != self.get_color(): #diff color
                    newmove = (row-2,col-1)
                    moves.append(newmove)
            

        self.set_poss_moves(moves)
