from src.pieces.Piece import Piece
from typing import Tuple

class Rook(Piece):
    def __init__(self, color: bool, position: Tuple[str, int], san_code: str):
        super().__init__(color, position, san_code)
    
    def set_movements(self,engine):
        #print("@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@")
        matrix = engine.get_board()
        #print(matrix)
        curr_pos = self.get_curr_pos()
        moves = []
        bounds= ['a','b','c','d','e','f','g','h']
        #print(curr_pos)
        row= curr_pos[1] #0
        col= self.find_pos(curr_pos[0]) #3
        #print("rowcol:", row,col, matrix[row][col])
        for i in range(row-1,-1,-1): # down
            if matrix[i][col] == None:
                newmove = (i, col) # casa vazia, pode mover
                moves.append(newmove)
            elif matrix[i][col].get_color() == self.get_color(): #same color
                break; # aliado trava os movimentos subsequentes
            elif matrix[i][col].get_color() != self.get_color(): #diff color
                newmove = (i,col)
                moves.append(newmove) #pode comer peça
                break; #trava movimentos subsequentes

        for i in range(row+1,engine.board_size): #up
            if matrix[i][col] == None:
                newmove = (i,col) # casa vazia, pode mover
                moves.append(newmove)

            elif matrix[i][col].get_color() == self.get_color(): #same color
                break; # aliado trava os movimentos subsequentes
            
            elif matrix[i][col].get_color() != self.get_color(): #diff color
                newmove = (i,col)
                moves.append(newmove) #pode comer peça
                break; #trava movimentos subsequentes
        
        for i in range(col+1,engine.board_size): #right
            if matrix[row][i]== None:
                newmove = (row,i) #casa vazia, pode mover
                moves.append(newmove)
            
            elif matrix[row][i].get_color() == self.get_color(): # same color
                break
            
            elif matrix[row][i].get_color() != self.get_color(): # diff color
                newmove = (row,i)
                moves.append(newmove)
                break
        
        for i in range(col-1,-1,-1): #left
            if matrix[row][i]== None:
                newmove = (row,i) #casa vazia, pode mover
                moves.append(newmove)

            elif matrix[row][i].get_color() == self.get_color(): # same color
                break
            
            elif matrix[row][i].get_color() != self.get_color(): #diff color
                newmove = (row,i)
                moves.append(newmove)
                break

        #print(self.get_san_code(),moves)
        self.set_poss_moves(moves)
        #print("@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@")
