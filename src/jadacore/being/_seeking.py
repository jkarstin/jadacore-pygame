#################################
# _seeking.py    [v0.0.1-alpha] #
#===============================#
#                               #
#-------------------------------#
# J Karstin Neill    05.12.2022 #
#################################


### IMPORTS ###

from pygame import Vector2

from jadacore.comp import Seeker
from . import Doing


### CLASS DEFINITIONS ###

class Seeking(Doing):

    ### FIELDS ###

    driver: Seeker = None


    ### CONSTRUCTOR ###

    def __init__(self, move_speed: float=None, **kwargs):
        Doing.__init__(self, **kwargs)

        self.driver = Seeker(
            'seeker',
            self.motor,
            move_speed=move_speed
        )
        self.attach_component(self.driver)

    
    ### WRAPPER METHODS ###

    def set_lamp_post(self, lamp_post: Vector2=None):
        self.driver.set_lamp_post(lamp_post)
