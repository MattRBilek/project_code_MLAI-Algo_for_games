


def evaluate(side,board,flags):
    if "winX" in flags:
        return 1
    if "winO" in flags:
        return -1
    return 0


class Algorithm:
    def __init__(self, game):
        self.game = game
    def makeMove(self, turn, board, flags):
        turn, moves = self.minimax(turn,board,flags,10)
        return moves[0]
    
    def minimax(self,side, board, flags, depth):
        moves = [ move for move in self.game.getMoves(side, board, flags) ]
        if len(moves) > 0:
            turnMult = 1 if side == 0 else -1
            value = None
            moveList = None
            for move in moves:
                newside, newboard, newflags = self.game.makeMove(move, side, board, flags)
                temp = None
                tempMoveList = None

                if depth <= 1:
                    temp = evaluate(side,board,flags)
                    tempMoveList = []
                else:
                    temp,tempMoveList, = self.minimax(newside, newboard, newflags, depth - 1)

                if value == None or value * turnMult < temp * turnMult:
                    moveList = [move] + tempMoveList
                    value = temp
            return (value, moveList)
        else:
            return (evaluate(side,board,flags), [])