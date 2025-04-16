import tkinter as tk
from tkinter import messagebox
from game import Game
from utils import generate_computer_name

class TicTacToeGUI:
    def __init__(self, root):
        self.root = root
        self.root.title("Tic Tac Toe")
        self.game = Game()
        self.buttons = []
        self.difficulty = 'easy'
        self.play_with_computer = False
        self.computer_name = generate_computer_name()
        self.create_widgets()

    def create_widgets(self):
        for i in range(9):
            button = tk.Button(self.root, text=' ', font=('normal', 40), width=5, height=2,
                               bg='lightgreen', command=lambda i=i: self.on_button_click(i))
            button.grid(row=i//3, column=i%3)
            self.buttons.append(button)
        self.reset_button = tk.Button(self.root, text='Reset', command=self.reset_game, bg='green', fg='white')
        self.reset_button.grid(row=3, column=0, columnspan=3, sticky='nsew')

        self.computer_button = tk.Button(self.root, text='Play with Computer', command=self.toggle_computer_mode, bg='green', fg='white')
        self.computer_button.grid(row=4, column=0, columnspan=3, sticky='nsew')

        self.difficulty_label = tk.Label(self.root, text='Difficulty:', bg='green', fg='white')
        self.difficulty_label.grid(row=5, column=0, sticky='nsew')

        self.difficulty_var = tk.StringVar(value='easy')
        self.difficulty_menu = tk.OptionMenu(self.root, self.difficulty_var, 'easy', 'medium', 'hard', command=self.set_difficulty)
        self.difficulty_menu.grid(row=5, column=1, columnspan=2, sticky='nsew')

    def on_button_click(self, position):
        if self.game.board[position] == ' ' and self.game.winner is None:
            self.game.make_move(position)
            self.update_buttons()
            if self.game.winner:
                messagebox.showinfo("Game Over", f"Player {self.game.winner} wins!")
            elif ' ' not in self.game.board:
                messagebox.showinfo("Game Over", "It's a tie!")
            elif self.play_with_computer and self.game.current_player == 'O':
                self.game.make_computer_move(self.difficulty)
                self.update_buttons()
                if self.game.winner:
                    messagebox.showinfo("Game Over", f"Player {self.game.winner} wins!")
                elif ' ' not in self.game.board:
                    messagebox.showinfo("Game Over", "It's a tie!")

    def update_buttons(self):
        for i in range(9):
            self.buttons[i].config(text=self.game.board[i])

    def reset_game(self):
        self.game.reset_game()
        self.update_buttons()

    def toggle_computer_mode(self):
        self.play_with_computer = not self.play_with_computer
        mode = "ON" if self.play_with_computer else "OFF"
        self.computer_button.config(text=f'Play with Computer: {mode}')
        if self.play_with_computer:
            self.computer_name = generate_computer_name()

    def set_difficulty(self, difficulty):
        self.difficulty = difficulty

if __name__ == "__main__":
    root = tk.Tk()
    gui = TicTacToeGUI(root)
    root.mainloop()