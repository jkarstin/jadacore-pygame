#################################
# _item.py       [v0.0.1-alpha] #
#===============================#
#                               #
#-------------------------------#
# J Karstin Neill    05.31.2022 #
#################################


### IMPORTS ###

from pathlib import Path

from jadacore.comp import Item
from . import Doing

class ItemBeing(Doing):

    ### FIELDS ###

    item: Item = None


    ### CONSTRUCTOR ###

    def __init__(self,
        sprite_sheet_path: Path,
        name: str,        
        space: float=None,
        icon_path: Path=None,
        **kwargs
    ):
        Doing.__init__(self, sprite_sheet_path, **kwargs)

        self.item = Item(name, space, icon_path)
        self.attach(self.item)
