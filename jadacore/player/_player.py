#################################
# _player.py     [v0.0.1-alpha] #
#===============================#
#                               #
#-------------------------------#
# J Karstin Neill    05.14.2022 #
#################################


### IMPORTS ###

from pathlib import Path
from pygame import Vector2

from jadacore.being import Doing
from jadacore.comp import Driver, KeyDriver, Seeker, Item, Inventory


### CLASS DEFINITIONS ###

class Player(Doing):

    ### FIELDS ###

    driver: Driver       = None
    inventory: Inventory = None


    ### CONSTRUCTOR ###

    def __init__(self,
        sprite_sheet_path: Path,
        **kwargs
    ) -> None:
        """
        Player(sprite_sheet_path: Path, **kwargs)

        Arguments:
        ----------
        - sprite_sheet_path: Path             [::Doing]
        - **kwargs:
            - sprite_sheet_dims: Vector2=None [::Doing]
            - frames_per_second: float=None   [::Doing]
            - animation_style: int=None       [::Doing]
            - default_anim_name: str=None     [::Doing]
            - pos: Vector2=None               [::Being]
            - size: Vector2=None              [::Being]
            - color: Color=None               [::Being]
            - image_path: Path=None           [::Being]
            - groups: list[Group]=None        [::Being]
        """
        Doing.__init__(self,
            sprite_sheet_path,
            **kwargs
        )

        self.inventory = Inventory('inventory')
        self.attach_component(self.inventory)

    
    ### WRAPPING METHODS ###

    def add_item(self, item: Item=None) -> float:
        return self.inventory.add_item(item)



class GoPlayer(Player):

    ### FIELDS ###

    driver: KeyDriver = None


    ### CONSTRUCTOR ###

    def __init__(self,
        sprite_sheet_path: Path,
        move_speed: float=None,
        **kwargs
    ) -> None:
        Player.__init__(self,
            sprite_sheet_path,
            **kwargs
        )

        self.driver = KeyDriver(
            'key_driver',
            self.motor,
            move_speed=move_speed
        )
        self.attach_component(self.driver)



class SeekPlayer(Player):

    ### FIELDS ###

    driver: Seeker = None


    ### CONSTRUCTOR ###

    def __init__(self,
        sprite_sheet_path: Path,
        move_speed: float=None,
        **kwargs
    ) -> None:
        Player.__init__(self,
            sprite_sheet_path,
            **kwargs
        )

        self.driver = Seeker(
            'seeker',
            self.motor,
            move_speed=move_speed
        )
        self.attach_component(self.driver)
    

    ### WRAPPING METHODS ###

    def set_lamp_post(self, lamp_post: Vector2=None) -> None:
        self.driver.set_lamp_post(lamp_post)
        