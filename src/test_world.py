###################################
# test_world.py    [v0.0.1-alpha] #
#=================================#
#                                 #
#---------------------------------#
# J Karstin Neill      05.10.2022 #
###################################


### IMPORTS ###

from pygame import Vector2

from jadacore.being import Being
from jadacore.game import World

from ghost import Ghost


### CLASS DEFINITIONS ###

class TestWorld(World):

    ### FIELDS ###

    being: Being = None
    ghost: Ghost = None


    ### OPERATIONAL METHODS ###

    def setup(self):
        self.being = Being()
        self.ghost = Ghost(pos=Vector2(650, 125))
        self.add(self.being, self.ghost)

    
    def update(self, dt: float):
        self.being.move(Vector2(80, 45))
        self.ghost.move(Vector2(-5, 0.0))
        self.update_world(dt)
        