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

from . import Window, World


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


    ### OPERATIONAL METHODS ###

    def run(self) -> None:
        """
        run() -> None

        Starts up the Game instance, and returns upon pygame.QUIT event.
        """

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

    
    ### AUXILIARY METHODS ###

    def set_world(self, world: World) -> None:
        self.window.set_world(world)
