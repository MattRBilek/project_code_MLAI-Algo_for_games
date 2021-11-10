import sys
import math
import pygame
import pygame as pg
import time
import random
import numpy as np
from copy import copy, deepcopy

BLUE = (0,0,255)
GREEN = (0,255,0)
BLACK = (0,0,0)
RED = (255,0,0)
YELLOW = (255,255,0)

ROW_COUNT = 6
COLUMN_COUNT = 6
SQUARESIZE = 100
width = COLUMN_COUNT * SQUARESIZE
height = (ROW_COUNT) * SQUARESIZE

size = (width, height)
APPLE = 3
HEAD = 2
TAIL = 1
EMPTY = 0
UP = 0
DOWN = 1
LEFT = 2
RIGHT = 3

def printboard(board):
    for i in range(ROW_COUNT):
        st = ""
        for j in range(COLUMN_COUNT):
            st += str(board[i][j].t) + ", "
        print(st)
def slowDown():
    time.sleep(0)
class Tile:
    def __init__(self,t,x,y,n,p=None):
        self.t = t;
        self.x = x;
        self.y = y;
        self.n = n;
        self.p = p;
    def cords(self):
        return (self.x*SQUARESIZE,self.y*SQUARESIZE,SQUARESIZE,SQUARESIZE);
    def color(self):
        return (RED if self.t==3 else BLUE if self.t==2 else YELLOW if self.t==1 else GREEN)
"""
leave this is not for you
"""
class GameBoard:
    def getMoves(turn, board, flags):
        return [UP,DOWN,LEFT,RIGHT];
    def makeMove(move, turn, board, flags):
        newTurn = not turn
        newFlags = deepcopy(flags)
        newboard = []
        h = None
        for i in range(ROW_COUNT):
            for j in range(COLUMN_COUNT):  
                if (board[i][j].t == HEAD):
                    h = board[i][j]
        for i in range(ROW_COUNT):
            temp = []
            for j in range(COLUMN_COUNT):
                temp.append(Tile(EMPTY,j,i,None))
            newboard.append(temp)
        
        for i in range(ROW_COUNT):
            for j in range(COLUMN_COUNT):   
                if ((board[i][j].p is None) and (board[i][j].t == HEAD or board[i][j].t == TAIL)):
                    temp = board[i][j]
                    tail = temp
                    oldx = temp.x
                    oldy = temp.y
                    
                    while (not (temp.n is None)):
                    
                        newTemp = temp.n;
                        temp.x = newTemp.x
                        temp.y = newTemp.y
                        newboard[newTemp.y][newTemp.x] = temp
                        temp = newTemp
                    
                    
                    x = temp.x + (1 if move == LEFT else -1 if move == RIGHT else 0)
                    y = temp.y + (1 if move == DOWN else -1 if move == UP else 0)
                    
                    if (x < 0 or y < 0 or x >= COLUMN_COUNT or y >= ROW_COUNT):
                        newFlags["over"] = "gamopfa"

                    elif (board[y][x].t == APPLE):
                        newFlags["point"] = 1;
                        newFlags["apple"] = True;
                        newboard[oldy][oldx] = Tile(TAIL,oldx,oldy,tail,None);
                        tail.p = newboard[oldy][oldx]
                        
                    if (not ("over" in newFlags) and board[y][x].t == TAIL):
                        newFlags["over"] = "naofwlmk"
                    
                    if (not ("over" in newFlags)):    
                        newboard[y][x] = temp
                        temp.x = x;
                        temp.y = y;
                    
                elif ((board[i][j].t == APPLE)):
                    if (newboard[i][j].t == EMPTY):
                        newboard[i][j] = board[i][j]
        spots = []
        for i in range(ROW_COUNT):
            for j in range(COLUMN_COUNT):
                if (newboard[i][j].t == EMPTY):
                    spots.append((j,i))
        if (newFlags["apple"] == True):
            if spots:
                newFlags["apple"] = False
                spot = random.choice(spots)
                x,y = spot;
                newboard[y][x] = Tile(APPLE,x,y,None)
            else:
                newFlags["over"] = True;
                
        return (newTurn, newboard, newFlags)
        
        
class Game:
    def __init__(self, alg1, alg2, fps = 1):
        self.player0 = alg1.Algorithm(GameBoard)
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
                pygame.draw.rect(self.screen, board[r][c].color(), board[r][c].cords())

        pygame.display.update()

    def run(self):
        board = []
        
        for i in range(ROW_COUNT):
            temp = []
            for j in range(COLUMN_COUNT):
                temp.append(Tile(EMPTY,j,i,None))
            board.append(temp)
        board[0][0] = Tile(HEAD,0,0,None)
        
        turn = False
        flags = {}
        flags["apple"] = False
        board[0][2] = Tile(APPLE,2,0,None)
        score = 0
        
        if self.fps:
            self.game_initiating_window()
            self.draw(board)
            pygame.display.update()
            time.sleep(1)
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
            
            slowDown();
            move = self.player0.makeMove(turn, deepcopy(board), deepcopy(flags))
            
            turn, board, flags = GameBoard.makeMove(move,turn, board, flags)
            
            if "over" in flags:
                running = False
            if "point" in flags and flags["point"]==1:
                score += 1
                flags["point"]=0
            
            if not self.fps == 0 and running:
                self.draw(board)
                pg.display.update()
                CLOCK.tick(self.fps)
        
        if not self.fps == 0:
            pg.quit()
        return score