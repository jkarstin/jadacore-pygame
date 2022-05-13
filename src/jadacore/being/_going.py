#################################
# _going.py      [v0.0.1-alpha] #
#===============================#
#                               #
#-------------------------------#
# J Karstin Neill    05.12.2022 #
#################################


### IMPORTS ###

from jadacore.comp import KeyDriver
from . import Doing


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
            up_keys,
            down_keys,
            left_keys,
            right_keys,
            move_speed=move_speed,
            motor=self.motor
        )
        self.attach_component(self.driver)
