#################################
# game.py        [v0.0.1-alpha] #
#===============================#
#                               #
#-------------------------------#
# J Karstin Neill    05.06.2022 #
#################################


### IMPORTS ###

import pygame
from pygame import Color
from pygame import Surface
from pygame import Vector2
from pygame.sprite import Group
from pygame.time import Clock

from sprite import Block, Ghost
from meta import PIXEL_SIZE


### CLASS DEFINITIONS ###

class Game:

    running: bool = None



    size = width, height = 160 * PIXEL_SIZE, 90 * PIXEL_SIZE

    bkg_color = Color('black')

    clock = Clock()
    screen = pygame.display.set_mode(size)
    screen.fill(bkg_color)
    all_sprites = Group()

    background: Surface = Surface(size)
    background.fill(bkg_color)

    block = Block(size=(PIXEL_SIZE, PIXEL_SIZE), groups=[all_sprites])

    ghost = Ghost('ghost.ss.gif')
    all_sprites.add(ghost)
    move_vect: Vector2 = Vector2(3.2, 1.8)



    def __init__(self):
        pygame.init()

        self.running = False


    def run(self):
        
        self.running = True
        
        while self.running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.running = False
            
            if self.running:
                


                self.ghost.move(self.move_vect)

                dt: float = self.clock.tick() / 1000.
                self.all_sprites.update(dt)

                self.all_sprites.clear(self.screen, self.background)
                self.all_sprites.draw(self.screen)

                pygame.display.flip()



        pygame.quit()
