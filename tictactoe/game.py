import random
from board  import Board
from player import Player
from human  import HumanPlayer
from comp   import ComputerPlayer
from move   import Move

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