#################################
# doing.py       [v0.0.1-alpha] #
#===============================#
#                               #
#-------------------------------#
# J Karstin Neill    05.12.2022 #
#################################


### IMPORTS ###

from pathlib import Path
from pygame import Vector2

from . import Being, Animator, Animation, Motor


### CLASS DEFINITIONS ###

class Doing(Being):

    ### FIELDS ###

    motor: Motor = None
    animator: Animator = None


    ### CONSTRUCTOR ###

    def __init__(self,
        sprite_sheet_path: Path,
        sprite_sheet_dims: Vector2=Vector2(1),
        frames_per_second: float=2,
        animation_style: int=Animation.ANIM_STYLE_LOOP,
        default_anim_name: str=None,
        **kwargs
    ) -> None:
        Being.__init__(self, **kwargs)

        self.motor = Motor('motor')
        self.attach_component(self.motor)

        self.animator = Animator(
            'animator',
            sprite_sheet_path,
            sprite_sheet_dims,
            frames_per_second,
            animation_style,
            default_anim_name
        )
        self.attach_component(self.animator)

        self.animator.start()


    ### OPERATIONAL METHODS ###

    def move(self, move_vect: Vector2) -> None:
        self.motor.move(move_vect)


    ### WRAPPING METHODS ###

    def add_animation(self,
        anim_name: str,
        sprite_sheet_path: Path,
        **kwargs
    ) -> Animation:
        return self.animator.add_animation(
            anim_name,
            sprite_sheet_path,
            **kwargs
        )
        
    
    def set_animation(self, anim_name: str) -> Animation:
        return self.animator.set_animation(anim_name)

