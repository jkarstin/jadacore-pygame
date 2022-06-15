####################################
# start_world.py    [v0.0.2-alpha] #
#==================================#
#                                  #
#----------------------------------#
# J Karstin Neill       06.14.2022 #
####################################


### IMPORTS ###

from pygame import Vector2

from jadacore.game   import World
from jadacore.item  import ItemBeing
from jadacore.player import ClickPlayer

from ghost import Ghost


### CLASS DEFINITIONS ###

class StartWorld(World):

    ### FIELDS ###

    key_item: ItemBeing       = None
    ghost: Ghost              = None
    click_player: ClickPlayer = None


    ### OPERATIONAL METHODS ###

    def setup(self):
        self.key_item = ItemBeing(
            'key.png', 'key-item', 0.0, 'cue_icon.png',
            pos=Vector2(100, 100)
        )
        
        self.ghost = Ghost(
            pos=Vector2(650, 125)
        )
        
        self.click_player = ClickPlayer(
            self.interact_group, self.icon_group, 'ghosti.ss.png', 10.0,
            sprite_sheet_dims=Vector2(2), pos=Vector2(300, 150)
        )

        self.add(
            self.key_item,
            self.ghost,
            self.click_player
        )

    
    def update(self, dt: float):
        self.ghost.move(Vector2(-5, 0.0))
        super().update(dt)
