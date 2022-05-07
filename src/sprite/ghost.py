#################################
# ghost.py       [v0.0.1-alpha] #
#===============================#
#                               #
#-------------------------------#
# J Karstin Neill    05.06.2022 #
#################################


### IMPORTS ###

from pathlib import Path
from pygame import Color, Vector2

from . import Being


### CONSTANTS & FLAGS ###


### CLASS DEFINITIONS ###

class Ghost(Being):

    ### FIELDS ###


    ### CONSTRUCTOR ###

    def __init__(
        self,
        ghost_path: Path,
        pos: Vector2=None,
        size: Vector2=None,
        color: Color=None,
        **kwargs
    ) -> None:
        Being.__init__(self, pos, size, color, image_path=ghost_path, **kwargs)
    

    ### METHODS ###

    def update(self, dt: float) -> None:
        super().update(dt)
