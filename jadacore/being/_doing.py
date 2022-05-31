#################################
# _doing.py      [v0.0.1-alpha] #
#===============================#
#                               #
#-------------------------------#
# J Karstin Neill    05.31.2022 #
#################################


### IMPORTS ###

from pathlib import Path
from pygame import Vector2

from . import Being, Animator, Animation, Motor


### CLASS DEFINITIONS ###

class Doing(Being):
    """
    Description:
    ------------

    """

    ### FIELDS ###

    motor: Motor = None
    animator: Animator = None


    ### CONSTRUCTOR ###

    def __init__(self,
        sprite_sheet_path: Path,
        sprite_sheet_dims: Vector2=None,
        frames_per_second: float=None,
        animation_style: int=None,
        default_anim_name: str=None,
        **kwargs
    ) -> None:
        """
        Usage:
        ------
        Doing(sprite_sheet_path: Path, sprite_sheet_dims: Vector2=None, frames_per_second: float=None, animation_style: int=None, default_anim_name: str=None, **kwargs)

        Description:
        ------------
        Constructor for Doing class

        Arguments:
        ----------
        - sprite_sheet_path: Path
        - sprite_sheet_dims: Vector2=None
        - frames_per_second: float=None
        - animation_style: int=None
        - default_anim_name: str=None
        - **kwargs:
            - pos: Vector2=None        [::Being]
            - size: Vector2=None       [::Being]
            - color: Color=None        [::Being]
            - image_path: Path=None    [::Being]
            - groups: list[Group]=None [::Being]
        
        Returns:
        --------
        - instance of Doing class
        """
        Being.__init__(self, **kwargs)

        self.motor = Motor('motor')
        self.attach(self.motor)

        self.animator = Animator(
            'animator',
            sprite_sheet_path,
            sprite_sheet_dims,
            frames_per_second,
            animation_style,
            default_anim_name
        )
        self.attach(self.animator)

        self.animator.start()


    ### WRAPPING METHODS ###

    def move(self, move_vect: Vector2) -> None:
        """
        Usage:
        ------


        Description:
        ------------


        Arguments:
        ----------
        

        Returns:
        --------

        """
        self.motor.move(move_vect)
        

    def add_animation(self,
        anim_name: str,
        sprite_sheet_path: Path,
        **kwargs
    ) -> Animation:
        """
        Usage:
        ------
        

        Description:
        ------------


        Arguments:
        ----------
        

        Returns:
        --------

        """
        return self.animator.add_animation(
            anim_name,
            sprite_sheet_path,
            **kwargs
        )
        
    
    def set_animation(self, anim_name: str) -> Animation:
        """
        Usage:
        ------
        

        Description:
        ------------


        Arguments:
        ----------
        

        Returns:
        --------

        """
        return self.animator.set_animation(anim_name)

