#################################
# _input.py      [v0.0.1-alpha] #
#===============================#
#                               #
#-------------------------------#
# J Karstin Neill    05.18.2022 #
#################################


### IMPORTS ###

import pygame

from jadacore.being import Component


### CLASS DEFINITIONS ###

class KeyInput(Component):

    ### FIELDS ###

    key_pressed: list[bool] = None
    key_pulled: list[bool]  = None


    ### CONSTRUCTOR ###

    def __init__(self,
        name:str
    ) -> None:
        Component.__init__(self, name)

        self.key_presses = []
        self.key_pulled  = []


    ### COMPONENT METHODS ###

    def on_attach(self) -> None: super().on_attach()


    def update(self, dt: float) -> None:
        self.key_pressed = pygame.key.get_pressed()
        self.key_pulled = [False] * len(self.key_pressed)


    def on_detach(self) -> None: super().on_detach()


    ### OPERATIONAL METHODS ###

    def check_key(self, key: int) -> bool:
        if self.key_pressed and key in range(len(self.key_pressed)):
            return (self.key_pressed[key] and not self.key_pulled[key])
        
        return False


    def pull_key(self, key: int) -> None:
        if self.key_pulled and key in range(len(self.key_pulled)):
            self.key_pulled[key] = True
