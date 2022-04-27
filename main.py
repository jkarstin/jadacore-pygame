#################################
# main.py
#-------------------------------
# J Karstin Neill    04.27.2022
#################################


### IMPORTS ###

import pygame
import sys


### CONSTANTS ###

EXIT_SUCCESS = 0


### MAIN FUNCTION DEFINITION ###

def main(argv: list[str], argc: int) -> int:
    print('Hello world!')
    
    if argc > 1:
        print(argv)

    return EXIT_SUCCESS


### CORE FUNCTIONS ###




### UTILITY FUNCTIONS ###




### MAIN FUNCTION EXECUTION ###

if __name__ == '__main__':
    pygame.init()
    argv: list[str] = sys.argv
    argc: int = len(argv)
    sys.exit(main(argv, argc))
