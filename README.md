# project_code_MLAI-Algo_for_games
this project is being created to provide starter code for participants if they want it as well as the games that the algorithms will be written for.

NOTES (MUST READ):
	-Nothing in here is meant for commercial use.

	-Do not use code I have provided to be used in school or commercial projects failure 
	 to follow this rule can get you kicked out of the school. if it is in your own personal learning environment then go for it.
	 
	-Do not use code written in the club by you or your group without consulting your professor/TA 
	 as this is self-plagiarism and can get you kicked out of the school (they will most likely let you use it ask first).



required downloads:
	python 3.9 (for windows custom install make sure add path and pip installed)

Allowed/required libraries:
	numpy (pip install numpy), 
	sklearn (pip install -U scikit-learn), 
	pytorch (pip3 install torch torchvision torchaudio), 
	random (no install), 
	pygame (pip install pygame)

DOCS:
				
	guaranteed game function calls:
		game.getMoves(self, turn, board, flags) - returns a list of possible moves
		game.makeMove(self, move, turn, board, flags) - returns a new board with flags and turn
	
	required for your algorithms:
		- class is called algorithm
		- __init__(self, game)
			@perams game a game as above
			sets up an algorithm
		makeMove(self, turn, board, flags)
			@returns x
				should return a move that is in the list game.getMoves()
	
	premade algorithms base:

		@ see https://en.wikipedia.org/wiki/Minimax
		miniMax(side, board, flags, game, evaluate = ez, maxDepth = None, depth=1)
			@peram evaluate a function exampleEval(side, board, flags, depth = None) 
			
			@returns (value, moveList, moveTree)
				- value - score of best moveList
				- moveList - order of moves for the optimally played outcome (acording to evaluate)
				- moveTree - dict of moves explored with values of scores


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


