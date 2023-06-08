class Board:
    def __init__(self):
        self.board = [[' ' for _ in range(3)] for _ in range(3)]

    def display(self):
        for row in self.board:
            print('|'.join(row))
            print('-' * 5)

    def is_valid_move(self, row, col):
        if row < 0 or row >= 3 or col < 0 or col >= 3:
            return False
        if self.board[row][col] == ' ':
            return True
        return False

    def place_symbol(self, row, col, symbol):
        self.board[row][col] = symbol

    def is_winner(self, symbol):
        # Check rows
        for row in self.board:
            if row.count(symbol) == 3:
                return True

        # Check columns
        for col in range(3):
            if self.board[0][col] == symbol and self.board[1][col] == symbol and self.board[2][col] == symbol:
                return True

        # Check diagonals
        if self.board[0][0] == symbol and self.board[1][1] == symbol and self.board[2][2] == symbol:
            return True
        if self.board[0][2] == symbol and self.board[1][1] == symbol and self.board[2][0] == symbol:
            return True

        return False

    def is_full(self):
        for row in self.board:
            if ' ' in row:
                return False
        return True

    def reset(self):
        self.board = [[' ' for _ in range(3)] for _ in range(3)]