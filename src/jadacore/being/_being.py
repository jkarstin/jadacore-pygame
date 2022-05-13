#################################
# _being.py      [v0.0.1-alpha] #
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

from jadacore.meta import RESOURCES_PATH, PIXEL_SIZE, ERROR_UNNAMED_COMPONENT
import jadacore.util.log as log


### CLASS DEFINITIONS ###

class Being(Sprite):

    ### FIELDS ###

    size: Vector2  = None
    image: Surface = None
    rect: Rect     = None

    components: dict[str, Optional['Component']] = None


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

        self.components = {}


    ### OPERATIONAL METHODS ###

    def update(self, dt: float) -> None:
        for comp_name in self.components:
            self.components[comp_name].update(dt)

    
    ### AUXILIARY METHODS ###
    
    def attach_component(self, component: Optional['Component']=None) -> None:
        if component and component.name not in self.components:
            self.components[component.name] = component
            component.attach_to(self)


    def fetch_component(self, comp_name: str) -> Optional['Component']:
        if comp_name and comp_name in self.components:
            return self.components[comp_name]
        return None

    
    def detach_component(self, component: Optional['Component']=None) -> None:
        if component and component.name in self.components:
            self.components.pop(component.name)
            component.detach_from(self)
    


class Component:

    name: str    = None
    being: Being = None


    def __init__(self, name: str):
        if not name: log.error("Cannot initialize Component without a name!", ERROR_UNNAMED_COMPONENT)
        self.name = name

    
    def on_attach(self) -> None: pass
    def update(self, dt: float) -> None: pass
    def on_detach(self) -> None: pass


    def attach_to(self, being: Being=None) -> None:
        if being:
            if self.being:
                self.being.detach_component(self)
            self.being = being
            self.on_attach()

    
    def detach_from(self, being: Being=None) -> None:
        if being:
            if self.being and self.being == being:
                self.on_detach()
                self.being = None
