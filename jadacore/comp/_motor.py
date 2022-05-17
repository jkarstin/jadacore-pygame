#################################
# _motor.py      [v0.0.1-alpha] #
#===============================#
#                               #
#-------------------------------#
# J Karstin Neill    05.17.2022 #
#################################


### IMPORTS ###

from pygame import Vector2

from jadacore.being import Component
from jadacore.meta import PIXEL_SIZE


### CONSTANTS & FLAGS ###

# ::StepMotor
DEFAULT_STEP_SIZE: int       = 1
DEFAULT_MIN_STEP_TIME: float = 0.35


### CLASS DEFINITIONS ###

class Motor(Component):

    ### FIELDS ###

    move_vect: Vector2 = None


    ### COMPONENT METHODS ###

    def update(self, dt: float):
        if self.being:
            if self.move_vect:
                self.being.pos.x += self.move_vect.x * PIXEL_SIZE * dt
                self.being.pos.y += self.move_vect.y * PIXEL_SIZE * dt
                self.move_vect = None
            
            self.being.rect.x = int(self.being.pos.x / PIXEL_SIZE) * PIXEL_SIZE
            self.being.rect.y = int(self.being.pos.y / PIXEL_SIZE) * PIXEL_SIZE

    
    ### OPERATIONAL METHODS ###

    def move(self, move_vect: Vector2):
        self.move_vect = move_vect



class StepMotor(Motor):

    ### FEILDS ###

    step_size:       int = None
    min_step_time: float = None


    ### CONSTRUCTOR ###

    def __init__(self, name: str, step_size: int=None, steps_per_second: float=None):
        Motor.__init__(self, name)

        self.step_size = step_size if step_size and step_size > 0 else DEFAULT_STEP_SIZE

        if steps_per_second and steps_per_second > 0.0:
            self.min_step_time = 1.0 / steps_per_second
        if not (self.min_step_time and self.min_step_time > 0.0):
            self.min_step_time = DEFAULT_MIN_STEP_TIME


    ### COMPONENT METHODS ###

    def update(self, dt: float):
        if self.being:
            pixel_step: int = PIXEL_SIZE * self.step_size

            if self.move_vect:
                self.being.pos.x += self.move_vect.x * pixel_step * dt / self.min_step_time
                self.being.pos.y += self.move_vect.y * pixel_step * dt / self.min_step_time
                self.move_vect = None
            
            self.being.rect.x = int(self.being.pos.x / pixel_step) * pixel_step
            self.being.rect.y = int(self.being.pos.y / pixel_step) * pixel_step


    ### WRAPPER METHODS ###

    def move(self, dir_vect: Vector2):
        super().move(dir_vect.normalize())
