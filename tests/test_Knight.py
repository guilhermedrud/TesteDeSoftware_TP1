import unittest
from src.pieces.Piece import Piece
from src.Board import Board, classic
from src.ChessEngine import ChessEngine

class TestKnight(unittest.TestCase):
    def setUp(self):
        tab = Board("rnbqkbnr/ppppp1p1/P4p2/8/8/7p/1PPPPPPP/RNBQKBNR")
        self.B = ChessEngine(tab)
        self.B.update_movements()
    
    def test_white_moves(self):
        curr,dest = ("g1","f3")
        lose = self.B.move_piece(curr, dest, 1)
        self.assertEqual(lose, 0)

    def test_black_moves(self):
        curr,dest = ("b8","c6")
        lose = self.B.move_piece(curr, dest, -1)
        self.assertEqual(lose, 0)

    def test_invalid_move_block_by_friend(self):
        curr,dest = ("g8","f6")
        with self.assertRaises(Exception) as context:
            lose = self.B.move_piece(curr, dest, 1)   
        
    def test_invalid_move(self):
        curr,dest = ("g8","h7")
        with self.assertRaises(Exception) as context:
            lose = self.B.move_piece(curr, dest, 1) 

    def test_eat_piece_white(self):
        curr,dest = ("g1","h3")
        lose = self.B.move_piece(curr, dest, 1)
        self.assertEqual(lose, 0)

    def test_eat_piece_black(self):
        curr,dest = ("b8","a6")
        lose = self.B.move_piece(curr, dest, -1)
        self.assertEqual(lose, 0)


if __name__ == '__name__':
    unittest.main()
