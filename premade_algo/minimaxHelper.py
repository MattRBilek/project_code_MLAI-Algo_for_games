# this functon returns a number in the range [-1,1] where -1 means that side=1 is winnning 1 means side=0 is winning and 0 means tied
def exampleEval(side, board, flags, depth = None):
    return 1.0;

def minimaxAlgo(side, board, flags, game, evaluate = exampleEval, maxDepth = None, depth=0, alpha = -2.0, beta = 2.0):
    moves = [ move for move in game.getMoves(side, board, flags) ]
    if len(moves) > 0 and ((not maxDepth) or maxDepth >= depth):
        turnMult = 1 if side == 0 else -1
        value = None
        moveTree = {}
        moveList = None
        for move in moves:
            newside, newboard, newflags = game.makeMove(move, side, board, flags)
            temp = None
            tempMoveList = None

            temp,tempMoveList,tempFlags = minimaxAlgo(newside, newboard, newflags, game, evaluate, maxDepth, depth - 1, alpha, beta)

            if value == None or value * turnMult < temp * turnMult:
                moveList = [move] + tempMoveList
                value = temp
            if (side):
                beta = min(beta, value)
            else:
                alpha = max(alpha,value)
                
            if (beta <= alpha):
                    pass#return (value, moveList, moveTree)
        return (value, moveList, moveTree)
    else:
        return (float(evaluate(side,board,flags)), [], {})

