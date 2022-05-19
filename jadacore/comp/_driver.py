#################################
# _driver.py     [v0.0.1-alpha] #
#===============================#
#                               #
#-------------------------------#
# J Karstin Neill    05.18.2022 #
#################################


### IMPORTS ###

import pygame
from pygame import Vector2

from jadacore.being import Component
from jadacore.meta import PIXEL_SIZE, PIXEL_SIZE_SQUARED

from . import Motor, KeyInput


### CONSTANTS & FLAGS ###

# ::Driver
DEFAULT_MOVE_SPEED: float = 10.0

# ::KeyDriver
DEFAULT_KEYS: dict[str, list[int]] = {
    'up_key':    [pygame.K_UP,    pygame.K_w],
    'down_key':  [pygame.K_DOWN,  pygame.K_s],
    'left_key':  [pygame.K_LEFT,  pygame.K_a],
    'right_key': [pygame.K_RIGHT, pygame.K_d]
}


### CLASS DEFINITIONS ###

class Driver(Component):

    ### FIELDS ###

    motor: Motor      = None
    move_speed: float = None

    
    ### CONSTRUCTOR ###

    def __init__(self,
        name: str,
        motor: Motor=None,
        move_speed: float=None
    ) -> None:
        Component.__init__(self, name)

        self.motor = motor
        self.move_speed = move_speed if move_speed else DEFAULT_MOVE_SPEED

    
    ### COMPONENT METHODS ###

    def on_attach(self) -> None:
        if not self.motor:
            self.motor = self.being.fetch_component('motor')
            if not self.motor:
                self.motor = Motor('motor')
                self.being.attach_component(self.motor)


    def update(self, dt: float) -> None:
        super().update(dt)

    
    def on_detach(self) -> None:
        super().on_detach()

    
    ### AUXILIARY METHODS ###

    def set_motor(self, motor: Motor=None) -> None:
        self.motor = motor
        if self.being and self.motor and not self.motor.being:
            self.being.attach_component(self.motor)



class KeyDriver(Driver):

    ### FIELDS ###

    key_input: KeyInput   = None
    up_keys: list[int]    = None
    down_keys: list[int]  = None
    left_keys: list[int]  = None
    right_keys: list[int] = None
    keys_held: list[int]  = None


    ### CONSTRUCTOR ###

    def __init__(self,
        name: str,
        motor: Motor=None,
        key_input: KeyInput=None,
        move_speed: float=None,
        up_keys: list[int]=None,
        down_keys: list[int]=None,
        left_keys: list[int]=None,
        right_keys: list[int]=None
    ) -> None:
        Driver.__init__(self, name, motor, move_speed)

        self.key_input = key_input

        self.up_keys    = up_keys    if up_keys    else DEFAULT_KEYS['up_key']
        self.down_keys  = down_keys  if down_keys  else DEFAULT_KEYS['down_key']
        self.left_keys  = left_keys  if left_keys  else DEFAULT_KEYS['left_key']
        self.right_keys = right_keys if right_keys else DEFAULT_KEYS['right_key']
        self.keys_held  = []


    ### COMPONENT METHODS ###

    ### COMPONENT METHODS ###

    def on_attach(self) -> None:
        super().on_attach()
        
        if not self.key_input:
            self.key_input = self.being.fetch_component('key_input')
            if not self.key_input:
                self.key_input = KeyInput('key_input')
                self.being.attach_component(self.key_input)


    def update(self, dt: float) -> None:
        def tickle_keys(keylist: list[int]) -> None:
            for key in keylist:
                if self.key_input.check_key(key):
                    if key not in self.keys_held:
                        self.keys_held.append(key)
                        self.key_input.pull_key(key)
                elif key in self.keys_held:
                    self.keys_held.remove(key)
                    self.key_input.pull_key(key)

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


    def on_detach(self) -> None:
        super().on_detach()



class Seeker(Driver):

    ### FIELDS ###

    pix_mv_spd_sqrd: float = None
    lamp_post: Vector2     = None


    ### CONSTRUCTOR ###

    def __init__(self,
        name: str,
        motor: Motor=None,
        move_speed: float=None
    ) -> None:
        Driver.__init__(self, name, motor, move_speed)

        self.pix_mv_spd_sqrd = self.move_speed * self.move_speed * PIXEL_SIZE_SQUARED


    ### COMPONENT METHODS ###

    def on_attach(self) -> None:
        super().on_attach()


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
    

    def on_detach(self) -> None:
        super().on_detach()


    ### OPERATIONAL METHODS ###

    def set_lamp_post(self, lamp_post: Vector2=None) -> None:
        self.lamp_post = lamp_post
