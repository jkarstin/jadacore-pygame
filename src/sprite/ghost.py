#################################
# ghost.py       [v0.0.1-alpha] #
#===============================#
#                               #
#-------------------------------#
# J Karstin Neill    05.06.2022 #
#################################


### IMPORTS ###

from pathlib import Path
import pygame
from pygame import Rect
from pygame import Surface
from pygame import Vector2
from pygame.sprite import Sprite

from meta import PIXEL_SIZE, RESOURCES_PATH


### CONSTANTS & FLAGS ###


### CLASS DEFINITIONS ###

class Ghost(Sprite):

    ### FIELDS ###

    image: Surface = None
    rect: Rect     = None
    pos: Vector2   = None

    move_vect: Vector2 = None

    ### CONSTRUCTOR ###

    def __init__(self, ghost_path: Path, pos: Vector2=None):
        Sprite.__init__(self)

        image_raw: Surface = pygame.image.load(RESOURCES_PATH / ghost_path).convert_alpha()
        self.image = pygame.transform.scale(
            image_raw,
            (image_raw.get_width() * PIXEL_SIZE, image_raw.get_height() * PIXEL_SIZE)
        )
        self.rect = self.image.get_rect()

        self.pos = pos if pos else Vector2()
    

    ### METHODS ###

    def update(self, dt: float):
        if self.move_vect:
            self.pos.x += self.move_vect.x * dt
            self.pos.y += self.move_vect.y * dt
            self.move_vect = None

        self.rect.x = int(self.pos.x / PIXEL_SIZE) * PIXEL_SIZE
        self.rect.y = int(self.pos.y / PIXEL_SIZE) * PIXEL_SIZE

    
    def move(self, move_vect: Vector2=None):
        self.move_vect = move_vect
