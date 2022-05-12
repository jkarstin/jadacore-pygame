#################################
# main.py        [v0.0.1-alpha] #
#===============================#
#                               #
#-------------------------------#
# J Karstin Neill    05.10.2022 #
#################################


### IMPORTS ###

import sys

from jadacore.game import Game
from jadacore.meta import EXIT_SUCCESS

from start_world import StartWorld


### MAIN FUNCTION DEFINITION ###

def main(argv: list[str], argc: int) -> int:
    processArgv(argv, argc)

    game: Game = Game()
    game.set_world(StartWorld())
    game.run()

    return EXIT_SUCCESS


### UTILITY FUNCTIONS ###

def processArgv(argv: list[str], argc: int) -> str:
    if argc > 1:
        print(argv)
    return None


### MAIN FUNCTION EXECUTION ###

if __name__ == '__main__':
    argv: list[str] = sys.argv
    argc: int = len(argv)
    sys.exit(main(argv, argc))
