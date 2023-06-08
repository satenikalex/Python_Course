import random

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


class Player:
    def __init__(self, name, symbol):
        self.name = name
        self.symbol = symbol

    def make_move(self, board):
        pass


class HumanPlayer(Player):
    def make_move(self, board):
        while True:
            try:
                row = int(input(f"{self.name}, enter the row number (0-2): "))
                col = int(input(f"{self.name}, enter the column number (0-2): "))
                if board.is_valid_move(row, col):
                    break
                else:
                    print("Invalid move! Try again.")
            except ValueError:
                print("Invalid input! Please enter a number.")

        board.place_symbol(row, col, self.symbol)


class ComputerPlayer(Player):
    def make_move(self, board):
        print(f"{self.name} is making a move...")
        # Generate random row and column numbers for the move
        row = random.randint(0, 2)
        col = random.randint(0, 2)

        while not board.is_valid_move(row, col):
            row = random.randint(0, 2)
            col = random.randint(0, 2)

        board.place_symbol(row, col, self.symbol)


class Move:
    def __init__(self, player, row, col):
        self.player = player
        self.row = row
        self.col = col


class Game:
    def __init__(self, player1, player2):
        self.board = Board()
        self.players = [player1, player2]

    def play(self):
        current_player = random.choice(self.players)

        while True:
            self.board.display()
            print()

            current_player.make_move(self.board)

            if self.board.is_winner(current_player.symbol):
                self.board.display()
                print(f"\n{current_player.name} wins!")
                break
            elif self.board.is_full():
                self.board.display()
                print("\nIt's a draw!")
                break

            current_player = self.get_next_player(current_player)

    def get_next_player(self, current_player):
        if current_player == self.players[0]:
            return self.players[1]
        else:
            return self.players[0]


# Example usage
player1 = HumanPlayer("Player 1", "X")
player2 = ComputerPlayer("Computer", "O")

game = Game(player1, player2)
game.play()
