#################################
# being.py       [v0.0.1-alpha] #
#===============================#
#                               #
#-------------------------------#
# J Karstin Neill    05.06.2022 #
#################################


### IMPORTS ###

from pathlib import Path
import pygame
from pygame import Color, Surface, Rect, Vector2
from pygame.sprite import Group, Sprite
from typing import Union

from meta.meta import PIXEL_SIZE, RESOURCES_PATH


### CLASS DEFINITIONS ###

class Being(Sprite):

    ### FIELD ###

    pos: Vector2   = None
    size: Vector2  = None
    image: Surface = None
    rect: Rect     = None

    move_vect: Vector2 = None


    ### CONSTRUCTOR ###

    def __init__(
        self,
        pos: Vector2=None,
        size: Vector2=None,
        color: Color=None,
        image_path: Path=None,
        groups: Union[Group, list[Group]]=None
    ) -> None:
        Sprite.__init__(self)

        self.pos = pos if pos else Vector2()
        self.size = size if size else Vector2(PIXEL_SIZE)

        if image_path:
            image_raw: Surface = pygame.image.load(RESOURCES_PATH/image_path)
            self.image = pygame.transform.scale(
                image_raw.convert_alpha(),
                (image_raw.get_width() * self.size.x, image_raw.get_height() * self.size.y)
            )
        else:
            self.image = Surface(self.size)
            self.image.fill(color if color else Color('pink'))
        
        self.rect = self.image.get_rect()

        if type(groups) == Group:
            groups.add(self)
        elif type(groups) == list:
            for group in groups:
                group.add(self)


    ### OPERATIONAL METHODS ###

    def update(self, dt: float) -> None:
        if self.move_vect:
            self.pos.x += self.move_vect.x * dt
            self.pos.y += self.move_vect.y * dt
            self.move_vect = None
        
        self.rect.x = int(self.pos.x / PIXEL_SIZE) * PIXEL_SIZE
        self.rect.y = int(self.pos.y / PIXEL_SIZE) * PIXEL_SIZE

    
    def move(self, move_vect: Vector2=None) -> None:
        self.move_vect = move_vect
