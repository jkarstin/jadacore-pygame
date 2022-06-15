##################################
# interact.py     [v0.0.2-alpha] #
#================================#
#                                #
#--------------------------------#
# J Karstin Neill     06.14.2022 #
##################################


### IMPORTS ###

from pathlib import Path
import pygame
from pygame import Rect
from pygame.sprite import Group, Sprite

from jadacore.being import Component
from jadacore.doing import Doing
from jadacore.input import Input, KeyInput, MouseInput
from jadacore.meta import PIXEL_SIZE
import jadacore.util as util


### CLASS STUBS ###

class Interactable(Doing):
    def __init__(self,
        sprite_sheet_path: Path,
        icon_path: Path=None,
        interact_key: int=None,
        **kwargs
    ): ...
class Interaction(Component):
    def __init__(self,
        name: str,
        icon_path: Path=None,
        interact_i: int=None
    ): ...
class KeyInteraction(Interaction):
    def __init__(self,
        name: str,
        interact_key: int=None,
        **kwargs
    ): ...
class ClickInteraction(Interaction):
    def __init__(self,
        name: str,
        interact_btn: int=None,
        **kwargs
    ):...
class Interactor(Component):
    def __init__(self,
        name: str,
        interact_group: Group,
        icon_group: Group,
        reach: float=None,
        input: Input=None
    ): ...
class KeyInteractor(Interactor):
    def __init__(self,
        name: str,
        interact_group: Group,
        icon_group: Group,
        key_input: KeyInput=None,
        **kwargs
    ): ...
class ClickInteractor(Interactor):
    def __init__(self,
        name: str,
        interact_group: Group,
        icon_group: Group,
        mouse_input: MouseInput=None,
        **kwargs
    ): ...

class Interactable(Doing):
    interaction: Interaction
    def __init__(self,
        sprite_sheet_path: Path,
        icon_path: Path=None,
        interact_key: int=None,
        **kwargs
    ): ...
    def interact(self, interactor: Interactor): ...
class Interaction(Component):
    icon_prompt: Sprite
    interact_i: int
    def __init__(self,
        name: str,
        icon_path: Path=None,
        interact_i: int=None
    ): ...
    def interact(self, interactor: Interactor): ...
class KeyInteraction(Interaction):
    interact_key: int
    def __init__(self,
        name: str,
        interact_key: int=None,
        **kwargs
    ): ...
class ClickInteraction(Interaction):
    interact_btn: int
    def __init__(self,
        name: str,
        interact_btn: int=None,
        **kwargs
    ):...
class Interactor(Component):
    interact_group: Group
    icon_group: Group
    reach: float
    reach_check: Sprite
    input: Input
    def __init__(self,
        name: str,
        interact_group: Group,
        icon_group: Group,
        reach: float=None,
        input: Input=None
    ): ...
    def interaction_trigger(self, interaction: Interaction) -> bool: ...
    def update(self, dt: float): ...
class KeyInteractor(Interactor):
    key_input: KeyInput
    def __init__(self,
        name: str,
        interact_group: Group,
        icon_group: Group,
        key_input: KeyInput=None,
        **kwargs
    ): ...
    def interaction_trigger(self, key_interaction: KeyInteraction) -> bool: ...
class ClickInteractor(Interactor):
    mouse_input: MouseInput
    def __init__(self,
        name: str,
        interact_group: Group,
        icon_group: Group,
        mouse_input: MouseInput=None,
        **kwargs
    ): ...
    def interaction_trigger(self, click_interaction: ClickInteraction) -> bool: ...


### CONSTANTS & FLAG ###

# ::KeyInteraction
DEFAULT_INTERACT_KEY: int = pygame.K_e

# ::ClickInteraction
DEFAULT_INTERACT_BTN: int = pygame.BUTTON_LEFT

# ::Interactor
DEFAULT_REACH: float = 20


### CLASS DEFINITIONS ###

class Interactable(Doing):

    ### FIELDS ###

    interaction: Interaction = None


    ### CONSTRUCTOR ###

    def __init__(self,
        sprite_sheet_path: Path,
        icon_path: Path=None,
        interact_key: int=None,
        **kwargs
    ):
        Doing.__init__(self, sprite_sheet_path, **kwargs)

        self.interaction = Interaction('interaction', icon_path, interact_key)
        self.attach(self.interaction)
    

    ### WRAPPER METHODS ###

    def interact(self, interactor: Interactor):
        self.interaction.interact(interactor)



