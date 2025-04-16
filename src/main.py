# main.py

import tkinter as tk
from gui import TicTacToeGUI

def main():
    # Set up the GUI
    root = tk.Tk()
    root.title("Tic Tac Toe")
    game_gui = TicTacToeGUI(root)
    
    # Start the GUI loop
    root.mainloop()

if __name__ == "__main__":
    main()