##################################
# _interact.py    [v0.0.1-alpha] #
#================================#
#                                #
#--------------------------------#
# J Karstin Neill     06.01.2022 #
##################################


### IMPORTS ###

from pathlib import Path
import pygame
from pygame import Rect, Surface
from pygame.sprite import Group, Sprite
from jadacore.meta import PIXEL_SIZE
import jadacore.util as util
import jadacore.util.log as log

from . import Component, Inventory, KeyInput, ItemBeing


### CLASS STUBS ###

class Interaction(Component):
    def __init__(self,
        name: str
    ): ...
class Interactor(Component):
    def __init__(self,
        name: str,
        interact_group: Group,
        icon_group: Group,
        reach: float=None,
        cue_icon_path: Path=None,
        inventory: Inventory=None,
        key_input: KeyInput=None,
        interact_key: int=None
    ): ...


### CONSTANTS & FLAG ###

DEFAULT_REACH: float      = 20
DEFAULT_INTERACT_KEY: int = pygame.K_e


### CLASS DEFINITIONS ###

class Interaction(Component):

    ### FIELDS ###

    icon_prompt: Surface = None
    interact_key: int    = None


    ### CONSTRUCTORS ###

    def __init__(self,
        name: str,
        icon_prompt_path: Path=None,
        interact_key: int=None
    ):
        Component.__init__(self, name)

        icon_prompt = util.load_pixel_image(icon_prompt_path)
        self.interact_key = interact_key if interact_key else DEFAULT_INTERACT_KEY
    
    
    def interact(self,
        interactor: Interactor
    ) -> bool:
        log(interactor)

        return False



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
    ):
        Component.__init__(self, name)

        self.interact_group = interact_group
        self.icon_group = icon_group

        self.reach = reach * PIXEL_SIZE if reach else DEFAULT_REACH * PIXEL_SIZE
        self.reach_sqrd = self.reach * self.reach
        self.reach_check = Sprite()
        self.reach_check.rect = Rect(
            (0.0, 0.0),
            (self.reach * 2, self.reach * 2)
        )
        self.reach_check.radius = self.reach

        if cue_icon_path:
            self.cue_icon = Sprite()
            self.cue_icon.image = util.load_pixel_image(cue_icon_path)
            if self.cue_icon.image:
                self.cue_icon.rect = self.cue_icon.image.get_rect()

        self.inventory = inventory
        self.key_input = key_input
        self.interact_key = interact_key if interact_key else DEFAULT_INTERACT_KEY

    
    ### COMPONENT METHODS ###

    def update(self, dt: float):
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

        def interact_with(*item_beings: ItemBeing):
            for item_being in item_beings:
                item_being.remove(item_being.groups())
                self.inventory.add_item(item_being.item)

        if self.key_input.pull_key(self.interact_key):
            interact_with(*collided_sprites)
            