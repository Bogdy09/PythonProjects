# services/computer_player.py
from copy import deepcopy
from random import randint


class ComputerPlayer:
    def __init__(self, piece):
        """
        Initializes a computer player with the specified piece ('X' or 'O').

        :param piece: Player piece ('X' or 'O')
        :return None
        """
        self.piece = piece


    def make_move(self, board):
        """
        Determines the computer player's next move based on a strategy:
        1. If a winning move is available, make that move.
        2. If the opponent has a winning move, block it.
        3. If no winning or blocking move, play randomly.

        :param board: ConnectFourBoard instance
        :return: int (column index for the next move)
        """

        # Check for a winning move
        winning_move = self.find_winning_move(board)
        if winning_move is not None:
            return winning_move

        # Check for a blocking move
        blocking_move = self.find_blocking_move(board)
        if blocking_move is not None:
            return blocking_move

        # If no winning or blocking move, play randomly
        valid_moves = [col for col in range(board.width) if board.is_valid_move(col)]
        return valid_moves[randint(0, len(valid_moves) - 1)]

    def find_winning_move(self, board):
        """
        Finds a winning move for the computer player by simulating possible moves.

        :param board: ConnectFourBoard instance
        :return: int (column index for a winning move or None if no winning move is found)
        """
        for col in range(board.width):
            if board.is_valid_move(col):
                # Create a copy of the board to simulate the move
                board_copy = deepcopy(board)
                board_copy.make_move(col, self.piece)
                # Check if the move results in a win
                if board_copy.check_win(self.piece):
                    return col
        return None

    def find_blocking_move(self, board):
        """
        Finds a move to block the opponent from winning by simulating opponent's possible moves.

        :param board: ConnectFourBoard instance
        :return: int (column index for a blocking move or None if no blocking move is found)
        """
        opponent_piece = 'O' if self.piece == 'X' else 'X'
        for col in range(board.width):
            if board.is_valid_move(col):
                # Create a copy of the board to simulate opponent's move
                board_copy = deepcopy(board)
                board_copy.make_move(col, opponent_piece)
                # Check if the move blocks the opponent from winning
                if board_copy.check_win(opponent_piece):
                    return col
        return None
