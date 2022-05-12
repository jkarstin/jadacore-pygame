#################################
# being.py       [v0.0.1-alpha] #
#===============================#
#                               #
#-------------------------------#
# J Karstin Neill    05.11.2022 #
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

    
    def setup(self) -> None: pass
    def update(self, dt: float) -> None: pass
    def cleanup(self) -> None: pass


    def attach_to(self, being: Optional['Being']=None) -> None:
        if being:
            if self.being:
                self.being.detach_component(self)
            self.being = being
            self.setup()

    
    def detach_from(self, being: Optional['Being']=None) -> None:
        if being:
            if self.being and self.being == being:
                self.cleanup()
                self.being = None



class Motor(Component):

    ### FIELDS ###

    move_vect: Vector2 = None


    ### OPERATIONAL METHODS ###

    def setup(self): pass
    def cleanup(self): pass


    def update(self, dt: float):
        if self.being:
            if self.move_vect:
                self.being.pos.x += self.move_vect.x * PIXEL_SIZE * dt
                self.being.pos.y += self.move_vect.y * PIXEL_SIZE * dt
                self.move_vect = None


    def move(self, move_vect: Vector2):
        self.move_vect = move_vect



class Being(Sprite):

    ### FIELDS ###

    size: Vector2  = None
    image: Surface = None
    rect: Rect     = None

    pos: Vector2   = None

    components: list[Component] = None
    motor: Motor   = None


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

        self.motor = Motor()
        self.attach_component(self.motor)


    ### OPERATIONAL METHODS ###

    def update(self, dt: float) -> None:
        for comp in self.components: comp.update(dt)
        
        self.rect.x = int(self.pos.x / PIXEL_SIZE) * PIXEL_SIZE
        self.rect.y = int(self.pos.y / PIXEL_SIZE) * PIXEL_SIZE


    def move(self, move_vect: Vector2=None) -> None:
        if self.motor:
            self.motor.move(move_vect)

    
    ### AUXILIARY METHODS ###
    
    def attach_component(self, component: Component=None) -> None:
        if component and component not in self.components:
            self.components.append(component)
            component.attach_to(self)

    
    def detach_component(self, component: Component=None) -> None:
        if component and component in self.components:
            self.components.remove(component)
            component.detach_from(self)
    