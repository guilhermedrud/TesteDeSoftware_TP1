import unittest
from src.pieces.Piece import Piece
from src.Board import Board, classic
from src.ChessEngine import ChessEngine


class TestAI(unittest.TestCase):

    def setUp(self):
        tab = Board(classic())
        self.B = ChessEngine(tab)
        self.B.update_movements()

    def test_ai_move_piece_white(self):
        move = self.B.ai_move('w')
        print(move)
        self.assertEqual(move, "e2 e4")

    def test_ai_move_piece_black(self):
        move = self.B.ai_move('b')
        print(move)
        self.assertEqual(move, "e7 e5")


if __name__ == '__name__':
    unittest.main()