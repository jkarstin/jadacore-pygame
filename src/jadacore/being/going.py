#################################
# going.py       [v0.0.1-alpha] #
#===============================#
#                               #
#-------------------------------#
# J Karstin Neill    05.10.2022 #
#################################


### IMPORTS ###

from pygame import Vector2

from . import Doing


### CONSTANTS & FLAGS ###


### CLASS DEFINITIONS ###

class Going(Doing):

    ### FIELDS ###


    ### CONSTRUCTOR ###

    def __init__(
        self,
        **kwargs
    ) -> None:
        Doing.__init__(self, **kwargs)


    ### METHODS ###

    def update(self, dt: float) -> None:
        super().update(dt)
        
