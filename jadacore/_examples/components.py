###################################
# components.py    [v0.0.2-alpha] #
#=================================#
#                                 #
#---------------------------------#
# J Karstin Neill      06.14.2022 #
###################################


### IMPORTS ###

from jadacore.being import Being
from jadacore.going import KeyDriver
from jadacore.game import Game, World


### CLASS DEFINITIONS ###

class SimpleWorld(World):

    ### FIELDS ###

    custom_being: Being = None


    ### WORLD METHODS ###

    def setup(self):
        self.custom_being = Being()
        self.custom_being.attach(KeyDriver('key_driver'))

        self.add(self.custom_being)


### MAIN FUNCTION DEFINITION ###

def main():
    game: Game = Game()
    game.set_world(SimpleWorld())
    game.run()


### MAIN FUNCTION EXECUTION ###

if __name__ == '__main__':
    main()
