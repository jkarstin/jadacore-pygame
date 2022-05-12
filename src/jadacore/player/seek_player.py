####################################
# seek_player.py    [v0.0.1-alpha] #
#==================================#
#                                  #
#----------------------------------#
# J Karstin Neill       05.12.2022 #
####################################


### IMPORTS ###

from pygame import Vector2

from jadacore.being import Seeking


### CLASS DEFINITIONS ###

class SeekPlayer(Seeking):

    ### CONSTRUCTOR ###

    def __init__(self, **kwargs) -> None:
        Seeking.__init__(self,
            sprite_sheet_path='ghosti.ss.png',
            sprite_sheet_dims=Vector2(2, 2),
            default_anim_name='float',
            **kwargs
        )
        