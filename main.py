import os,sys,argparse
import games.tictactoe
if __name__ == "__main__":
    parser = argparse.ArgumentParser(
        description     = 'mlai_algo', 
        formatter_class = argparse.ArgumentDefaultsHelpFormatter)

    parser.add_argument('--player0', default = 'premade_algo.minimax',
                       type=str,
                       help='the first algorithm to run')
    parser.add_argument('--player1', default = 'premade_algo.minimax',
                       type=str,
                       help='the second algorithm to run')
    parser.add_argument('--game', default = 'tictactoe',
                        type=str,
                        help = 'the game that we are playing')
    parser.add_argument('--fps', default = None,
                        type=int,
                        help = 'the game that we are playing (leave as None for best experiance)')                    
    args   = parser.parse_args()
    engine = __import__("games."+args.game, fromlist=[''])
    game = None
    if args.fps is None:
        game = engine.Game(__import__(args.player0, fromlist=['']) if args.player0 != "None" else None,__import__(args.player1, fromlist=['']) if args.player1 != "None" else None)
    else:
        game = engine.Game(__import__(args.player0, fromlist=['']) if args.player0 != "None" else None,__import__(args.player1, fromlist=['']) if args.player1 != "None" else None, args.fps)
    result = game.run()
    print(result)