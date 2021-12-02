from typing import Tuple, List, Char


class Piece:
    def __init__(self, color: bool, position: Tuple[str,int], san_code: str):
        self.color = color
        self.curr_pos = position
        self.possible_moves = []
        self.san_code = san_code
        self.bounds = ['a','b','c','d','e','f','g','h']
        self.translation = dict(enumerate(self.bounds))

    def find_pos(self,character: str):
        return self.translation[character]

    def highlight_possible_moves(self):
        current = self.get_curr_pos()
        text = str(current[0])+str(current[1])+" have "+len(self.possible_moves)+" legal movements: "
        for move in self.possible_moves:
            text += str(move[0])+str(move[1])+", "
        print(text)
    
    def set_curr_pos(self,position: Tuple[str,int]):
        self.curr_pos = position
    
    def get_color(self):
        return self.color
    