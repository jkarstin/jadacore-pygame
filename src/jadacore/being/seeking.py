#################################
# seeking.py     [v0.0.1-alpha] #
#===============================#
#                               #
#-------------------------------#
# J Karstin Neill    05.11.2022 #
#################################


### IMPORTS ###

from pygame import Vector2

from jadacore.meta import PIXEL_SIZE, PIXEL_SIZE_SQUARED

from . import Doing


### CONSTANTS & FLAGS ###

DEFAULT_MOVE_SPEED: float = 2.0


### CLASS DEFINITIONS ###

class Seeking(Doing):

    ### FIELDS ###

    move_speed: float      = None

    pix_mv_spd_sqrd: float = None
    lamp_post: Vector2     = None


    ### CONSTRUCTOR ###

    def __init__(self, move_speed: float=None, **kwargs):
        Doing.__init__(self, **kwargs)

        self.move_speed      = move_speed if move_speed else DEFAULT_MOVE_SPEED
        self.pix_mv_spd_sqrd = self.move_speed * self.move_speed * PIXEL_SIZE_SQUARED


    ### OPERATIONAL METHODS ###

    def update(self, dt: float):
        if self.lamp_post:
            delta: Vector2 = self.lamp_post - self.pos

            if delta.length_squared() > self.pix_mv_spd_sqrd * dt * dt:
                # move it closer to lamp_post
                delta.scale_to_length(self.move_speed)
                self.move(delta)
            elif delta.x < PIXEL_SIZE and delta.y < PIXEL_SIZE:
                # arrived at lamp_post
                self.pos = self.lamp_post
                self.lamp_post = None
            else: # delta.length() <= move_speed * PIXEL_SIZE * dt:
                # precision movement to lamp_post (prevent overshooting in high-velocity/low frame-rate instances)
                distance: float = delta.length()
                delta.scale_to_length(distance / (PIXEL_SIZE * dt))
                self.move(delta)

        super().update(dt)

    
    ### AUXILIARY METHODS ###

    def set_lamp_post(self, lamp_post: Vector2=None):
        self.lamp_post = lamp_post
