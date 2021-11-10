import random
import premade_algo.minimaxHelper as alg
ROW_COUNT = 6
COLUMN_COUNT = 7

def evaluate(side,board,flags):
    if "win1" in flags:
        return 1.0
    if "win2" in flags:
        return -1.0
    maxCount1 = 1;
    maxCount2 = 1;
    for c in range(COLUMN_COUNT):
            for r in range(ROW_COUNT):
                j = 1
                tempcount = 1
                while j < 4 and j+c < COLUMN_COUNT and board[r][c] == board[r][c+j]:
                    tempcount += 1
                    j+=1
                
                if board[r][c] == 1.:
                    maxCount1 = max(maxCount1,tempcount)
                elif board[r][c] == 2.:
                    maxCount2 = max(maxCount2,tempcount)
    max(maxCount2,tempcount)          
    return (maxCount1-maxCount2)/4
                
class Algorithm:
    def __init__(self, game):
        self.game = game
        
    def makeMove(self, turn, board, flags):
        print()
        value, moves, moveTree = alg.minimaxAlgo(turn,board,flags,self.game, evaluate, 2) # for 5 u will be 2
        print()
        print(moves[0])
        print()
        return moves[0]