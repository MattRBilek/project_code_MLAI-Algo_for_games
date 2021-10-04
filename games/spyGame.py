import pygame as pg
import time
import random
from copy import copy, deepcopy

__types = 4
__width = 600
__height = 600
__tileSize = __width/10
"""
just some logic for the game class seperated from game class in order to ensure people only use code i want them to have
turn = true implies shooter | false implies mover
"""
class GameBoard:
    def getMoves(turn, board, flags = None):
        if turn:
            return [i for i in range(11)] # 0 shoots 0 1 shoots 1 ... 10 means wait
        else:
            
    def makeMove(move, turn, board, flags = None):
        if turn:
            if move
class Mover:
    def __init__(self, moveType):
        self.goals = [0,0,0,0]
        self.moveType =  random.randint(1, __types - 1) if moveType is None else moveType: # zero reseved for human / player made ai
    def draw(self, x,y):
class Game:
    def __init__(self, alg1, alg2, fps = 1):
        self.player0 = alg1.Algorithm(GameBoard)
        self.player1 = alg2.Algorithm(GameBoard)
        self.fps = fps
        self.width = __width
        self.height = __height
        
    def game_initiating_window(self):
        self.screen = pg.display.set_mode((self.width, self.height), 0, 32)
        # displaying over the screen
        #self.screen.blit(initiating_window, (0, 0))
        
        # updating the display
        pg.display.update()         
        white = (255, 255, 255)        
        self.screen.fill(white)
        pg.display.update()
        time.sleep(3)
    
    def draw(self,board):
        pg.display.update()

    def run(self):
        board = [None]*100
        turn = False
        flags = {}
        self.game_initiating_window()
        running = True
        CLOCK = pg.time.Clock()
        while(running):
            for event in pg.event.get():
                if event.type == pg.QUIT:
                    pg.quit()
                    return
            move = None
            if turn:
                move = self.player1.makeMove(turn, deepcopy(board), flags)
            else:
                move = self.player0.makeMove(turn, deepcopy(board), flags)
            if not move is None:
                turn, board, flags = GameBoard.makeMove(move,turn, board, flags)
            if "over" in flags:
                running = False
            
            self.draw(board)
            CLOCK.tick(self.fps)
        pg.quit()
        return