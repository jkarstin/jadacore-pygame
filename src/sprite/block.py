#################################
# block.py       [v0.0.1-alpha] #
#===============================#
#                               #
#-------------------------------#
# J Karstin Neill    05.06.2022 #
#################################


### IMPORTS ###

from pathlib import Path
from pygame import Color, Vector2

from . import Being


### CLASS DEFINITIONS ###

class Block(Being):

    ### FIELDS ###


    ### CONSTRUCTOR ###

    def __init__(
        self,
        pos: Vector2=None,
        size: Vector2=None,
        color: Color=None,
        image_path: Path=None,
        **kwargs
    ) -> None:
        Being.__init__(self, pos, size, color, image_path, **kwargs)
    

    ### OPERATIONAL METHODS ###

    def update(self, dt: float) -> None:
        super().update(dt)
