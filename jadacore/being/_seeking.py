#################################
# _seeking.py    [v0.0.1-alpha] #
#===============================#
#                               #
#-------------------------------#
# J Karstin Neill    05.31.2022 #
#################################


### IMPORTS ###

from pygame import Vector2

from . import Seeker, Doing


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
        self.attach(self.driver)

    
    ### WRAPPER METHODS ###

    def set_lamp_post(self, lamp_post: Vector2=None):
        self.driver.set_lamp_post(lamp_post)
