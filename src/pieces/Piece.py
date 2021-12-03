from typing import Tuple, List


class Piece:
    def __init__(self, color: bool, position:str, san_code: str):
        self.color = color
        self.curr_pos = (position[0],int(position[1]))
        self.possible_moves = []
        self.san_code = san_code
        self.bounds = ['a','b','c','d','e','f','g','h']
        self.translation = dict(zip(self.bounds,range(len(self.bounds))))  

    def find_pos(self,character: str):
        return self.translation[character]

    def highlight_possible_moves(self):
        current = self.get_curr_pos()
        text = str(current[0])+str(current[1])+" have "+str(len(self.possible_moves))+" legal movements: "
        for move in self.possible_moves:
            text += str(self.bounds[move[1]])+str(move[0]+1)+", "
        print(text)
    
    def set_curr_pos(self,position: Tuple[str,int]):
        self.curr_pos = position

    def get_curr_pos(self):
        return self.curr_pos
    
    def get_color(self):
        return self.color
    
    def set_poss_moves(self, moves: List):
        self.possible_moves = moves

    def get_san_code(self):
        return self.san_code
    
    def get_poss_moves(self):
        return self.possible_moves