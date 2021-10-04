import pygame as pg
import time
import random
import numpy as np
from copy import copy, deepcopy
"""
leave this is not for you
"""
class GameBoard:
    def getMoves(turn, board, flags):
        return [0,1]
    def makeMove(move, turn, board, flags):
        newTurn = not turn
        newFlags = flags
        newboard = [None, None]
        if "player1" in flags and not flags["player1"] is None:
            move1 = flags["player1"]
            move2 = move
            score1 = 0
            score2 = 0

            if move1 == move2:
                score1 = 1 if move1 == 0 else 0
                score2 = score1
            else:
                score1 = (2 if move1 > move2 else 0)
                score2 = (2 if move1 < move2 else 0)
            newboard = [score1, score2]

            flags["player1"] = None
        else:
            newFlags["player1"] = move
        return (newTurn, newboard, newFlags)
        
class Game:
    def __init__(self, alg1, alg2, fps = 1):
        self.player0 = alg1.Algorithm(GameBoard)
        self.player1 = alg2.Algorithm(GameBoard)
        

    def run(self):
        board = [None, None]
        x = []
        turn = False
        flags = {}
        running = True
        numRounds = random.randint(1,2) * 100
        score = np.array([0,0])
        for i in range(numRounds):
            move = None
            if turn:
                move = self.player1.makeMove(turn, deepcopy(board), deepcopy(flags))
                turn, board, flags = GameBoard.makeMove(move,turn, board, flags)

                
                score += np.array(board)
            else:
                move = self.player0.makeMove(turn, deepcopy(board), deepcopy(flags))
                turn, x, flags = GameBoard.makeMove(move,turn, board, flags)
                
        return score