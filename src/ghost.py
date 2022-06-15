#################################
# ghost.py       [v0.0.2-alpha] #
#===============================#
#                               #
#-------------------------------#
# J Karstin Neill    06.14.2022 #
#################################


### IMPORTS ###

from pygame import Vector2

from jadacore.doing import Doing


### CLASS DEFINITIONS ###

class Ghost(Doing):

    ### CONSTRUCTOR ###

    def __init__(self, **kwargs):
        Doing.__init__(self,
            'ghosti.ss.png',
            sprite_sheet_dims=Vector2(2, 2),
            frames_per_second=1.7,
            default_anim_name='float',
            **kwargs
        )
