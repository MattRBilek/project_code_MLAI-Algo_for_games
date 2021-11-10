import sys
import math
import pygame
import pygame as pg
import time
import random
import numpy as np
from copy import copy, deepcopy

BLUE = (0,0,255)
BLACK = (0,0,0)
RED = (255,0,0)
YELLOW = (255,255,0)

ROW_COUNT = 6
COLUMN_COUNT = 7
SQUARESIZE = 100
RADIUS = int(SQUARESIZE/2 - 5)
width = COLUMN_COUNT * SQUARESIZE
height = (ROW_COUNT+1) * SQUARESIZE

size = (width, height)
"""
leave this is not for you
"""
class GameBoard:
    def getMoves(turn, board, flags):
        moveArr = []
        for i in range(COLUMN_COUNT):
            if board[ROW_COUNT-1][i] == 0:
                moveArr.append(i);
        ##print(moveArr)
        return moveArr
    def makeMove(move, turn, board, flags):
        newTurn = not turn
        newFlags = deepcopy(flags)
        newboard = deepcopy(board)
        moved = False;
        ##print(move)
        for i in range(ROW_COUNT):
            if newboard[i][move] == 0 and not moved:
                newboard[i][move] = 1 if not turn else 2
                moved = True
        if GameBoard.winning_move(newboard,1 if not turn else 2):
            newFlags["win"+str(1 if not turn else 2)]= "sure";
        if len(GameBoard.getMoves(newTurn,newboard,newFlags)) == 0:
            newFlags["full"] = "it sure is"
        return (newTurn, newboard, newFlags)
        
        
    def winning_move(board, piece):
        # Check horizontal locations for win
        for c in range(COLUMN_COUNT-3):
            for r in range(ROW_COUNT):
                if board[r][c] == piece and board[r][c+1] == piece and board[r][c+2] == piece and board[r][c+3] == piece:
                    return True

        # Check vertical locations for win
        for c in range(COLUMN_COUNT):
            for r in range(ROW_COUNT-3):
                if board[r][c] == piece and board[r+1][c] == piece and board[r+2][c] == piece and board[r+3][c] == piece:
                    return True

        # Check positively sloped diaganols
        for c in range(COLUMN_COUNT-3):
            for r in range(ROW_COUNT-3):
                if board[r][c] == piece and board[r+1][c+1] == piece and board[r+2][c+2] == piece and board[r+3][c+3] == piece:
                    return True

        # Check negatively sloped diaganols
        for c in range(COLUMN_COUNT-3):
            for r in range(3, ROW_COUNT):
                if board[r][c] == piece and board[r-1][c+1] == piece and board[r-2][c+2] == piece and board[r-3][c+3] == piece:
                    return True
        
class Game:
    def __init__(self, alg1, alg2, fps = 1):
        self.player0 = alg1.Algorithm(GameBoard)
        self.player1 = alg2.Algorithm(GameBoard)
        self.fps = fps
    def game_initiating_window(self):
        if self.fps == 0:
            return;
        pygame.init()

        self.screen = pygame.display.set_mode(size)

        myfont = pygame.font.SysFont("monospace", 75)

        
        
    
    def draw(self,board):
        for c in range(COLUMN_COUNT):
            for r in range(ROW_COUNT):
                pygame.draw.rect(self.screen, BLUE, (c*SQUARESIZE, r*SQUARESIZE+SQUARESIZE, SQUARESIZE, SQUARESIZE))
                pygame.draw.circle(self.screen, BLACK, (int(c*SQUARESIZE+SQUARESIZE/2), int(r*SQUARESIZE+SQUARESIZE+SQUARESIZE/2)), RADIUS)
        
        for c in range(COLUMN_COUNT):
            for r in range(ROW_COUNT):		
                if board[r][c] == 1:
                    pygame.draw.circle(self.screen, RED, (int(c*SQUARESIZE+SQUARESIZE/2), height-int(r*SQUARESIZE+SQUARESIZE/2)), RADIUS)
                elif board[r][c] == 2: 
                    pygame.draw.circle(self.screen, YELLOW, (int(c*SQUARESIZE+SQUARESIZE/2), height-int(r*SQUARESIZE+SQUARESIZE/2)), RADIUS)
        pygame.display.update()

    def run(self):
        board = np.zeros((ROW_COUNT,COLUMN_COUNT))
        turn = False
        flags = {}
        if self.fps:
            self.game_initiating_window()
            self.draw(board)
            pygame.display.update()
        running = True
        if not self.fps == 0:
            CLOCK = pg.time.Clock()
        while(running):
            if not self.fps == 0:
                for event in pg.event.get():
                    if event.type == pg.QUIT:
                        pg.quit()
                        return
            move = None
            if turn:
                move = self.player1.makeMove(turn, deepcopy(board), deepcopy(flags))
            else:
                move = self.player0.makeMove(turn, deepcopy(board), deepcopy(flags))
            
            turn, board, flags = GameBoard.makeMove(move,turn, board, flags)
            if "win1" in flags or "win2" in flags or "full" in flags:
                running = False
            print(board)
            if not self.fps == 0:
                self.draw(board)
                pg.display.update()
                CLOCK.tick(self.fps)
        if not self.fps == 0:
            pg.quit()
        return [0.,1.] if "win2" in flags else [1.,0.] if "win1" in flags else [.5,.5]