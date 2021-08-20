def minimax(side, board, flags, depth):
    moves = [ move for move in generateMoves(side, board, flags) ]
    if len(moves) > 0:
        turnMult = 1 if side == 0 else -1
        value = None
        moveTree = {}
        moveList = None
        for move in moves:
            newside, newboard, newflags = makeMove(side, board, move[0], move[1], flags, move[2])
            temp = None
            tempMoveList = None

            if depth <= 1:
                temp = evaluate(newboard)
                tempMoveList = []
            else:
                temp,tempMoveList, = minimax(newside, newboard, newflags, depth - 1)

            if value == None or value * turnMult < temp * turnMult:
                moveList = [move] + tempMoveList
                value = temp

        return (value, moveList)
    else:
        return (evaluate(board), [])

