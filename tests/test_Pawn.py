import unittest
from src.pieces.Piece import Piece
from src.Board import Board, classic
from src.ChessEngine import ChessEngine
    
class TestPawn(unittest.TestCase):
    def setUp(self):
        tab = Board("8/3p2p1/8/2p1p3/1P1P4/8/4P1P1/8")
        self.B = ChessEngine(tab)
        self.B.update_movements()
    
    def test_white_moves(self):
        curr,dest = ("e2","e3")
        lose = self.B.move_piece(curr, dest, 1)
        curr,dest = ("e3","e4")
        lose = self.B.move_piece(curr, dest, 1)
        self.assertEqual(lose, 0)
    
    def test_white_double_move_on_first_play(self):
        curr,dest = ("g2","g4")
        lose = self.B.move_piece(curr, dest, 1)
        self.assertEqual(lose, 0)

    def test_black_moves(self):
        curr,dest = ("g7","g6")
        lose = self.B.move_piece(curr, dest, -1)
        curr,dest = ("g6","g5")
        lose = self.B.move_piece(curr, dest, -1)
        self.assertEqual(lose, 0)
    
    def test_black_double_move_on_first_play(self):
        curr,dest = ("g7","g5")
        lose = self.B.move_piece(curr, dest, -1)
        self.assertEqual(lose, 0)

    def test_black_move_block(self):
        curr,dest = ("d7","d5")
        lose = self.B.move_piece(curr, dest, -1) 
        curr,dest = ("d5","d4")
        with self.assertRaises(Exception) as context:
            lose = self.B.move_piece(curr, dest, -1)

    def test_white_move_block(self):
        curr,dest = ("e2","e4")
        lose = self.B.move_piece(curr, dest, 1) 
        curr,dest = ("e4","e5")
        with self.assertRaises(Exception) as context:
            lose = self.B.move_piece(curr, dest, 1)      

    def test_eat_piece_white(self):
        curr,dest = ("d4","e5")
        lose = self.B.move_piece(curr, dest, 1)
        self.assertEqual(lose, 0)

    def test_eat_piece_black(self):
        curr,dest = ("c5","d4")
        lose = self.B.move_piece(curr, dest, -1)
        self.assertEqual(lose, 0)


if __name__ == '__name__':
    unittest.main()