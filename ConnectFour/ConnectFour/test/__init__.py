import unittest

from domain.board import ConnectFourBoard
from services.computer_player import ComputerPlayer


class TestConnectFourBoard(unittest.TestCase):
    def setUp(self):
        self.board = ConnectFourBoard()
        self.computer_player=ComputerPlayer('O')

    def test_initialization(self):
        # Check if the board is initialized correctly
        self.assertEqual(self.board.width, 7)
        self.assertEqual(self.board.height, 6)

    def test_get_empty_cell(self):
        # Test getting a cell that is initially empty
        row, col = 0, 0
        self.assertEqual(self.board.get(row, col), ' ')



    def test_invalid_get(self):
        with self.assertRaises(IndexError):
            self.board.get(10, 10)

    def test_valid_move(self):
        col, piece = 2, 'X'
        self.assertTrue(self.board.make_move(col, piece))

    def test_invalid_move(self):
        # Test making an invalid move
        col, piece = 3, 'X'
        for _ in range(self.board.height):
            self.board.make_move(col, 'O')  # Fill the column
        self.assertFalse(self.board.make_move(col, piece))
        self.assertEqual(self.board.get(0, col), 'O')  # Ensure the column is still full

    def test_out_of_bounds_move(self):
        # Test making a move with an out-of-bounds column
        col, piece = 7, 'X'
        self.assertFalse(self.board.make_move(col, piece))

    def test_horizontal_win(self):
        # Test horizontal win
        piece = 'X'
        for col in range(0, 4):
            self.board.make_move(col, piece)
        self.assertTrue(self.board.check_win(piece))

    def test_vertical_win(self):
        # Test vertical win
        piece = 'O'
        for _ in range(4):
            self.board.make_move(2, piece)
        self.assertTrue(self.board.check_win(piece))

    def test_diagonal_win_top_left_to_bottom_right(self):
        # Test diagonal win from top-left to bottom-right
        piece = 'X'
        for i in range(4):
            self.board.make_move(i, piece)
        self.assertTrue(self.board.check_win(piece))

    def test_diagonal_win_top_right_to_bottom_left(self):
        # Test diagonal win from top-right to bottom-left
        piece = 'O'
        for i in range(3, -1, -1):
            self.board.make_move(i, piece)
        self.assertTrue(self.board.check_win(piece))

    def test_no_win(self):
        # Test when there is no win
        self.assertFalse(self.board.check_win('X'))
        self.assertFalse(self.board.check_win('O'))

    def test_block_move(self):
        self.board.make_move(1, 'X')
        self.board.make_move(1, 'X')
        self.board.make_move(1, 'X')
        self.assertTrue(self.computer_player.find_blocking_move(self.board), 1)

    def test_winning_move(self):
        self.board.make_move(2, 'O')
        self.board.make_move(2, 'O')
        self.board.make_move(2, 'O')
        self.assertTrue(self.computer_player.find_winning_move(self.board), 2)

if __name__ == '__main__':
    unittest.main()
