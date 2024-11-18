# ui/connect_four_ui.py
import time

from domain.board import ConnectFourBoard
from services.computer_player import ComputerPlayer

class UiError(Exception):
    pass

class ConnectFourUI:
    def __init__(self):
        self.board = ConnectFourBoard()
        self.computer_player = None

    def print_board(self):
        print(self.board)

    def run(self):
        try:
            while True:
                try:
                    player_piece = input('Choose X or O: ').upper()
                    if player_piece not in ('X', 'O'):
                        print("There was an error!")
                        print("Invalid input! Please choose X or O.")
                        continue  # Continue the loop to ask for input again

                    computer_piece = 'X' if player_piece == 'O' else 'O'
                    self.computer_player = ComputerPlayer(computer_piece)

                    print('To play: enter an integer between 1 and 7 corresponding to each column in the board.')
                    print(
                        'Whoever stacks 4 pieces next to each other, either horizontally, vertically, or diagonally wins.')

                    while True:
                        self.print_board()
                        try:
                            col = int(input('Your move (column 1-7): ')) - 1
                            if not (0 <= col < 7):
                                print("Invalid column! Please enter a number between 1 and 7.")
                                continue  # Continue the loop to ask for input again

                            if self.board.is_valid_move(col):
                                self.board.make_move(col, player_piece)
                                if self.board.check_win(player_piece):
                                    self.print_board()
                                    print(f"Congratulations! You won!")
                                    break
                                self.print_board()
                                print('Computer is thinking...')
                                computer_col = self.computer_player.make_move(self.board)
                                self.board.make_move(computer_col, computer_piece)

                                if self.board.check_win(computer_piece):
                                    self.print_board()
                                    print(f"Computer won! Better luck next time.")
                                    break
                            else:
                                print('Invalid move. The column is already full. Try again.')
                                time.sleep(1)
                        except ValueError:
                            print('Invalid input! Please enter a valid integer for the column.')
                except UiError as ve:
                    print("There was an error!")
                    print(ve)
        except ValueError as ve:
            print("There was an error!")


if __name__ == '__main__':
    connect_four_ui = ConnectFourUI()
    connect_four_ui.run()
