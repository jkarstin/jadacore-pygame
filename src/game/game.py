#################################
# game.py        [v0.0.1-alpha] #
#===============================#
#                               #
#-------------------------------#
# J Karstin Neill    05.06.2022 #
#################################


### IMPORTS ###

import pygame
from pygame import Color, Surface, Vector2
from pygame.sprite import Group
from pygame.time import Clock

from sprite import Block, Ghost
from meta import PIXEL_SIZE


### CONSTANTS & FLAGS ###

SIZE = WIDTH, HEIGHT = 160 * PIXEL_SIZE, 90 * PIXEL_SIZE


### CLASS DEFINITIONS ###

class Game:

    ### FIELDS ###

    running: bool = None

    bkg_color: Color    = None
    clock: Clock        = None
    screen: Surface     = None
    all_sprites: Group  = None
    background: Surface = None

    block: Block = None
    ghost: Ghost = None


    ### CONSTRUCTOR ###

    def __init__(self):
        pygame.init()
        self.running = False
        self.setup()


    ### OPERATIONAL METHODS ###

    def setup(self):
        self.bkg_color = Color('black')

        self.clock = Clock()
        self.screen = pygame.display.set_mode(SIZE)
        self.screen.fill(self.bkg_color)
        self.all_sprites = Group()

        self.background: Surface = Surface(SIZE)
        self.background.fill(self.bkg_color)

        self.block = Block(size=(PIXEL_SIZE, PIXEL_SIZE), groups=self.all_sprites)
        self.ghost = Ghost('ghost.ss.gif', groups=self.all_sprites)


    def run(self):
        self.running = True
        
        while self.running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.running = False
            
            if self.running:
                self.block.move(Vector2(80, 45))
                self.ghost.move(Vector2(3.2, 1.8))

                dt: float = self.clock.tick() / 1000.
                self.all_sprites.update(dt)

                self.all_sprites.clear(self.screen, self.background)
                self.all_sprites.draw(self.screen)
                pygame.display.flip()

        pygame.quit()
