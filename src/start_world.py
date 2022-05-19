####################################
# start_world.py    [v0.0.1-alpha] #
#==================================#
#                                  #
#----------------------------------#
# J Karstin Neill       05.18.2022 #
####################################


### IMPORTS ###

from pygame import Vector2

from jadacore.being  import ItemBeing
from jadacore.game   import World
from jadacore.player import KeyPlayer, SeekPlayer

from ghost import Ghost


### CLASS DEFINITIONS ###

class StartWorld(World):

    ### FIELDS ###

    key_item: ItemBeing     = None
    ghost: Ghost            = None
    seek_player: SeekPlayer = None
    key_player: KeyPlayer   = None


    ### OPERATIONAL METHODS ###

    def setup(self):
        self.key_item = ItemBeing('key.png', 'key_item', 0.0, icon_path='key.png', pos=Vector2(100, 100))
        self.ghost = Ghost(pos=Vector2(650, 125))
        self.seek_player = SeekPlayer(self.interact_group, self.icon_group, 'ghosti.ss.png', move_speed=10.0, cue_icon_path='cue_icon.png', sprite_sheet_dims=Vector2(2), pos=Vector2(300, 150))
        self.seek_player.set_lamp_post(Vector2(400, -10))
        self.key_player = KeyPlayer(self.interact_group, self.icon_group, 'ghosti.ss.png', cue_icon_path='cue_icon.png', sprite_sheet_dims=Vector2(2), pos=Vector2(200, 175))

        self.add(self.key_item, self.ghost, self.seek_player, self.key_player)

    
    def update(self, dt: float):
        self.ghost.move(Vector2(-5, 0.0))
        self.update_world(dt)
