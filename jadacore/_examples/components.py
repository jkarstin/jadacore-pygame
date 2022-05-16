#################################
# components.py                 #
#===============================#
#                               #
#-------------------------------#
# J Karstin Neill    05.13.2022 #
#################################


### IMPORTS ###

from jadacore.being import Being
from jadacore.comp import Motor, KeyDriver
from jadacore.game import Game, World


### CLASS DEFINITIONS ###

class SimpleWorld(World):

    ### FIELDS ###

    custom_being: Being      = None
    custom_motor: Motor      = None
    custom_driver: KeyDriver = None


    ### WORLD METHODS ###

    def setup(self) -> None:
        self.custom_being = Being()
        self.custom_motor = Motor('motor')
        self.custom_driver = KeyDriver('key_driver', self.custom_motor)
        self.custom_being.attach_component(self.custom_motor)
        self.custom_being.attach_component(self.custom_driver)
        self.add(self.custom_being)


    def update(self, dt: float) -> None:
        super().update_world(dt)


### MAIN FUNCTION DEFINITION ###

def main():
    game: Game = Game()
    game.set_world(SimpleWorld())
    game.run()


### MAIN FUNCTION EXECUTION ###

if __name__ == '__main__':
    main()
