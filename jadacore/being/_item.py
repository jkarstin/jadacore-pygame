#################################
# _item.py       [v0.0.1-alpha] #
#===============================#
#                               #
#-------------------------------#
# J Karstin Neill    05.17.2022 #
#################################


### IMPORTS ###

from pathlib import Path

from jadacore.comp import Item
from . import Being

class ItemBeing(Being):

    ### FIELDS ###

    item: Item = None


    ### CONSTRUCTOR ###

    def __init__(self,
        name: str,
        space: float=None,
        icon_path: Path=None,
        **kwargs
    ):
        Being.__init__(self, **kwargs)

        self.item = Item(name, space, icon_path)
        self.attach_component(self.item)
