import unittest
from src.pieces.Piece import Piece
from src.Board import Board, classic
from src.ChessEngine import ChessEngine
    
class TestBishop(unittest.TestCase):
    def setUp(self):
        tab = Board("8/1B6/7b/3Bb3/5B2/8/1B4b1/3b4")
        self.B = ChessEngine(tab)
        self.B.update_movements()
    
    def test_white_moves(self):
        curr,dest = ("b2","d4")
        lose = self.B.move_piece(curr, dest, 1)
        curr,dest = ("d4","g1")
        lose = self.B.move_piece(curr, dest, 1)
        self.assertEqual(lose, 0)

    def test_black_moves(self):
        curr,dest = ("h6","f8")
        lose = self.B.move_piece(curr, dest, -1)
        curr,dest = ("f8","a3")
        lose = self.B.move_piece(curr, dest, -1)
        self.assertEqual(lose, 0)

    def test_invalid_move_block_by_enemy(self):
        curr,dest = ("f4","f6")
        with self.assertRaises(Exception) as context:
            lose = self.B.move_piece(curr, dest, 1)   
        
    def test_invalid_move_block_by_friend(self):
        curr,dest = ("b7","d5")
        with self.assertRaises(Exception) as context:
            lose = self.B.move_piece(curr, dest, 1) 

    def test_eat_piece_white(self):
        curr,dest = ("f4","h6")
        lose = self.B.move_piece(curr, dest, 1)
        self.assertEqual(lose, 0)

    def test_eat_piece_black(self):
        curr,dest = ("g2","d5")
        lose = self.B.move_piece(curr, dest, -1)
        curr,dest = ("d5","b7")
        lose = self.B.move_piece(curr, dest, -1)
        self.assertEqual(lose, 0)


if __name__ == '__name__':
    unittest.main()