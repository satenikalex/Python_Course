from player import Player

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