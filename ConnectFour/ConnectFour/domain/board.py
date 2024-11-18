# domain/board.py
from texttable import Texttable


class ConnectFourBoard:
    def __init__(self, width: int = 7, height: int = 6):
        """
        Initializes a Connect Four board with the specified width and height.

        :param width: Width of the board (default: 7)
        :param height: Height of the board (default: 6)
        :return: None
        """
        self.__width = width
        self.__height = height
        self.__board = [[' ' for _ in range(width)] for _ in range(height)]

    @property
    def width(self):
        """
        Returns the width of the Connect Four board.

        :return: int
        """
        return self.__width

    @property
    def height(self):
        """
        Returns the height of the Connect Four board.

        :return: int
        """
        return self.__height

    def get(self, row: int, col: int):
        """
        Returns the content of the cell at the specified row and column on the Connect Four board.

        :param row: Row index
        :param col: Column index
        :return: str
        """
        return self.__board[row][col]

    def is_valid_move(self, col: int):
        """
        Returns True if making a move in the specified column is valid, otherwise returns False.

        :param col: Column index
        :return: bool
        """
        return 0 <= col < self.__width and self.__board[0][col] == ' '

    def make_move(self, col: int, piece: str):
        """
        Attempts to make a move by placing the specified piece in the specified column.

        :param col: Column index
        :param piece: Player piece ('X' or 'O')
        :return: bool (True if move is successful, False otherwise)
        """
        if self.is_valid_move(col):
            for row in range(self.__height - 1, -1, -1):
                if self.__board[row][col] == ' ':
                    self.__board[row][col] = piece
                    return True
        return False

    def __str__(self):
        """
        Returns a string representation of the Connect Four board suitable for printing.

        :return: str
        """
        t = Texttable()

        for i in range(self.__height):
            t.add_row([chr(ord('A') + i)] + self.__board[i])

        # Display column labels at the bottom
        hrow = [' '] + [str(i + 1) for i in range(self.__width)]
        t.add_row(hrow)


        return t.draw()

    def check_win(self, piece):
        """
        Checks if the specified player's pieces form a winning combination on the Connect Four board.

        :param piece: Player piece ('X' or 'O')
        :return: bool (True if there is a winning combination, False otherwise)
        """
        for row in range(self.__height):
            for each in range(self.__width - 3):
                if self.__board[row][each] == piece and self.__board[row][each + 1] == piece and self.__board[row][
                    each + 2] == piece and self.__board[row][each + 3] == piece:
                    return True

        for column in range(self.__width):
            for each in range(self.__height - 3):
                if self.__board[each][column] == piece and self.__board[each + 1][column] == piece and \
                        self.__board[each + 2][
                            column] == piece and self.__board[each + 3][column] == piece:
                    return True

        for row in range(self.__height - 3):
            for col in range(self.__width - 3):
                # Check diagonal (from top-left to bottom-right)
                if all(self.__board[row + i][col + i] == piece for i in range(4)):
                    return True

                # Check diagonal (from top-right to bottom-left)
                if all(self.__board[row + 3 - i][col + i] == piece for i in range(4)):
                    return True

        return False
