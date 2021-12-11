from src.pieces.Piece import Piece
from src.pieces.Rook import Rook
from src.pieces.Bishop import Bishop
from src.pieces.King import King
from src.pieces.Knight import Knight
from src.pieces.Pawn import Pawn
from src.pieces.Queen import Queen
from src.Board import Board
import numpy as np
from typing import Tuple
from stockfish import Stockfish

class ChessEngine:
    def __init__(self, project: Board):
        self.board = project
        self.pieces = np.empty((project.size,project.size),dtype=Piece)
        self.board_size = project.size
        self.create_pieces(project)
        self.ai = Stockfish()

    def pair_to_str(self, row: int, col: int):
        bounds = ['a','b','c','d','e','f','g','h']
        st = bounds[col]
        line = str(row)
        st += line
        return st
    
    def create_pieces(self, project: Board):
        for i in range(project.size):
            for j in range(project.size):
                color = 1
                if project.get_position(i, j).isupper(): color=1
                else: color=-1
                if (project.get_position(i, j)=='k') | (project.get_position(i, j)=='K'):
                    king_piece =  King(color, self.pair_to_str(i,j), project.get_position(i, j))
                    self.pieces[i][j]= king_piece
                elif (project.get_position(i, j)=='q') | (project.get_position(i, j)=='Q'):
                    queen_piece = Queen(color, self.pair_to_str(i,j), project.get_position(i, j))
                    self.pieces[i][j]= queen_piece
                elif(project.get_position(i, j)=='b') | (project.get_position(i, j)=='B'):
                    bishop_piece = Bishop(color, self.pair_to_str(i,j), project.get_position(i, j))
                    self.pieces[i][j]= bishop_piece
                elif(project.get_position(i, j)=='n') | (project.get_position(i, j)=='N'):
                    knight_piece = Knight( color, self.pair_to_str(i,j), project.get_position(i, j))
                    self.pieces[i][j]= knight_piece
                elif(project.get_position(i, j)=='r') | (project.get_position(i, j)=='R'):
                    rook_piece = Rook( color, self.pair_to_str(i,j), project.get_position(i, j))
                    self.pieces[i][j]= rook_piece
                elif(project.get_position(i, j)=='p') | (project.get_position(i, j)=='P'):
                    pawn_piece = Pawn( color, self.pair_to_str(i,j), project.get_position(i, j))
                    self.pieces[i][j]= pawn_piece
        self.update_movements()
    
    def get_board(self):
        return self.pieces

    def update_board(self):
        board = np.empty((self.board_size,self.board_size), dtype=str)
        for i in range(self.board_size):
            for j in range(self.board_size):
                if self.pieces[i][j] != None:
                    board[i][j] = self.pieces[i][j].get_san_code()
                else:
                    board[i][j] = " "
        self.board.board = board

    def update_movements(self):
        for i in range(self.board_size):
            for j in range(self.board_size):
                # print(i,j)
                # print(self.pieces[i][j])
                if self.pieces[i][j] is not None:
                    # print("a")
                    self.pieces[i][j].set_movements(self)

    def get_coordinates(self, st: str):
        bounds = ['a','b','c','d','e','f','g','h']
        row = -1
        col = -1
        for i in range(self.board_size):
            if bounds[i]== st[0]: col = i
        row = int(st[1])-1
        kLast = self.board_size - 1
        if (row > kLast) | (row < 0) | (col > kLast) | (col < 0): raise Exception("invalid position")
        coord = (row,col)
        return coord

    def check_movement(self, curr_pos: Tuple, next_pos: Tuple):
        movements = self.pieces[curr_pos[0]][curr_pos[1]].get_poss_moves()
        if next_pos in movements:
            return True
        else: return False

    def move_piece(self, piece: str, destination: str, color: int):
        lose=0
        current = self.get_coordinates(piece)
        next = self.get_coordinates(destination)
        #print("current",current,",next",next)
        if self.pieces[current[0]][current[1]] == None: raise Exception("empty cell, no piece found")
        if self.pieces[current[0]][current[1]].get_color() != color: raise Exception("wrong color")
        if self.check_movement(current,next) == True:
            if self.pieces[next[0]][next[1]] != None:
                if self.pieces[next[0]][next[1]].get_san_code()=='K': lose=1
                if self.pieces[next[0]][next[1]].get_san_code()=='k': lose=-1
                self.pieces[next[0]][next[1]] = None; # come peça
            self.pieces[next[0]][next[1]] = self.pieces[current[0]][current[1]]
            self.pieces[current[0]][current[1]] = None
            new_pos = (destination[0],int(destination[1])-1)
            self.pieces[next[0]][next[1]].set_curr_pos(new_pos)
            self.update_movements()
        else:
            #print(self.pieces[current[0]][current[1]])
            self.pieces[current[0]][current[1]].highlight_possible_moves()
            raise Exception("invalid movement")
        return lose
    
    def ai_move(self,color):
        castle = " - - 0 1"
        self.update_board()
        board_str = self.board.to_string()
        fen_str = board_str+" "+color+castle
        self.ai.set_fen_position(fen_str)
        best_move = self.ai.get_best_move()
        return best_move[0:2]+" "+best_move[2:]

    def print_board(self):
        bounds = ['a','b','c','d','e','f','g','h']
        print("#| ",end="")
        for i in range(self.board_size):
            print('{:>3}'.format(bounds[i])+" ",end="")
        print("\n",end="")
        print("#|--------------------------------")
        for i in range(self.board_size-1,-1,-1):
            print(str(i+1)+"| ",end="")
            for j in range(self.board_size):
                if self.pieces[i][j]!= None: print('{:>3}'.format(self.pieces[i][j].get_san_code())+" ",end="")
                else: print('{:>3}'.format("_")+" ",end="")
            print("\n",end="")
        print("#|--------------------------------")
        print("#| ",end="")
        for i in range(self.board_size):
            print('{:>3}'.format(bounds[i])+" ",end="")
        print("\n",end="")

