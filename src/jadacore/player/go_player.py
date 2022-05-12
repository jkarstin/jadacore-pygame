##################################
# go_player.py    [v0.0.1-alpha] #
#================================#
#                                #
#--------------------------------#
# J Karstin Neill     05.11.2022 #
##################################


### IMPORTS ###

from pygame import Vector2

from jadacore.being import Going


### CONSTANTS & FLAGS ###


### CLASS DEFINITIONS ###

class GoPlayer(Going):

    ### FIELDS ###


    ### CONSTRUCTOR ###

    def __init__(self, **kwargs) -> None:
        Going.__init__(self,
            move_speed=15,
            sprite_sheet_path='ghosti.ss.png',
            sprite_sheet_dims=Vector2(2, 2),
            default_anim_name='float',
            **kwargs
        )


    ### OPERATIONAL METHODS ###

    def update(self, dt: float) -> None:
        super().update(dt)
