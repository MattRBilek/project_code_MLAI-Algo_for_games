import random
class Algorithm:
    def __init__(self, game):
        self.game = game
    def makeMove(self, turn, board, flags):
        return random.choice(self.game.getMoves(turn, board, flags))