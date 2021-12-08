import unittest
from src.pieces.Piece import Piece
from src.Board import Board, classic
from src.ChessEngine import ChessEngine

class TestQueen(unittest.TestCase):
    def setUp(self):
        tab = Board("rnb1kbn1/1p2ppp1/2p2r2/3p2Rp/pq5P/P1P1P3/1P1P1PP1/RNBQKBN1")
        self.B = ChessEngine(tab)
        self.B.update_movements()
    
    def test_white_moves(self):
        curr,dest = ("d1","c2")
        lose = self.B.move_piece(curr, dest, 1)
        self.assertEqual(lose, 0)

    def test_black_moves(self):
        curr,dest = ("b4","b6")
        lose = self.B.move_piece(curr, dest, -1)
        self.assertEqual(lose, 0)

    def test_invalid_move_block_by_enemy(self):
        curr,dest = ("b4","e1")
        with self.assertRaises(Exception) as context:
            lose = self.B.move_piece(curr, dest, 1)   
        
    def test_invalid_move_block_by_friend(self):
        curr,dest = ("d1","d4")
        with self.assertRaises(Exception) as context:
            lose = self.B.move_piece(curr, dest, 1) 

    def test_eat_piece_white(self):
        curr,dest = ("d1","h5")
        lose = self.B.move_piece(curr, dest, 1)
        self.assertEqual(lose, 0)

    def test_eat_piece_black(self):
        curr,dest = ("b4","h4")
        lose = self.B.move_piece(curr, dest, -1)
        self.assertEqual(lose, 0)


if __name__ == '__name__':
    unittest.main()
