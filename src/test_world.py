###################################
# test_world.py    [v0.0.1-alpha] #
#=================================#
#                                 #
#---------------------------------#
# J Karstin Neill      05.10.2022 #
###################################


### IMPORTS ###

from pygame import Vector2

from jadacore.being import Being, Going
from jadacore.game import World

from ghost import Ghost


### CLASS DEFINITIONS ###

class TestWorld(World):

    ### FIELDS ###

    being: Being = None
    ghost: Ghost = None
    going: Going = None


    ### OPERATIONAL METHODS ###

    def setup(self):
        self.being = Being()
        self.ghost = Ghost(pos=Vector2(650, 125))
        self.going = Going(move_speed=50, sprite_sheet_path='ghost.ss.gif', sprite_sheet_dims=Vector2(2, 2), pos=Vector2(200, 175))
        self.add(self.being, self.ghost)
        self.add(self.going)

    
    def update(self, dt: float):
        self.being.move(Vector2(80, 45))
        self.ghost.move(Vector2(-5, 0.0))
        self.update_world(dt)
