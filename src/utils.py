import random

def generate_computer_name():
    names = ["AI Bot", "Computer", "Robo", "AI Master", "TicTacToe AI"]
    return random.choice(names)

def reset_board():
    return [[" " for _ in range(3)] for _ in range(3)]

def is_board_full(board):
    return all(cell != " " for row in board for cell in row)

def check_valid_move(board, row, col):
    return board[row][col] == " "