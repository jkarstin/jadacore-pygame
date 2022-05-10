#################################
# world.py       [v0.0.1-alpha] #
#===============================#
#                               #
#-------------------------------#
# J Karstin Neill    05.07.2022 #
#################################


### IMPORTS ###

from pygame import Surface
from pygame.sprite import Group

from jadacore.being import Being
from jadacore.meta import WINDOW_SIZE


### CONSTANTS & FLAGS ###


### CLASS DEFINITIONS ###

class World:

    ### FIELDS ###

    world_group: Group    = None
    world_screen: Surface = None


    ### CONSTRUCTOR ###

    def __init__(self) -> None:
        self.world_group = Group()
        self.world_screen = Surface(WINDOW_SIZE)
        self.setup()


    ### OPERATIONAL FUNCTIONS ###

    def setup(self) -> None: pass
    def update(self, dt: float) -> None: pass


    def update_world(self, dt: float) -> None:
        self.world_group.update(dt)

    
    def draw(self, base_screen: Surface) -> None:
        self.world_group.clear(base_screen, self.world_screen)
        self.world_group.draw(base_screen)


    ### UTILITY FUNCTIONS ###

    def add(self, *beings: Being) -> None:
        self.world_group.add(*beings)
