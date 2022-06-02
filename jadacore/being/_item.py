#################################
# _item.py       [v0.0.1-alpha] #
#===============================#
#                               #
#-------------------------------#
# J Karstin Neill    06.01.2022 #
#################################


### IMPORTS ###

from pathlib import Path
import re

import jadacore.util.log as log

from . import InteractBeing, Interaction, Interactor


### CLASS STUBS ###

class ItemBeing(InteractBeing):
    def __init__(self,
        sprite_sheet_path: Path,
        name: str,        
        space: float=None,
        **kwargs
    ): ...
class Item(Interaction):
    def __init__(self,
        name: str,
        space: float=None,
        **kwargs
    ): ...
class Inventory(Interactor):
    def __init__(self,
        name: str,
        space_max: float=None,
        **kwargs
    ): ...


### CONSTANTS & FLAGS ###

# ::Item
DEFAULT_SPACE: float = 0.0

# ::Inventory
DEFAULT_SPACE_MAX: float = 50.0


### CLASS DEFINITIONS ###

class ItemBeing(InteractBeing):

    ### FIELDS ###

    item: Item = None


    ### CONSTRUCTOR ###

    def __init__(self,
        sprite_sheet_path: Path,
        name: str,        
        space: float=None,
        icon_path: Path=None,
        interact_key: int=None,
        **kwargs
    ):
        InteractBeing.__init__(self, sprite_sheet_path, **kwargs)

        self.item = Item(name, space, icon_path=icon_path, interact_key=interact_key)
        self.interaction = self.item
        self.attach(self.item)
    

    def interact(self,
        interactor: Interactor
    ) -> bool:
        if interactor:
            log.sprint(f"ItemBeing '{self.item.name}' interacted with by: {interactor}")

            if isinstance(interactor, Inventory):
                inventory: Inventory = interactor
                self.remove(self.groups())
                inventory.add_item(self.item)

            return True

        return False



class Item(Interaction):
    """
    Description:
    ------------
    Component subclass designed to allow the attached Being to
    be usable in an Inventory.

    Constructor:
    ------------
    Item(name: str, space: float=None, icon_path: Path=None) -> <Item>
    """

    ### FIELDS ###

    space: float  = None


    ### CONSTRUCTOR ###

    def __init__(self,
        name: str,
        space: float=None,
        **kwargs
    ):
        """
        Usage:
        ------
        Item(name: str, space: float=None, icon_path: Path=None) -> <Item>

        Description:
        ------------
        Constructor for Item Component subclass.

        Arguments:
        ----------
        - name: str - Component name. [::Component]
        - space: float=None - Amount of space Item takes up in Inventory.
        - icon_path: Path=None - Path to icon image in resources to
        use as Item image when viewed in Inventory.

        Returns:
        --------
        - <Item> - Instance of Item class.
        """
        Interaction.__init__(self, name, **kwargs)

        self.space = space if space else DEFAULT_SPACE



