import os,sys,argparse

if __name__ == "__main__":
    parser = argparse.ArgumentParser(
        description     = 'mlai_algo', 
        formatter_class = argparse.ArgumentDefaultsHelpFormatter)

    parser.add_argument('--player0', default = 'minimax',
                       type=str,
                       help='the first algorithm to run')
    parser.add_argument('--player1', default = 'minimax',
                       type=str,
                       help='the second algorithm to run')
    parser.add_argument('--game', default = 'tictactoe',
                        type=str,
                        help = 'the game that we are playing')
    args   = parser.parse_args()
    
    engine = __import__(args.game)
    game = engine.Game(__import__(args.player0),__import__(args.player1) if args.player0 != "None" else None)
    game.run()
