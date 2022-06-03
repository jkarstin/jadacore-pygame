#################################
# _input.py      [v0.0.1-alpha] #
#===============================#
#                               #
#-------------------------------#
# J Karstin Neill    06.03.2022 #
#################################


### IMPORTS ###

from typing import Callable
import pygame
from pygame import Vector2

from . import Component


### CLASS STUBS ###

class Input(Component):
    def __init__(self,
        name: str,
        gather_function: Callable
    ): ...
class KeyInput(Input):
    def __init__(self,
        name: str
        ): ...
class MouseInput(Input):
    def __init__(self,
        name: str
    ): ...

class Input(Component):
    pressed: list[bool]
    pulled: list[int]
    gather_function: Callable
    def __init__(self,
        name: str,
        gather_function: Callable
    ): ...
    def update(self, dt: float): ...
    def check(self, i: int, pull: bool=False) -> bool: ...
    def pull(self, i: int) -> bool: ...
class KeyInput(Input):
    def __init__(self,
        name: str
    ): ...
    def check_key(self, key: int, pull: bool=False) -> bool: ...
    def pull_key(self, key: int) -> bool: ...
class MouseInput(Input):
    mouse_pos: Vector2
    def __init__(self,
        name: str
    ): ...
    def update(self, dt: float): ...
    def check_button(self, btn: int, pull: bool=False) -> bool: ...
    def pull_button(self, btn: int) -> bool: ...


### CLASS DEFINITIONS ###

class Input(Component):
    pressed: list[bool]       = None
    pulled: list[int]         = None
    gather_function: Callable = None

    def __init__(self,
        name: str,
        gather_function: Callable
    ):
        Component.__init__(self, name)

        self.pressed = []
        self.pulled  = []
        self.gather_function = gather_function

    
    def update(self, dt: float):
        if self.gather_function:
            self.pressed = self.gather_function()
        self.pulled = []
    
    
    def check(self,
        i: int,
        pull: bool=False
    ) -> bool:
        state: bool = False

        N: int = len(self.pressed)
        if i in range(N) and i not in self.pulled:
            state = self.pressed[i]
            if pull:
                self.pulled.append(i)
        
        return state

    
    def pull(self,
        i: int
    ) -> bool:
        return self.check(i, pull=True)



class KeyInput(Input):

    ### CONSTRUCTOR ###

    def __init__(self,
        name: str
    ):
        Input.__init__(self, name, pygame.key.get_pressed)


    ### WRAPPER METHODS ###

    def check_key(self, key: int, pull: bool=False) -> bool:
        return super().check(key, pull)


    def pull_key(self, key: int) -> bool:
        return super().pull(key)



class MouseInput(Input):
    
    ### FIELDS ###

    mouse_pos: Vector2 = None


    ### CONSTRUCTOR ###

    def __init__(self,
        name: str
    ):
        Input.__init__(self, name, pygame.mouse.get_pressed)


    ### COMPONENT METHODS ###

    def update(self, dt: float):
        super().update(dt)

        mouse_pos_raw: tuple[int, int] = pygame.mouse.get_pos()
        self.mouse_pos = Vector2(*mouse_pos_raw)


    ### WRAPPER METHODS ###

    def check_button(self, btn: int, pull: bool=False) -> bool:
        # NOTE: use btn-1 to index pressed, as this is how pygame.mouse.get_pressed() stores these states
        return super().check(btn-1, pull)


    def pull_button(self, btn: int) -> bool:
        # NOTE: use btn-1 to index pressed, as this is how pygame.mouse.get_pressed() stores these states
        return super().pull(btn-1)
