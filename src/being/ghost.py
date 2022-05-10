#################################
# ghost.py       [v0.0.1-alpha] #
#===============================#
#                               #
#-------------------------------#
# J Karstin Neill    05.06.2022 #
#################################


### IMPORTS ###

from pathlib import Path
from pygame import Surface, Vector2

from . import Animation, Being


### CONSTANTS & FLAGS ###


### CLASS DEFINITIONS ###

class Ghost(Being):

    ### FIELDS ###

    animation: Animation = None


    ### CONSTRUCTOR ###

    def __init__(
        self,
        ghost_path: Path,
        sprite_sheet_size: Vector2=Vector2(1),
        frames_per_second: float=2,
        animation_style: int=Animation.ANIM_STYLE_LOOP,
        *args,
        **kwargs
    ) -> None:
        Being.__init__(self, *args, **kwargs)

        self.animation = Animation(
            ghost_path,
            sprite_sheet_size,
            frames_per_second,
            animation_style
        )

        self.image = self.animation.get_frame()
        self.rect.w = self.animation.frame_size.x
        self.rect.h = self.animation.frame_size.y

        self.animation.start()


    ### METHODS ###

    def update(self, dt: float) -> None:
        super().update(dt)
        self.image = self.animation.update(dt)
