import unittest
from src.pieces.Piece import Piece
from src.Board import Board, classic
from src.ChessEngine import ChessEngine

class TestBoard(unittest.TestCase):
    
    def test_empty_board(self):
        tab = Board("8/8/8/8/8/8/8/8")
        self.assertEqual(tab.to_string(),"8/8/8/8/8/8/8/8")

    def test_correct_board(self):
        tab = Board("2q5/3p2b1/7K/8/2R1b3/8/1k3N2/8")
        self.assertEqual(tab.to_string(),"2q5/3p2b1/7K/8/2R1b3/8/1k3N2/8")
    
    def test_classic_board(self):
        tab = Board(classic())
        self.assertEqual(tab.to_string(),classic())

    def test_invalid_board_piece(self):
        with self.assertRaises(Exception) as context:
            tab = Board("8/8/8/8/7Y/8/8/8")
    
    def test_invalid_board_extra_char(self):
        with self.assertRaises(Exception) as context:
            tab = Board("bpppnrkq/bqbqnrqp/8/8/8/8/RPPNBBBN/PNKBQQRQ/")
    
    def test_invalid_string_space(self):
        with self.assertRaises(Exception) as context:
            tab = Board("bpppnrkq/bqbqnrqp/8/8/8/8/RP PNBBBN/PNKBQQRQ")
    
    def test_invalid_string_line_missing(self):
        with self.assertRaises(Exception) as context:
            tab = Board("bpppnrkq/bqbqnrqp/8/8/8//RPPNBBBN/PNKBQQRQ")

if __name__ == '__name__':
    unittest.main()