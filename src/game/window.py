#################################
# window.py      [v0.0.1-alpha] #
#===============================#
#                               #
#-------------------------------#
# J Karstin Neill    05.07.2022 #
#################################


### IMPORTS ###

import pygame
from pygame import Surface, Vector2

from . import World
from meta import WINDOW_SIZE


### CONSTANTS & FLAGS ###


### CLASS DEFINITIONS ###

class Window:

    ### FIELDS ###

    size: Vector2        = None
    base_screen: Surface = None
    world: World         = None


    ### CONSTRUCTOR ###

    def __init__(self, world: World=None) -> None:
        self.size = WINDOW_SIZE
        self.base_screen = pygame.display.set_mode(WINDOW_SIZE)
        self.world = world


    ### OPERATIONAL FUNCTIONS ###

    def update(self, dt: float):
        if self.world:
            self.world.update(dt)

    
    def render(self):
        if self.world:
            self.world.draw(self.base_screen)
            pygame.display.flip()


    ### UTILITY FUNCTIONS ###

    def set_world(self, world: World):
        self.world = world