class Interaction(Component):

    ### FIELDS ###

    icon_prompt: Sprite = None
    interact_i: int = None


    ### CONSTRUCTOR ###

    def __init__(self,
        name: str,
        icon_path: Path=None,
        interact_i: int=None
    ):
        Component.__init__(self, name)

        icon_image = util.load_pixel_image(icon_path)
        if icon_image:
            self.icon_prompt = Sprite()
            self.icon_prompt.image = icon_image
            self.icon_prompt.rect  = icon_image.get_rect()
        
        self.interact_i = interact_i

    
    ### OPERATIONAL METHODS ###

    def interact(self, interactor: Interactor): pass
        


class KeyInteraction(Interaction):

    ### FIELDS ###

    interact_key: int = None


    ### CONSTRUCTOR ###

    def __init__(self,
        name: str,
        interact_key: int=None,
        **kwargs
    ):
        Interaction.__init__(self,
            name,
            interact_i=interact_key,
            **kwargs
        )

        self.interact_key = interact_key if interact_key else DEFAULT_INTERACT_KEY



class ClickInteraction(Interaction):

    ### FIELDS ###

    interact_btn: int = None


    ### CONSTRUCTOR ###

    def __init__(self,
        name: str,
        interact_btn: int=None,
        **kwargs
    ):
        Interaction.__init__(self,
            name,
            interact_i=interact_btn,
            **kwargs
        )

        self.interact_btn = interact_btn if interact_btn else DEFAULT_INTERACT_BTN



class Interactor(Component):

    ### FIELDS ###
    
    interact_group: Group = None
    icon_group: Group     = None
    reach: float          = None
    reach_check: Sprite   = None
    input: Input          = None

    
    ### CONSTRUCTOR ###

    def __init__(self,
        name: str,
        interact_group: Group,
        icon_group: Group,
        reach: float=None,
        input: Input=None
    ):
        Component.__init__(self, name)

        self.interact_group = interact_group
        self.icon_group = icon_group

        self.reach = reach * PIXEL_SIZE if reach else DEFAULT_REACH * PIXEL_SIZE
        self.reach_check = Sprite()
        self.reach_check.rect = Rect(
            (0.0, 0.0),
            (self.reach * 2, self.reach * 2)
        )
        self.reach_check.radius = self.reach

        self.input = input


    ### OPERATIONAL METHODS ###

    def interaction_trigger(self, interaction: Interaction) -> bool:
        if not (interaction and self.input):
            return False

        return self.input.pull(interaction.interact_i)

    
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
                interact_being: Interactable = sprite
                icon: Sprite = interact_being.interaction.icon_prompt
                
                if icon and icon not in self.icon_group.sprites():
                    icon.rect.centerx = interact_being.rect.centerx
                    icon.rect.bottom  = interact_being.rect.top
                    self.icon_group.add(icon)

                if self.interaction_trigger(interact_being.interaction):
                    interact_being.interact(self)



class KeyInteractor(Interactor):

    ### FIELDS ###

    key_input: KeyInput = None

    
    ### CONSTRUCTOR ###

    def __init__(self,
        name: str,
        interact_group: Group,
        icon_group: Group,
        key_input: KeyInput=None,
        **kwargs
    ):
        Interactor.__init__(self,
            name, interact_group, icon_group,
            input=key_input,
            **kwargs
        )

        self.key_input = key_input


    ### INTERACTOR METHODS ###

    def interaction_trigger(self, key_interaction: KeyInteraction) -> bool:
        if not (key_interaction and self.key_input):
            return False

        return self.key_input.pull_key(key_interaction.interact_key)



class ClickInteractor(Interactor):

    ### FIELDS ###

    mouse_input: MouseInput = None


    ### COSTRUCTORS ###

    def __init__(self,
        name: str,
        interact_group: Group,
        icon_group: Group,
        mouse_input: MouseInput=None,
        **kwargs
    ):
        Interactor.__init__(self,
            name, interact_group, icon_group,
            input=mouse_input,
            **kwargs
        )

        self.mouse_input = mouse_input


    ### Interactor Methods ###

    def interaction_trigger(self, click_interaction: ClickInteraction) -> bool:
        if not (click_interaction and self.mouse_input):
            return False
        
        return self.mouse_input.pull_button(click_interaction.interact_btn)
