#################################
# main.py
#-------------------------------
# J Karstin Neill    04.28.2022
#################################


### IMPORTS ###

import pygame
import sys


### CONSTANTS ###

EXIT_SUCCESS = 0


### MAIN FUNCTION DEFINITION ###

def main(argv: list[str], argc: int) -> int:
    size = width, height = 320, 240
    speed = [2, 2]
    black = 0, 0, 0

    screen = pygame.display.set_mode(size)

    ball = pygame.image.load("resources/intro_ball.gif")
    ballrect = ball.get_rect()

    while 1:
        for event in pygame.event.get():
            if event.type == pygame.QUIT: return EXIT_SUCCESS
        
        ballrect = ballrect.move(speed)
        if ballrect.left < 0 or ballrect.right > width:
            speed[0] = -speed[0]
        if ballrect.top < 0 or ballrect.bottom > height:
            speed[1] = -speed[1]
        
        screen.fill(black)
        screen.blit(ball, ballrect)
        pygame.display.flip()


### CORE FUNCTIONS ###




### UTILITY FUNCTIONS ###




### MAIN FUNCTION EXECUTION ###

if __name__ == '__main__':
    pygame.init()
    argv: list[str] = sys.argv
    argc: int = len(argv)
    sys.exit(main(argv, argc))
