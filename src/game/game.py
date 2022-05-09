#################################
# game.py        [v0.0.1-alpha] #
#===============================#
#                               #
#-------------------------------#
# J Karstin Neill    05.06.2022 #
#################################


### IMPORTS ###

import pygame
from pygame.time import Clock

from . import Window
from test_world import TestWorld


### CONSTANTS & FLAGS ###


### CLASS DEFINITIONS ###

class Game:

    ### FIELDS ###

    running: bool  = None
    clock: Clock   = None
    window: Window = None


    ### CONSTRUCTOR ###

    def __init__(self):
        pygame.init()
        self.running = False
        self.window = Window()
        self.window.set_world(TestWorld())


    ### OPERATIONAL METHODS ###

    def run(self):
        self.running = True
        self.clock = Clock()

        while self.running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.running = False
            
            if self.running:
                dt: float = self.clock.tick() / 1000.
                self.window.update(dt)

                self.window.render()

        pygame.quit()
