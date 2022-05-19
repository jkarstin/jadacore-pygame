##################################
# _interact.py    [v0.0.1-alpha] #
#================================#
#                                #
#--------------------------------#
# J Karstin Neill     05.18.2022 #
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
from . import Inventory, KeyInput


### CONSTANTS & FLAG ###

DEFAULT_REACH: float      = 10.0
DEFAULT_INTERACT_KEY: int = pygame.K_e


### CLASS DEFINITIONS ###

class Interactor(Component):

    ### FIELDS ###
    
    interact_group: Group = None
    icon_group: Group     = None
    reach: float          = None
    reach_sqrd: float     = None
    reach_check: Sprite   = None
    cue_icon: Sprite      = None
    inventory: Inventory  = None
    key_input: KeyInput   = None
    interact_key: int     = None

    
    ### CONSTRUCTOR ###

    def __init__(self,
        name: str,
        interact_group: Group,
        icon_group: Group,
        reach: float=None,
        cue_icon_path: Path=None,
        inventory: Inventory=None,
        key_input: KeyInput=None,
        interact_key: int=None
    ) -> None:
        Component.__init__(self, name)

#        import pdb; pdb.set_trace()

        self.interact_group = interact_group
        self.icon_group = icon_group

        self.reach = reach if reach else DEFAULT_REACH
        self.reach_sqrd = self.reach * self.reach
        self.reach_check = Sprite()
        self.reach_check.rect = Rect(
            (0.0, 0.0),
            (self.reach * 2, self.reach * 2)
        )
        self.reach_check.radius = self.reach

        if cue_icon_path:
            self.cue_icon = Sprite()
            cue_icon_image_raw: Surface = pygame.image.load(RESOURCES_PATH/cue_icon_path)
            if cue_icon_image_raw:
                self.cue_icon.image = pygame.transform.scale(
                    cue_icon_image_raw.convert_alpha(),
                    (cue_icon_image_raw.get_width() * PIXEL_SIZE, cue_icon_image_raw.get_height() * PIXEL_SIZE)
                )
                self.cue_icon.rect = self.cue_icon.image.get_rect()

        self.inventory = inventory
        self.key_input = key_input
        self.interact_key = interact_key if interact_key else DEFAULT_INTERACT_KEY

    
    ### COMPONENT METHODS ###

    def on_attach(self) -> None: super().on_attach()


    def update(self, dt: float) -> None:
        self.reach_check.rect.center = (self.being.pos.x, self.being.pos.y)
        collided_sprites = pygame.sprite.spritecollide(
            self.reach_check,
            self.interact_group,
            dokill=False,
            collided=pygame.sprite.collide_circle
        )

        self.icon_group.empty()
        if len(collided_sprites) > 0:
            for item_being in collided_sprites:
                self.cue_icon.rect.centerx = item_being.rect.centerx
                self.cue_icon.rect.bottom = item_being.rect.top
                self.icon_group.add(self.cue_icon)

        def interact_with(*item_beings: Optional['jadacore.being.ItemBeing']):
            for item_being in item_beings:
                item_being.remove(item_being.groups())
                self.inventory.add_item(item_being.item)

        if self.key_input.pull_key(self.interact_key):
            interact_with(*collided_sprites)
            

    def on_detach(self) -> None: super().on_detach()
