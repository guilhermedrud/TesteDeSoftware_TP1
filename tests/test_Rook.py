import unittest
from src.pieces.Piece import Piece
from src.Board import Board, classic
from src.ChessEngine import ChessEngine
    
class TestRook(unittest.TestCase):
    def setUp(self):
        #tab = Board("8/1B6/7b/3Bb3/5B2/8/1B4b1/3b4")
        tab = Board("rnbqkbn1/1pppppp1/5r2/p5Rp/P6P/8/1PPPPPP1/RNBQKBN1")
        self.B = ChessEngine(tab)
        self.B.update_movements()
    
    def test_white_moves(self):
        curr,dest = ("a1","a3")
        lose = self.B.move_piece(curr, dest, 1)
        self.assertEqual(lose, 0)

    def test_black_moves(self):
        curr,dest = ("a8","a6")
        lose = self.B.move_piece(curr, dest, -1)
        self.assertEqual(lose, 0)

    def test_invalid_move_block_by_enemy(self):
        curr,dest = ("g5","g8")
        with self.assertRaises(Exception) as context:
            lose = self.B.move_piece(curr, dest, 1)   
        
    def test_invalid_move_block_by_friend(self):
        curr,dest = ("a1","a5")
        with self.assertRaises(Exception) as context:
            lose = self.B.move_piece(curr, dest, 1) 

    def test_eat_piece_white(self):
        curr,dest = ("g5","g7")
        lose = self.B.move_piece(curr, dest, 1)
        self.assertEqual(lose, 0)

    def test_eat_piece_black(self):
        curr,dest = ("f6","f2")
        lose = self.B.move_piece(curr, dest, -1)
        self.assertEqual(lose, 0)


if __name__ == '__name__':
    unittest.main()
