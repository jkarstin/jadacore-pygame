#################################
# doing.py       [v0.0.1-alpha] #
#===============================#
#                               #
#-------------------------------#
# J Karstin Neill    05.11.2022 #
#################################


### IMPORTS ###

from pathlib import Path
from pygame import Vector2

from . import Being, Animation, Motor


### CONSTANTS & FLAGS ###

DEFAULT_ANIM_NAME: str = 'anim_default'


### CLASS DEFINITIONS ###

class Doing(Being):

    ### FIELDS ###

    motor: Motor = None

    animations: dict[str, Animation] = None
    current_animation: Animation     = None
    current_anim_name: str           = None


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

        self.animations = {}
        self.animations['default'] = Animation(
            (default_anim_name if default_anim_name else DEFAULT_ANIM_NAME),
            sprite_sheet_path,
            sprite_sheet_dims,
            frames_per_second,
            animation_style
        )
        self.current_anim_name = default_anim_name if default_anim_name else 'default'
        if self.current_anim_name not in self.animations:
            self.animations[self.current_anim_name] = self.animations['default']
        self.current_animation = self.animations[self.current_anim_name]

        self.attach_component(self.current_animation)
        self.rect.w = self.current_animation.frame_size.x
        self.rect.h = self.current_animation.frame_size.y

        self.current_animation.start()


    ### OPERATIONAL METHODS ###

    def update(self, dt: float) -> None:
        self.current_animation = self.animations[self.current_anim_name]
        self.attach_component(self.current_animation)
        super().update(dt)


    def move(self, move_vect: Vector2) -> None:
        self.motor.move(move_vect)


    ### AUXILIARY METHODS ###

    def add_animation(self,
        animation_name: str,
        sprite_sheet_path: Path,
        sprite_sheet_dims: Vector2,
        frames_per_second: float,
        animation_style: int
    ) -> Animation:
        if not animation_name:
            return None

        self.animations[animation_name] = Animation(
            sprite_sheet_path,
            sprite_sheet_dims,
            frames_per_second,
            animation_style
        )

        return self.animations[animation_name]
        
    
    def set_animation(self, animation_name: str) -> Animation:
        if not animation_name or animation_name not in self.animations:
            return None

        self.current_anim_name = animation_name
        self.update(0)
        return self.current_animation
