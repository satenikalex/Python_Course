import random
from player import Player
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