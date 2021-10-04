#example class for tictac toe for infinite depth
import premade_algo.minimaxHelper as alg



def evaluate(side,board,flags):
    if "winX" in flags:
        return 1.0
    if "winO" in flags:
        return -1.0
    return 0.0


class Algorithm:
    def __init__(self, game):
        self.game = game
    def makeMove(self, turn, board, flags):
        value, moves, moveTree = alg.minimaxAlgo(turn,board,flags,self.game, evaluate, 2) # for u none will be 3
        return moves[0]