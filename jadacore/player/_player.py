#################################
# _player.py     [v0.0.1-alpha] #
#===============================#
#                               #
#-------------------------------#
# J Karstin Neill    06.03.2022 #
#################################


### IMPORTS ###

from pathlib import Path
from pygame import Vector2
from pygame.sprite import Group

from jadacore.being import (
    Doing,
    KeyInput, MouseInput,
    Driver, KeyDriver, Seeker, ClickSeeker,
    ItemBeing, Item, Inventory,
)


### CLASS STUB ###

class Player(Doing):
    def __init__(self,
        interact_group: Group,
        icon_group: Group,
        sprite_sheet_path: Path,
        driver: Driver=None,
        reach: float=None,
        **kwargs
    ): ...
class KeyPlayer(Player):
    def __init__(self,
        interact_group: Group,
        icon_group: Group,
        sprite_sheet_path: Path,
        move_speed: float=None,
        **kwargs
    ): ...
class SeekPlayer(Player):
    def __init__(self,
        interact_group: Group,
        icon_group: Group,
        sprite_sheet_path: Path,
        move_speed: float=None,
        **kwargs
    ): ...
class ClickPlayer(SeekPlayer):
    def __init__(self,
        interact_group: Group,
        icon_group: Group,
        sprite_sheet_path: Path,
        move_speed: float=None,
        **kwargs
    ): ...

class Player(Doing):
    inventory: Inventory
    key_input: KeyInput
    driver: Driver
    def __init__(self,
        interact_group: Group,
        icon_group: Group,
        sprite_sheet_path: Path,
        driver: Driver=None,
        reach: float=None,
        **kwargs
    ): ...
    def pick_up(self, item_being: ItemBeing=None) -> float: ...
    def add_item(self, item: Item=None) -> float: ...
class KeyPlayer(Player):
    driver: KeyDriver
    def __init__(self,
        interact_group: Group,
        icon_group: Group,
        sprite_sheet_path: Path,
        move_speed: float=None,
        **kwargs
    ): ...
class SeekPlayer(Player):
    driver: Seeker
    def __init__(self,
        interact_group: Group,
        icon_group: Group,
        sprite_sheet_path: Path,
        move_speed: float=None,
        **kwargs
    ): ...
    def set_lamp_post(self, lamp_post: Vector2=None): ...
class ClickPlayer(SeekPlayer):
    driver: ClickSeeker
    mouse_input: MouseInput
    def __init__(self,
        interact_group: Group,
        icon_group: Group,
        sprite_sheet_path: Path,
        move_speed: float=None,
        **kwargs
    ): ...


### CLASS DEFINITIONS ###

