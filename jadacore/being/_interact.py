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
from pygame import Rect
from pygame.sprite import Group, Sprite
from jadacore.meta import PIXEL_SIZE
import jadacore.util as util
import jadacore.util.log as log

from . import Component, Doing, KeyInput


### CLASS STUBS ###

class InteractBeing(Doing):
    def __init__(self,
        icon_prompt_path: Path=None,
        interact_key: int=None,
        **kwargs
    ): ...
class Interactor(Component):
    def __init__(self,
        name: str,
        interact_group: Group,
        icon_group: Group,
        reach: float=None,
        key_input: KeyInput=None
    ): ...
class Interaction(Component):
    icon_prompt: Sprite
    interact_key: int
    def __init__(self,
        name: str,
        icon_prompt_path: Path=None,
        interact_key: int=None
    ): ...
    def interact(self,
        interactor: Interactor
    ) -> bool: ...



### CONSTANTS & FLAG ###

DEFAULT_REACH: float      = 20
DEFAULT_INTERACT_KEY: int = pygame.K_e


### CLASS DEFINITIONS ###

class InteractBeing(Doing):

    ### FIELDS ###

    interaction: Interaction = None


    ### CONSTRUCTOR ###

    def __init__(self,
        icon_prompt_path: Path=None,
        interact_key: int=None,
        **kwargs
    ):
        Doing.__init__(self, **kwargs)

        self.interaction = Interaction('interaction', icon_prompt_path, interact_key)
        self.attach(self.interaction)
    

    def interact(self,
        interactor: Interactor
    ) -> bool:
        return self.interaction.interact(interactor)



class Interaction(Component):

    ### FIELDS ###

    icon_prompt: Sprite = None
    interact_key: int   = None


    ### CONSTRUCTORS ###

    def __init__(self,
        name: str,
        icon_prompt_path: Path=None,
        interact_key: int=None
    ):
        Component.__init__(self, name)

        icon_prompt_image = util.load_pixel_image(icon_prompt_path)
        if icon_prompt_image:
            self.icon_prompt = Sprite()
            self.icon_prompt.image = icon_prompt_image
            self.icon_prompt.rect  = icon_prompt_image.get_rect()

        self.interact_key = interact_key if interact_key else DEFAULT_INTERACT_KEY
    
    
    def interact(self,
        interactor: Interactor
    ) -> bool:
        log.sprint(interactor)

        return True



class Interactor(Component):

    ### FIELDS ###
    
    interact_group: Group = None
    icon_group: Group     = None
    reach: float          = None
    reach_check: Sprite   = None
    key_input: KeyInput   = None

    
    ### CONSTRUCTOR ###

    def __init__(self,
        name: str,
        interact_group: Group,
        icon_group: Group,
        reach: float=None,
        key_input: KeyInput=None
    ):
        Component.__init__(self, name)

        self.interact_group = interact_group
        self.icon_group = icon_group

        self.reach = reach * PIXEL_SIZE if reach else DEFAULT_REACH * PIXEL_SIZE
#        self.reach_sqrd = self.reach * self.reach
        self.reach_check = Sprite()
        self.reach_check.rect = Rect(
            (0.0, 0.0),
            (self.reach * 2, self.reach * 2)
        )
        self.reach_check.radius = self.reach

#        if cue_icon_path:
#            self.cue_icon = Sprite()
#            self.cue_icon.image = util.load_pixel_image(cue_icon_path)
#            if self.cue_icon.image:
#                self.cue_icon.rect = self.cue_icon.image.get_rect()

        self.key_input = key_input
#        self.interact_key = interact_key if interact_key else DEFAULT_INTERACT_KEY

    
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
            for sprite in collided_sprites:
                interact_being: InteractBeing = sprite

                if interact_being.interaction.icon_prompt:
                    interact_being.interaction.icon_prompt.rect.centerx = interact_being.rect.centerx
                    interact_being.interaction.icon_prompt.rect.bottom  = interact_being.rect.top
                    self.icon_group.add(interact_being.interaction.icon_prompt)

                if self.key_input.pull_key(interact_being.interaction.interact_key):
                    s: bool = interact_being.interact(self)
                    log.sprint(f"Interaction success: {s}")

                    #TODO: Handle in Inventory (maybe make Inventory a child of Interactor)
#                    interact_being.remove(interact_being.groups())
#                    self.inventory.add_item(interact_being.item)
            