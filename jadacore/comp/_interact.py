##################################
# _interact.py    [v0.0.1-alpha] #
#================================#
#                                #
#--------------------------------#
# J Karstin Neill     05.17.2022 #
##################################


### IMPORTS ###

from pathlib import Path
import pygame
from pygame import Rect, Surface, Vector2
from pygame.sprite import Group, Sprite
from typing import Optional

import jadacore.being
from jadacore.being import Component
from jadacore.meta import RESOURCES_PATH, PIXEL_SIZE
from . import Inventory


### CONSTANTS & FLAG ###

DEFAULT_REACH: float = 10.0


### CLASS DEFINITIONS ###

class Interactor(Component):

    ### FIELDS ###
    
    interact_group: Group = None
    reach: float          = None
    reach_sqrd: float     = None
    reach_check: Rect     = None
    cue_icon: Surface     = None
    inventory: Inventory  = None

    
    ### CONSTRUCTOR ###

    def __init__(self,
        name: str,
        interact_group: Group,
        reach: float=None,
        cue_icon_path: Path=None,
        inventory: Inventory=None
    ) -> None:
        Component.__init__(self, name)

        self.interact_group = interact_group

        self.reach = reach if reach else DEFAULT_REACH
        self.reach_sqrd = self.reach * self.reach
        self.reach_check = Rect(
            (0.0, 0.0),
            (self.reach * 2, self.reach * 2)
        )

        if cue_icon_path:
            cue_icon_raw: Surface = pygame.image.load(RESOURCES_PATH/cue_icon_path)
            if cue_icon_raw:
                self.cue_icon = pygame.transform.scale(
                    cue_icon_raw.convert_alpha(),
                    (cue_icon_raw.get_width() * PIXEL_SIZE, cue_icon_raw.get_height() * PIXEL_SIZE)
                )
        
        self.inventory = inventory

    
    ### COMPONENT METHODS ###

    def on_attach(self) -> None: super().on_attach()


    def update(self, dt: float) -> None:
        def interact_with(*item_beings: Optional['jadacore.being.ItemBeing']):
            for item_being in item_beings:
                delta: Vector2 = item_being.pos - self.being.pos
                if delta.length_squared() <= self.reach_sqrd:
                    item_being.remove(item_being.groups())
                    self.inventory.add_item(item_being.item)
                    print(self.inventory.items)

        self.reach_check.center = (self.being.pos.x, self.being.pos.y)

        collide_indices: list[int] = self.reach_check.collidelistall(
            [
                item_sprite.rect
                for item_sprite in self.interact_group.sprites()
            ]
        )
        interact_items: list[Sprite] = [self.interact_group.sprites()[i] for i in collide_indices]

        interact_with(*interact_items)


    def on_detach(self) -> None: super().on_detach()