class Player(Doing):
    """
    Description:
    ------------
    Doing subclass designed to integrate Driver and Inventory alongside inherited
    Animator and Motor Components to provide a base for user input and world interaction.

    Note: Driver is not usually assigned in this class as it is primarily a base to extend from
    for more specialized behaviors. A driver can be passed to the constructor, but this is
    more a convenience for custom designs, and in general subclassing is better.

    Constructor:
    ------------
    Player(sprite_sheet_path: Path, driver: Driver=None, **kwargs) -> <Player>
    """

    ### FIELDS ###

    inventory: Inventory   = None
    key_input: KeyInput    = None
    driver: Driver         = None


    ### CONSTRUCTOR ###

    def __init__(self,
        interact_group: Group,
        icon_group: Group,
        sprite_sheet_path: Path,
        driver: Driver=None,
        reach: float=None,
        **kwargs
    ) -> None:
        """
        Usage:
        ------
        Player(sprite_sheet_path: Path, driver: Driver=None, **kwargs) -> <Player>

        Description:
        ------------
        Constructor for Player Doing subclass.

        Arguments:
        ----------
        - interact_group: Group             - Group of ItemBeing instances which Interactor will interact with.
        - icon_group: Group                 - Group to which icon images should be drawn for Interactor.
        - sprite_sheet_path: Path [::Doing] - Path to sprite sheet, which is set up in Doing superclass.
        - driver: Driver=None               - Convenience argument for assigning a Driver upon creation. Almost always better to leave as None and assign within a subclass.
        - reach: float=None                 - Radius distance from Player pos within which interactions can occur.
        - cue_icon_path: Path=None          - Path to cue icon image which will appear near interactable ItemBeings.
        - interact_key: int=None            - Integer keycode representing the key used in Interactor interactions.
        - **kwargs:
            - sprite_sheet_dims: Vector2=None [::Doing] - 
            - frames_per_second: float=None   [::Doing] - 
            - animation_style: int=None       [::Doing] - 
            - default_anim_name: str=None     [::Doing] - 
            - pos: Vector2=None               [::Being] - 
            - size: Vector2=None              [::Being] - 
            - color: Color=None               [::Being] - 
            - image_path: Path=None           [::Being] - 
            - groups: list[Group]=None        [::Being] - 
        
        Returns:
        --------
        - <Player> - Instance of Player class.
        """
        Doing.__init__(self,
            sprite_sheet_path,
            **kwargs
        )

        self.key_input = KeyInput('key_input')
        self.attach(self.key_input)

        self.inventory = Inventory('inventory',
            interact_group, icon_group,
            reach=reach, key_input=self.key_input
        )
        self.attach(self.inventory)

        if driver:
            self.driver = driver
            self.driver.set_motor(self.motor)
            self.attach(self.driver)

    
    ### OPERATIONAL METHODS ###

    def pick_up(self, item_being: ItemBeing=None) -> float:
        if item_being:
            return self.add_item(item_being.item)
        
        return self.inventory.space_used


    ### WRAPPING METHODS ###

    def add_item(self, item: Item=None) -> float:
        """
        Usage:
        ------
        <Player>.add_item(item: Item=None) -> float

        Description:
        ------------
        Wraps <Inventory>.add_item(...) method used to add Item to Player Inventory.

        Arguments:
        ----------
        - item: Item=None - Item instance to add to Player Inventory.

        Returns:
        --------
        - space_used: float - Amount of space currently being used in Player Inventory after trying to add the Item.
        """
        return self.inventory.add_item(item)



class KeyPlayer(Player):
    """
    Description:
    ------------

    Constructor:
    ------------
    
    """

    ### FIELDS ###

    driver: KeyDriver = None


    ### CONSTRUCTOR ###

    def __init__(self,
        interact_group: Group,
        icon_group: Group,
        sprite_sheet_path: Path,
        move_speed: float=None,
        **kwargs
    ):
        Player.__init__(self,
            interact_group, icon_group, sprite_sheet_path,
            **kwargs
        )

        self.driver = KeyDriver(
            'key_driver',
            motor=self.motor, move_speed=move_speed
        )
        self.attach(self.driver)



class SeekPlayer(Player):
    """
    Description:
    ------------

    Constructor:
    ------------

    """

    ### FIELDS ###

    driver: Seeker = None


    ### CONSTRUCTOR ###

    def __init__(self,
        interact_group: Group,
        icon_group: Group,
        sprite_sheet_path: Path,
        move_speed: float=None,
        **kwargs
    ):
        Player.__init__(self,
            interact_group, icon_group, sprite_sheet_path,
            **kwargs
        )

        self.driver = Seeker(
            'seeker',
            motor=self.motor, move_speed=move_speed
        )
        self.attach(self.driver)
    

    ### WRAPPING METHODS ###

    def set_lamp_post(self, lamp_post: Vector2=None) -> None:
        self.driver.set_lamp_post(lamp_post)



class ClickPlayer(SeekPlayer):

    ### FIELDS ###

    driver: ClickSeeker     = None
    mouse_input: MouseInput = None


    ### CONSTRUCTORS ###

    def __init__(self,
        interact_group: Group,
        icon_group: Group,
        sprite_sheet_path: Path,
        move_speed: float=None,
        **kwargs
    ):
        SeekPlayer.__init__(self,
            interact_group, icon_group, sprite_sheet_path,
            **kwargs
        )

        self.mouse_input = MouseInput('mouse_input')
        self.attach(self.mouse_input)

        self.driver = ClickSeeker(
            'click_seeker', self.mouse_input,
            motor=self.motor, move_speed=move_speed
        )
        self.attach(self.driver)
    