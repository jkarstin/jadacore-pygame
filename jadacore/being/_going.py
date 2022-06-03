#################################
# _going.py      [v0.0.1-alpha] #
#===============================#
#                               #
#-------------------------------#
# J Karstin Neill    06.03.2022 #
#################################


### IMPORTS ###

from pygame import Vector2

from . import Doing, KeyDriver, Seeker


### CLASS STUBS ###




### CLASS DEFINITIONS ###

class Going(Doing):

    ### FIELDS ###

    driver: KeyDriver = None


    ### CONSTRUCTOR ###

    def __init__(self,
        up_keys: list[int]=None,
        down_keys: list[int]=None,
        left_keys: list[int]=None,
        right_keys: list[int]=None,
        move_speed: float=None,
        **kwargs
    ) -> None:
        Doing.__init__(self, **kwargs)

        self.driver = KeyDriver(
            'key_driver',
            self.motor,
            up_keys,
            down_keys,
            left_keys,
            right_keys,
            move_speed=move_speed
        )
        self.attach(self.driver)



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
