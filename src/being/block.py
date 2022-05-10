#################################
# block.py       [v0.0.1-alpha] #
#===============================#
#                               #
#-------------------------------#
# J Karstin Neill    05.09.2022 #
#################################


### IMPORTS ###

from pathlib import Path
from pygame import Color, Vector2

from . import Being


### CLASS DEFINITIONS ###

class Block(Being):

    ### CONSTRUCTOR ###

    def __init__(
        self,
        pos: Vector2=None,
        size: Vector2=None,
        color: Color=None,
        image_path: Path=None,
        *args,
        **kwargs
    ) -> None:
        Being.__init__(self, pos, size, color, image_path, *args, **kwargs)
    

    ### OPERATIONAL METHODS ###

    def update(self, dt: float) -> None:
        super().update(dt)
