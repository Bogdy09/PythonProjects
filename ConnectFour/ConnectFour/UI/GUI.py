import tkinter as tk
from tkinter import messagebox
from domain.board import ConnectFourBoard
from services.computer_player import ComputerPlayer

class ConnectFourGUI:
    def __init__(self):
        self.root = tk.Tk()
        self.root.title("Connect Four")

        self.board = ConnectFourBoard()
        self.computer_player = ComputerPlayer('O')

        self.create_widgets()

    def create_widgets(self):
        self.buttons = []
        for col in range(self.board.width):
            button = tk.Button(self.root, text=str(col + 1), command=lambda c=col: self.make_move(c))
            button.grid(row=0, column=col)
            self.buttons.append(button)

        self.canvas = tk.Canvas(self.root, width=70*self.board.width, height=70*self.board.height)
        self.canvas.grid(row=1, column=0, columnspan=self.board.width)

        self.draw_board()

    def make_move(self, col):
        player_piece = 'X'

        if self.board.is_valid_move(col):
            self.board.make_move(col, player_piece)
            self.draw_board()

            if self.board.check_win(player_piece):
                self.show_message("Congratulations! You won!")
                self.reset_game()
            else:
                self.root.after(1000, self.computer_move)

    def computer_move(self):
        computer_col = self.computer_player.make_move(self.board)
        computer_piece = 'O'

        if self.board.is_valid_move(computer_col):
            self.board.make_move(computer_col, computer_piece)
            self.draw_board()

            if self.board.check_win(computer_piece):
                self.show_message("Computer won! Better luck next time.")
                self.reset_game()

    def draw_board(self):
        self.canvas.delete("all")

        cell_size = 70
        for row in range(self.board.height):
            for col in range(self.board.width):
                x0, y0 = col * cell_size, row * cell_size
                x1, y1 = x0 + cell_size, y0 + cell_size
                self.canvas.create_rectangle(x0, y0, x1, y1, outline="black", fill="white")

                if self.board.get(row, col) == 'X':
                    self.canvas.create_oval(x0, y0, x1, y1, outline="black", fill="red")
                elif self.board.get(row, col) == 'O':
                    self.canvas.create_oval(x0, y0, x1, y1, outline="black", fill="yellow")

    def show_message(self, message):
        messagebox.showinfo("Game Over", message)

    def reset_game(self):
        self.board = ConnectFourBoard()
        self.computer_player = ComputerPlayer('O')
        self.draw_board()

    def run(self):
        self.root.mainloop()

if __name__ == '__main__':
    connect_four_gui = ConnectFourGUI()
    connect_four_gui.run()
