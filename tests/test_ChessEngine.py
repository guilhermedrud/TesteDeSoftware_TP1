import unittest
from src.pieces.Piece import Piece
from src.Board import Board, classic
from src.ChessEngine import ChessEngine

class TestChessEngine(unittest.TestCase):

    def setUp(self):
        tab = Board("3qrbnp/8/n4k2/5K2/8/3N4/8/4QRBP")
        self.B = ChessEngine(tab)
        self.B.update_movements()

    def test_move_piece(self):
        curr,dest = ("d3","b2")
        lose = self.B.move_piece(curr, dest, 1)
        self.assertEqual(lose, 0)

    def test_out_of_bounds_piece(self):
        with self.assertRaises(Exception) as context:
            coord = self.B.get_coordinates("a9")

    def test_no_piece_in_coordinate(self):
        curr,dest = ("a1","b2")
        with self.assertRaises(Exception) as context:
            lose = self.B.move_piece(curr, dest, 1)
    
    def test_try_to_move_wrong_color(self):
        curr,dest = ("d3","b2")
        with self.assertRaises(Exception) as context:
            lose = self.B.move_piece(curr, dest, -1)
    
    def test_invalid_movement(self):
        curr,dest = ("d3","e6")
        with self.assertRaises(Exception) as context:
            lose = self.B.move_piece(curr, dest, 1)
    
    def test_white_wins(self):
        curr,dest = ("f5","f6")
        lose = self.B.move_piece(curr, dest, 1)
        self.assertEqual(lose, -1)
    
    def test_black_wins(self):
        curr,dest = ("f6","f5")
        lose = self.B.move_piece(curr, dest, -1)
        self.assertEqual(lose, 1)

if __name__ == '__name__':
    unittest.main()