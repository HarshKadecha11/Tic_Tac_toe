import random

class Game:
    def __init__(self):
        self.board = [' ' for _ in range(9)]  # A list to hold the board state
        self.current_player = 'X'  # Starting player
        self.winner = None

    def start_game(self):
        self.board = [' ' for _ in range(9)]
        self.current_player = 'X'
        self.winner = None

    def make_move(self, position):
        if self.board[position] == ' ' and self.winner is None:
            self.board[position] = self.current_player
            if self.check_winner():
                self.winner = self.current_player
            else:
                self.current_player = 'O' if self.current_player == 'X' else 'X'

    def check_winner(self):
        winning_combinations = [
            (0, 1, 2), (3, 4, 5), (6, 7, 8),  # Horizontal
            (0, 3, 6), (1, 4, 7), (2, 5, 8),  # Vertical
            (0, 4, 8), (2, 4, 6)               # Diagonal
        ]
        for combo in winning_combinations:
            if self.board[combo[0]] == self.board[combo[1]] == self.board[combo[2]] != ' ':
                return True
        return False

    def reset_game(self):
        self.start_game()

    def get_empty_positions(self):
        return [i for i, spot in enumerate(self.board) if spot == ' ']

    def make_computer_move(self, difficulty):
        if difficulty == 'easy':
            self.make_random_move()
        elif difficulty == 'medium':
            self.make_medium_move()
        elif difficulty == 'hard':
            self.make_hard_move()

    def make_random_move(self):
        empty_positions = self.get_empty_positions()
        if empty_positions:
            position = random.choice(empty_positions)
            self.make_move(position)

    def make_medium_move(self):
        # Implement a medium difficulty move strategy
        self.make_random_move()

    def make_hard_move(self):
        best_score = float('-inf')
        best_move = None
        for position in self.get_empty_positions():
            self.board[position] = 'O'
            score = self.minimax(self.board, 0, False)
            self.board[position] = ' '
            if score > best_score:
                best_score = score
                best_move = position
        if best_move is not None:
            self.make_move(best_move)

    def minimax(self, board, depth, is_maximizing):
        if self.check_winner():
            return 1 if self.current_player == 'O' else -1
        elif ' ' not in board:
            return 0

        if is_maximizing:
            best_score = float('-inf')
            for position in self.get_empty_positions():
                board[position] = 'O'
                score = self.minimax(board, depth + 1, False)
                board[position] = ' '
                best_score = max(score, best_score)
            return best_score
        else:
            best_score = float('inf')
            for position in self.get_empty_positions():
                board[position] = 'X'
                score = self.minimax(board, depth + 1, True)
                board[position] = ' '
                best_score = min(score, best_score)
            return best_score