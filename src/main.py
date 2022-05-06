#################################
# main.py        [v0.0.1-alpha] #
#===============================#
#                               #
#-------------------------------#
# J Karstin Neill    05.06.2022 #
#################################


### IMPORTS ###

import pdb
import sys

from game import Game
from util import Stylist


### CONSTANTS & FLAGS ###

EXIT_SUCCESS  = 0
ERROR_GENERIC = 1

LOG_STYLE_ERROR = Stylist.style('red', 'underline')


### MAIN FUNCTION DEFINITION ###

def main(argv: list[str], argc: int) -> int:
    processArgv(argv, argc)

    game: Game = Game()
    game.run()

    return EXIT_SUCCESS


### OPERATIONAL FUNCTIONS ###


### UTILITY FUNCTIONS ###

def processArgv(argv: list[str], argc: int) -> str:
    return None


def error(msg: str, err_code: int=ERROR_GENERIC) -> None:
    sprint(f"[ERROR]: {msg}", LOG_STYLE_ERROR)
    sys.exit(err_code)


def sprint(value: any, styletags: str='', **kwargs) -> None:
    print(f"{styletags}{value}{Stylist.style('reset')}", **kwargs)


### MAIN FUNCTION EXECUTION ###

if __name__ == '__main__':
    argv: list[str] = sys.argv
    argc: int = len(argv)
    sys.exit(main(argv, argc))
