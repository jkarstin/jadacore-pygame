#################################
# being.py       [v0.0.1-alpha] #
#===============================#
#                               #
#-------------------------------#
# J Karstin Neill    05.10.2022 #
#################################


### IMPORTS ###

from pathlib import Path
import pygame
from pygame import Color, Surface, Rect, Vector2
from pygame.sprite import Group, Sprite
from typing import Optional

from jadacore.meta import RESOURCES_PATH, PIXEL_SIZE


### CLASS DEFINITIONS ###

class Component:

    being: Optional['Being'] = None

    
    def setup(self, **kwargs): pass
    def update(self, dt: float, **kwargs): pass
    

    def attach_to(self, being: Optional['Being']=None, **kwargs):
        self.being = being
        self.setup(**kwargs)


class Being(Sprite):

    ### FIELD ###

    size: Vector2  = None
    image: Surface = None
    rect: Rect     = None

    pos: Vector2       = None
    move_vect: Vector2 = None

    components: list[Component] = None


    ### CONSTRUCTOR ###

    def __init__(self,
        pos: Vector2=Vector2(0.0, 0.0),
        size: Vector2=Vector2(1, 1),
        color: Color=None,
        image_path: Path=None,
        groups: list[Group]=None
    ) -> None:
        Sprite.__init__(self)

        self.pos = pos if pos else Vector2()
        self.size = PIXEL_SIZE * (size if size else Vector2(1))

        if image_path:
            image_raw: Surface = pygame.image.load(RESOURCES_PATH/image_path)
            self.image = pygame.transform.scale(
                image_raw.convert_alpha(),
                [image_raw.get_width() * self.size.x, image_raw.get_height() * self.size.y]
            )
        else:
            self.image = Surface(self.size)
            self.image.fill(color if color else Color('pink'))
        
        self.rect = self.image.get_rect()

        if groups:
            for group in groups: group.add(self)

        self.components = []


    ### OPERATIONAL METHODS ###

    def update(self, dt: float) -> None:
        if self.move_vect:
            self.pos.x += self.move_vect.x * PIXEL_SIZE * dt
            self.pos.y += self.move_vect.y * PIXEL_SIZE * dt
            self.move_vect = None
        
        self.rect.x = int(self.pos.x / PIXEL_SIZE) * PIXEL_SIZE
        self.rect.y = int(self.pos.y / PIXEL_SIZE) * PIXEL_SIZE

    
    ### AUXILIARY METHODS ###

    def move(self, move_vect: Vector2=None) -> None:
        self.move_vect = move_vect

    
    def add_component(self, component: Component=None) -> None:
        if component and component not in self.components:
            self.components.append(component)

    
    def remove_component(self, component: Component=None) -> None:
        if component and component in self.components:
            self.components.remove(component)
    