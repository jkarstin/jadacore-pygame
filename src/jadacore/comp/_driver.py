#################################
# _driver.py     [v0.0.1-alpha] #
#===============================#
#                               #
#-------------------------------#
# J Karstin Neill    05.12.2022 #
#################################


### IMPORTS ###

import pygame
from pygame import Vector2

from jadacore.being import Component
from jadacore.meta import PIXEL_SIZE, PIXEL_SIZE_SQUARED

from . import Motor


### CONSTANTS & FLAGS ###

DEFAULT_KEYS: dict[str, list[int]] = {
    'up_key':    [pygame.K_UP,    pygame.K_w],
    'down_key':  [pygame.K_DOWN,  pygame.K_s],
    'left_key':  [pygame.K_LEFT,  pygame.K_a],
    'right_key': [pygame.K_RIGHT, pygame.K_d]
}
DEFAULT_MOVE_SPEED: float = 10.0


### CLASS DEFINITIONS ###

class Driver(Component):

    ### FIELDS ###

    motor: Motor      = None
    move_speed: float = None

    
    ### CONSTRUCTOR ###

    def __init__(self, name: str, motor: Motor, move_speed: float=None) -> None:
        Component.__init__(self, name)

        self.motor = motor
        self.move_speed = move_speed if move_speed else DEFAULT_MOVE_SPEED


class KeyDriver(Driver):

    ### FIELDS ###

    up_keys: list[int]    = None
    down_keys: list[int]  = None
    left_keys: list[int]  = None
    right_keys: list[int] = None
    keys_held: list[int]  = None


    ### CONSTRUCTOR ###

    def __init__(self,
        name: str,
        motor: Motor,
        up_keys: list[int]=None,
        down_keys: list[int]=None,
        left_keys: list[int]=None,
        right_keys: list[int]=None,
        **kwargs
    ) -> None:
        Driver.__init__(self, name, motor, **kwargs)

        self.up_keys    = up_keys    if up_keys    else DEFAULT_KEYS['up_key']
        self.down_keys  = down_keys  if down_keys  else DEFAULT_KEYS['down_key']
        self.left_keys  = left_keys  if left_keys  else DEFAULT_KEYS['left_key']
        self.right_keys = right_keys if right_keys else DEFAULT_KEYS['right_key']
        self.keys_held  = []


    ### COMPONENT METHODS ###

    def update(self, dt: float) -> None:
        keys_pressed: list[bool] = pygame.key.get_pressed()


        def tickle_keys(keylist: list[int]) -> None:
            for key in keylist:
                if keys_pressed[key]:
                    if key not in self.keys_held:
                        self.keys_held.append(key)
                elif key in self.keys_held:
                    self.keys_held.remove(key)

        tickle_keys(self.up_keys)
        tickle_keys(self.down_keys)
        tickle_keys(self.left_keys)
        tickle_keys(self.right_keys)


        def record_movement(keylist: list[int], delta: Vector2, move_vect: Vector2=None) -> Vector2:
            for key in keylist:
                if key in self.keys_held:
                    if move_vect:
                        move_vect += delta
                    else:
                        move_vect = delta
            return move_vect

        move_vect: Vector2 = None
        move_vect = record_movement(self.up_keys,    Vector2(               0, -self.move_speed), move_vect)
        move_vect = record_movement(self.down_keys,  Vector2(               0,  self.move_speed), move_vect)
        move_vect = record_movement(self.left_keys,  Vector2(-self.move_speed,                0), move_vect)
        move_vect = record_movement(self.right_keys, Vector2( self.move_speed,                0), move_vect)
        self.motor.move(move_vect)



class Seeker(Driver):

    ### FIELDS ###

    pix_mv_spd_sqrd: float = None
    lamp_post: Vector2     = None


    ### CONSTRUCTOR ###

    def __init__(self, name: str, motor: Motor, **kwargs):
        Driver.__init__(self, name, motor, **kwargs)

        self.pix_mv_spd_sqrd = self.move_speed * self.move_speed * PIXEL_SIZE_SQUARED


    ### COMPONENT METHODS ###

    def update(self, dt: float) -> None:
        if self.lamp_post:
            delta: Vector2 = self.lamp_post - self.being.pos

            if delta.length_squared() > self.pix_mv_spd_sqrd * dt * dt:
                # move it closer to lamp_post
                delta.scale_to_length(self.move_speed)
                self.motor.move(delta)
            elif delta.x < PIXEL_SIZE and delta.y < PIXEL_SIZE:
                # arrived at lamp_post
                self.being.pos = self.lamp_post
                self.lamp_post = None
            else: # delta.length() <= move_speed * PIXEL_SIZE * dt:
                # precision movement to lamp_post (prevent overshooting in high-velocity/low frame-rate instances)
                distance: float = delta.length()
                delta.scale_to_length(distance / (PIXEL_SIZE * dt))
                self.motor.move(delta)
    

    ### OPERATIONAL METHODS ###

    def set_lamp_post(self, lamp_post: Vector2=None):
        self.lamp_post = lamp_post
