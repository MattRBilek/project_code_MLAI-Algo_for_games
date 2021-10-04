import pygame as pg
import time
from copy import copy, deepcopy
"""
leave this is not for you
"""
class GameBoard:
    def getMoves(turn, board, flags):
        if ("winX" in flags or "winO" in flags):
            return []
        arr = []
        for i in range(9):
            if board[i] is None:
                arr.append(i)
        return arr
    def makeMove(move, turn, board, flags):
        if not move in GameBoard.getMoves(turn, board,flags):
            return (turn,None,None)
        
        newBoard = deepcopy(board)
        newBoard[move] = "X" if not turn else "O"
        newTurn = not turn
        newFlags = {}
        
        if len(GameBoard.getMoves(newTurn, newBoard,flags)) == 0:
            newFlags["full"] = True
        
        for i in range(3):
            if (not newBoard[3 * i] == None) and newBoard[3 * i + 1] == newBoard[3 * i] and newBoard[3 * i + 2] == newBoard[3 * i]:
               newFlags["win"+newBoard[3*i]] = True
            if (not newBoard[i] == None) and newBoard[i + 3] == newBoard[i] and newBoard[i + 6] == newBoard[i]:
                newFlags["win"+newBoard[i]] = True
                
        if (not newBoard[0] == None) and newBoard[4] == newBoard[0] and newBoard[8] == newBoard[0]:
            newFlags["win"+newBoard[0]] = True

        if (not newBoard[2] == None) and newBoard[4] == newBoard[2] and newBoard[6] == newBoard[2]:
            newFlags["win"+newBoard[2]] = True
        return (newTurn, newBoard, newFlags)
        
class Game:
    def __init__(self, alg1, alg2, fps = 1):
        self.player0 = alg1.Algorithm(GameBoard)
        self.player1 = alg2.Algorithm(GameBoard)
        self.fps = fps
        self.width = 600
        self.height = 600
        
    def game_initiating_window(self):
        if self.fps == 0:
            return;
        self.screen = pg.display.set_mode((self.width, self.height), 0, 32)
        # displaying over the screen
        #self.screen.blit(initiating_window, (0, 0))
        
        # updating the display
        pg.display.update()
        time.sleep(1)         
        white = (255, 255, 255)        
        self.screen.fill(white)
        
        line_color = (0, 0, 0)
        # drawing vertical lines
        pg.draw.line(self.screen, line_color, (self.width / 3, 0), (self.width / 3, self.height), 7)
        pg.draw.line(self.screen, line_color, (self.width / 3 * 2, 0), (self.width / 3 * 2, self.height), 7)
       
        # drawing horizontal lines
        pg.draw.line(self.screen, line_color, (0, self.height / 3), (self.width, self.height / 3), 7)
        pg.draw.line(self.screen, line_color, (0, self.height / 3 * 2), (self.width, self.height / 3 * 2), 7)
        pg.display.update()
    
    def draw(self,board):
        for i in range(9):
            if not (board[i] is None):
                y = int(i/3) * 200
                x = int(i%3) * 200
                pg.draw.rect(self.screen, (200,0,0) if board[i] == "X" else (0,0,200), (x, y, 200, 200))

    def run(self):
        board = [None]*9
        turn = False
        flags = {}
        self.game_initiating_window()
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
            if "winX" in flags or "winO" in flags or "full" in flags:
                running = False
            
            if not self.fps == 0:
                self.draw(board)
                pg.display.update()
                CLOCK.tick(self.fps)
        if not self.fps == 0:
            pg.quit()
        return [0.,1.] if "winO" in flags else [1.,0.] if "winX" in flags else [.5,.5]