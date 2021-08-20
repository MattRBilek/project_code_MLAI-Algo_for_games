# project_code_MLAI-Algo_for_games
this project is being created to provide starter code for participants if they want it as well as the games that the algorithms will be written for.

NOTES (MUST READ):
	-Nothing in here is meant for commercial use.

	-Do not pull code from I have provided to be used in school or commercial projects failure 
	 to follow this rule can get you kick out of the school. if it is in your own personal learning environment then go for it.
	 
	-Do not use code written in the club by you or your group without consulting your professor/TA 
	 as this is self-plagiarism and can get you kicked out of the school.

Allowed/required libaries:
	numpy, sktlearn, pytorch, random

DOCS:
	FOR MEMBER --- must make | see randomAlg for example:
		file with class called Algorithm
		Algorithm must have a contructor that takes a single argument save the argument as game (this saves a libary)
		
		DO NOT MODIFY ANY OF THE PERAMITERS IT WILL NOT WORK
		Algorithm must have a function called makeMove(self,turn,board,flags)
		
	guaranteed function calls:

		board.getMoves() - returns a list of possible moves
		board.makeMove(move, turn = None, flags = None) - returns a new board with flags and turn

	premade algorithms:

		@ see https://en.wikipedia.org/wiki/Minimax
		miniMax(board, depth, turn = None, flags = None)
		- requirements
			evaluate(board, turn, flags)

		@ runs miniMax with depth of one see above (finds best move given current state)
		bestMove(board, turn = None, flags = None)
		- requirements
			evaluate(board) 


NOTES FOR MATT about what games and how hard they are:

games:

easy:
tic Tac Toe
pong

med:
snake like game 2p
image classification

hard:
pac man like game
space invaders

extermeme:

spy party


