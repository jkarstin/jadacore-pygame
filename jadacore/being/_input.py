#################################
# _input.py      [v0.0.1-alpha] #
#===============================#
#                               #
#-------------------------------#
# J Karstin Neill    05.21.2022 #
#################################


### IMPORTS ###

import pygame

from . import Component


### CLASS DEFINITIONS ###

class KeyInput(Component):

    ### FIELDS ###

    key_pressed: list[bool] = None
    key_pulled: list[int]   = None


    ### CONSTRUCTOR ###

    def __init__(self,
        name:str
    ) -> None:
        Component.__init__(self, name)

        self.key_pressed = []
        self.key_pulled  = []


    ### COMPONENT METHODS ###

    def on_attach(self) -> None: super().on_attach()


    def update(self, dt: float) -> None:
        self.key_pressed = pygame.key.get_pressed()
        self.key_pulled = []


    def on_detach(self) -> None: super().on_detach()


    ### OPERATIONAL METHODS ###

    def check_key(self, key: int, pull: bool=False) -> bool:
        key_state: bool = False

        K: int = len(self.key_pressed)
        if key in range(K) and key not in self.key_pulled:
            key_state = self.key_pressed[key]
            if pull:
                self.key_pulled.append(key)
        
        return key_state


    def pull_key(self, key: int) -> bool:
        return self.check_key(key, pull=True)
