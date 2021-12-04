import unittest
from src.pieces.Piece import Piece
from src.Board import Board, classic
from src.ChessEngine import ChessEngine
    
class TestKing(unittest.TestCase):
    def setUp(self):
        tab = Board("8/1k4k1/2P5/8/8/2p5/1KP3K1/8")
        self.B = ChessEngine(tab)
        self.B.update_movements()
    
    def test_white_moves(self):
        curr,dest = ("g2","f3")
        lose = self.B.move_piece(curr, dest, 1)
        curr,dest = ("f3","g3")
        lose = self.B.move_piece(curr, dest, 1)
        self.assertEqual(lose, 0)

    def test_black_moves(self):
        curr,dest = ("g7","g6")
        lose = self.B.move_piece(curr, dest, -1)
        curr,dest = ("g6","h7")
        lose = self.B.move_piece(curr, dest, -1)
        self.assertEqual(lose, 0)

    def test_invalid_move_unreachable(self):
        curr,dest = ("b2","b4")
        with self.assertRaises(Exception) as context:
            lose = self.B.move_piece(curr, dest, 1)   
        
    def test_invalid_move_block_by_friend(self):
        curr,dest = ("b2","c2")
        with self.assertRaises(Exception) as context:
            lose = self.B.move_piece(curr, dest, 1) 

    def test_eat_piece_white(self):
        curr,dest = ("b2","c3")
        lose = self.B.move_piece(curr, dest, 1)
        self.assertEqual(lose, 0)

    def test_eat_piece_black(self):
        curr,dest = ("b7","c6")
        lose = self.B.move_piece(curr, dest, -1)
        self.assertEqual(lose, 0)
    
    def test_game_ends_on_white_death(self):
        curr,dest = ("c3","b2")
        lose = self.B.move_piece(curr, dest, -1)
        self.assertEqual(lose, 1)
    
    def test_game_ends_on_black_death(self):
        curr,dest = ("c6","b7")
        lose = self.B.move_piece(curr, dest, 1)
        self.assertEqual(lose, -1)


if __name__ == '__name__':
    unittest.main()