class Inventory(Interactor):
    """
    Description:
    ------------
    Component subclass designed to store and utilitize Item objects.

    Constructor:
    ------------
    Inventory(name: str, space_max: float=None) -> <Inventory>
    """

    ### FIELDS ###

    items: dict[str, list[Item]] = None
    space_used: float            = None
    space_max: float             = None


    ### CONSTRUCTOR ###

    def __init__(self,
        name: str,
        space_max: float=None,
        **kwargs
    ):
        """
        Usage:
        ------
        Inventory(name: str, space_max: float=None) -> <Inventory>

        Description:
        ------------
        Constructor for Inventory Component subclass.

        Arguments:
        ----------
        - name: str - Component name. [::Component]
        - space_max: float=None - Maximum capacity limit for Inventory.

        Returns:
        --------
        - <Inventory> - Instance of Inventory class.
        """
        Interactor.__init__(self, name, **kwargs)

        self.items = {}
        self.space_used = 0.0
        self.space_max = space_max if space_max else DEFAULT_SPACE_MAX

    
    ### OPERATIONAL METHODS ###

    def add_item(self, item: Item=None) -> float:
        """
        Usage:
        ------
        <Inventory>.add_item(item: Item=None) -> float

        Description:
        ------------
        Used to add a new Item instance to the Inventory.

        Arguments:
        ----------
        - item: Item=None - Item instance to add to Inventory.

        Returns:
        --------
        - space_used: float - Amount of space currently being used in the Inventory after trying to add the Item.
        """
        if item and self.space_free() >= item.space:
            if item.name in self.items:
                self.items[item.name].append(item)
            else:
                self.items[item.name] = [item]
            self.space_used += item.space
        
        return self.space_used

    
    def has_item(self, item_name: str=None) -> bool:
        """
        Usage:
        ------
        <Inventory>.has_item(item_name: str=None) -> bool

        Description:
        ------------
        Used to see if an Item with the given name is in the Inventory.

        Arguments:
        ----------
        - item_name: str=None - Name of Item to find.

        Returns:
        --------
        - has_item: bool - True if Item with name is in Inventory; False if no Item with given name was found.
        
        """
        return item_name and item_name in self.items

    
    def how_many(self, item_name: str=None) -> int:
        """
        Usage:
        ------
        <Inventory>.how_many(item_name: str=None) -> int

        Description:
        ------------
        Used to see how many instances of the Item with the given name exist in Inventory.

        Arguments:
        ----------
        - item_name: str=None - Name of Item to search for in Inventory.

        Returns:
        --------
        - count: int - Integer count of Items associated with given name; will be 0 [zero] if no Items found.
        """
        if self.has_item(item_name):
            return len(self.items[item_name])

        return 0

    
    def space_free(self) -> float:
        """
        Usage:
        ------
        <Inventory>.space_free() -> float

        Description:
        ------------
        Used to check how much space is available for more Items to be added.

        Arguments:
        ----------
        [None]

        Returns:
        --------
        - space_free: float - Amount of space remaining before maximum space limit is reached.
        
        """
        return self.space_max - self.space_used

    
    def remove_item(self, item_name: str=None) -> tuple[Item, float]:
        """
        Usage:
        ------
        <Inventory>.remove_item(item_name: str=None) -> (Item|None, float)

        Description:
        ------------
        Removes a single Item instance from the Inventory by looking for an Item with the given name.

        Arguments:
        ----------
        - item_name: str=None - Name of the Item that should be removed.

        Returns:
        --------
        - (removed_item: Item|None, space_used: float)
            - removed_item: Item - Item instance removed from the Inventory; None if no Item was found with given name.
            - space_used: float - Amount of space currently being used in the Inventory after trying to remove the Item.
        
        """
        removed_item: Item = None

        if self.has_item(item_name):
            items_list = self.items.pop(item_name)
            removed_item = items_list.pop(-1)
            self.space_used -= removed_item.space

            if len(items_list) > 0:
                self.items[item_name] = items_list

        return removed_item, self.space_used

    
    def dump_out(self, item_name_pattern: str=None) -> tuple[dict[str, list[Item]], float]:
        """
        Usage:
        ------
        <Inventory>.dump_out(item_name_pattern: str=None) -> ({str: [Item, ...], ...}|None, float)

        Description:
        ------------
        Dumps out (removes and returns) the contents of the Inventory en-masse, either by removing
        every Item and setting it to empty (default), or by looking for any Items with a name that
        matches the given name pattern string (using regex matching).

        Arguments:
        ----------
        - item_name_pattern: str=None - Regex pattern to match against Item names in a search;
        Leave empty or as None to match all Items.

        Returns:
        --------
        - (dump_items: {str: [Item, ...], ...}|None, space_used: float)
            - dump_items: dict[str, list[Item]]|None - Dictionary of Item lists aggregated by name
            which were removed from the Inventory; None if no Items were removed.
            - space_used: float - Amount of space currently being used in the Inventory after trying to remove the Items.
        """
        dump_items: dict[str, list[Item]] = None

        if not item_name_pattern:
            dump_items: dict[str, list[Item]] = self.items

            self.items = {}
            self.space_used = 0.0
        else:
            dump_items = {}

            for item_name in self.items:
                if re.search(item_name_pattern, item_name):
                    dump_items[item_name] = self.items[item_name]

                    while True:
                        item, _ = self.remove_item(item_name)
                        if not item: break

        return dump_items, self.space_used
