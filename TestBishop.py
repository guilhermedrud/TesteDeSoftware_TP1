import unittest
from src.pieces.Piece import Piece
from src.Board import Board, classic
from src.ChessEngine import ChessEngine
    
class TestBishop(unittest.TestCase):
    def set_up(self):
        tab = Board("8/1B6/8/7b/4b3/5B2/1B4b1/3b4")
        self.B = ChessEngine(tab)
        self.B.update_movements()
    
    def test_white_moves(self):
        curr,dest = ("b2","f6")
        lose = self.B.move_piece(curr, dest, 1)
        self.assertEqual(lose, 0)

    