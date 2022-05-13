####################################
# start_world.py    [v0.0.1-alpha] #
#==================================#
#                                  #
#----------------------------------#
# J Karstin Neill       05.13.2022 #
####################################


### IMPORTS ###

from pygame import Vector2

from jadacore.game import World
from jadacore.player import GoPlayer, SeekPlayer

from ghost import Ghost


### CLASS DEFINITIONS ###

class StartWorld(World):

    ### FIELDS ###

    ghost: Ghost = None

    go_player: GoPlayer     = None
    seek_player: SeekPlayer = None


    ### OPERATIONAL METHODS ###

    def setup(self):
        self.ghost = Ghost(pos=Vector2(650, 125))
        self.add(self.ghost)

        self.go_player = GoPlayer(pos=Vector2(200, 175))
        self.add(self.go_player)

        self.seek_player = SeekPlayer(move_speed=10, pos=Vector2(300, 150))
        self.seek_player.set_lamp_post(Vector2(400, -10))
        self.add(self.seek_player)

    
    def update(self, dt: float):
        self.ghost.move(Vector2(-5, 0.0))
        self.update_world(dt)
