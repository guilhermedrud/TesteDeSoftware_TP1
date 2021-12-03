import numpy as np

def classic():
    return "rnbqkbnr/pppppppp/8/8/8/8/PPPPPPPP/RNBQKBNR"

class Board:
    def __init__(self, inital_positions: str):
        self.valid_pieces = {'p', 'P', 'r', 'R', 'n', 'N', 'b', 'B', 'q', 'Q', 'k', 'K'}
        self.size = 8
        self.board = self.build_board(inital_positions)

    def build_board(self, board_str: str):
        num_lines = 0
        curline_len = 0
        print(board_str)
        corr_str = board_str.split("/")
        corr_str.reverse()
        print(corr_str)
        board_str = "/".join(corr_str)

        board = np.empty((self.size,self.size), dtype=str)
        for char in board_str:
            if num_lines == self.size: break
            if char.isdigit():
                spaces = int(char)
                if (spaces < 1) | (curline_len + spaces > self.size):
                    raise Exception("invalid board string")
                else:
                    for i in range(spaces):
                        board[num_lines][curline_len+i] = ' '
                    curline_len += spaces
            elif (char == '/') | ((num_lines == self.size - 1) & (char == ' ')):
                if curline_len != self.size :
                    raise Exception("invalid board string")
                else:
                    curline_len = 0
                    num_lines+=1
            elif curline_len == self.size:
                raise Exception("invalid board string")
            else:
                if char not in self.valid_pieces:
                    raise Exception("invalid board string")
                else:
                    board[num_lines][curline_len] = char
                    curline_len +=1
        if (num_lines == self.size) | ((num_lines == self.size - 1) & (curline_len == self.size)):
            return board
        else:
            raise Exception("invalid fen board string")
        
    def set_position(self, row: int, col: int, piece_code: str):
        if (row > self.size): raise Exception("row out of bounds")
        if (col > self.size): raise Exception("col out of bounds")
        if piece_code not in self.valid_pieces: raise Exception("invalid piece code")
        self.board[row][col] = piece_code

    def get_position(self, row: int, col: int):
        if (row > self.size): raise Exception("row out of bounds")
        if (col > self.size): raise Exception("col out of bounds")
        return self.board[row][col]
