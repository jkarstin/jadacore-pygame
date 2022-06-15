#################################
# going.py       [v0.0.2-alpha] #
#===============================#
#                               #
#-------------------------------#
# J Karstin Neill    06.14.2022 #
#################################


### IMPORTS ###

from pathlib import Path
import pygame
from pygame import Vector2

from jadacore.meta import PIXEL_SIZE, PIXEL_SIZE_SQUARED
from jadacore.being import Component
from jadacore.doing import Doing, Motor
from jadacore.input import KeyInput, MouseInput


### CLASS STUBS ###

class Driving(Doing):
    def __init__(self,
        sprite_sheet_path: Path,
        **kwargs
    ): ...
class Going(Driving):
    def __init__(self,
        sprite_sheet_path: Path,
        key_input: KeyInput=None,
        up_keys: list[int]=None,
        down_keys: list[int]=None,
        left_keys: list[int]=None,
        right_keys: list[int]=None,
        move_speed: float=None,
        **kwargs
    ): ...
class Seeking(Driving):
    def __init__(self,
        sprite_sheet_path: Path,
        move_speed: float=None,
        **kwargs
    ): ...
class Driver(Component):
    def __init__(self,
        name: str,
        motor: Motor=None,
        move_speed: float=None
    ): ...
class KeyDriver(Driver):
    def __init__(self,
        name: str,
        key_input: KeyInput=None,
        up_keys: list[int]=None,
        down_keys: list[int]=None,
        left_keys: list[int]=None,
        right_keys: list[int]=None,
        **kwargs
    ): ...
class Seeker(Driver):
    def __init__(self,
        name: str,
        **kwargs
    ): ...
class ClickSeeker(Seeker):
    def __init__(self,
        name: str,
        mouse_input: MouseInput=None,
        **kwargs
    ): ...

class Driving(Doing):
    driver: Driver
    def __init__(self,
        sprite_sheet_path: Path,
        **kwargs
    ): ...
class Going(Driving):
    driver: KeyDriver
    def __init__(self,
        sprite_sheet_path: Path,
        key_input: KeyInput=None,
        up_keys: list[int]=None,
        down_keys: list[int]=None,
        left_keys: list[int]=None,
        right_keys: list[int]=None,
        move_speed: float=None,
        **kwargs
    ): ...
class Seeking(Driving):
    driver: Seeker
    def __init__(self,
        sprite_sheet_path: Path,
        move_speed: float=None,
        **kwargs
    ): ...
    def set_lamp_post(self, lamp_post: Vector2=None): ...
class Driver(Component):
    motor: Motor
    move_speed: float
    def __init__(self,
        name: str,
        motor: Motor=None,
        move_speed: float=None
    ): ...
    def on_attach(self): ...
    def set_motor(self, motor: Motor=None): ...
class KeyDriver(Driver):
    key_input: KeyInput
    up_keys: list[int]
    down_keys: list[int]
    left_keys: list[int]
    right_keys: list[int]
    keys_held: list[int]
    def __init__(self,
        name: str,
        key_input: KeyInput=None,
        up_keys: list[int]=None,
        down_keys: list[int]=None,
        left_keys: list[int]=None,
        right_keys: list[int]=None,
        **kwargs
    ): ...
    def on_attach(self): ...
    def update(self, dt: float): ...
class Seeker(Driver):
    pix_mv_spd_sqrd: float
    lamp_post: Vector2
    def __init__(self,
        name: str,
        **kwargs
    ): ...
    def update(self, dt: float): ...
    def set_lamp_post(self, lamp_post: Vector2=None): ...
class ClickSeeker(Seeker):
    def __init__(self,
        name: str,
        mouse_input: MouseInput=None,
        **kwargs
    ): ...
    def on_attach(self): ...
    def update(self, dt: float): ...


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

class Driving(Doing):

    ### FIELDS ###

    driver: Driver = None


    ### CONSTRUCTOR ###

    def __init__(self,
        sprite_sheet_path: Path,
        **kwargs
    ):
        Doing.__init__(self,
            sprite_sheet_path,
            **kwargs
        )


class Going(Driving):

    ### FIELDS ###

    driver: KeyDriver = None


    ### CONSTRUCTOR ###

    def __init__(self,
        sprite_sheet_path: Path,
        key_input: KeyInput=None,
        up_keys: list[int]=None,
        down_keys: list[int]=None,
        left_keys: list[int]=None,
        right_keys: list[int]=None,
        move_speed: float=None,
        **kwargs
    ) -> None:
        Driving.__init__(self,
            sprite_sheet_path,
            **kwargs
        )

        self.driver = KeyDriver('key_driver',
            key_input, up_keys, down_keys, left_keys, right_keys,
            motor=self.motor, move_speed=move_speed
        )
        self.attach(self.driver)



class Seeking(Driving):

    ### FIELDS ###

    driver: Seeker = None


    ### CONSTRUCTOR ###

    def __init__(self,
        sprite_sheet_path: Path,
        move_speed: float=None,
        **kwargs
    ):
        Driving.__init__(self,
            sprite_sheet_path,
            **kwargs
        )

        self.driver = Seeker('seeker',
            motor=self.motor, move_speed=move_speed
        )
        self.attach(self.driver)

    
    ### WRAPPER METHODS ###

    def set_lamp_post(self, lamp_post: Vector2=None):
        self.driver.set_lamp_post(lamp_post)



class Driver(Component):

    ### FIELDS ###

    motor: Motor      = None
    move_speed: float = None

    
    ### CONSTRUCTOR ###

    def __init__(self,
        name: str,
        motor: Motor=None,
        move_speed: float=None
    ):
        Component.__init__(self, name)

        self.motor = motor
        self.move_speed = move_speed if move_speed else DEFAULT_MOVE_SPEED

    
    ### COMPONENT METHODS ###

    def on_attach(self):
        if not self.motor:
            self.motor = self.being.fetch_component('motor')
            if not self.motor:
                self.motor = Motor('motor')
                self.being.attach(self.motor)

    
    ### AUXILIARY METHODS ###

    def set_motor(self, motor: Motor=None):
        self.motor = motor
        if self.being and self.motor and not self.motor.being:
            self.being.attach(self.motor)



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
        key_input: KeyInput=None,
        up_keys: list[int]=None,
        down_keys: list[int]=None,
        left_keys: list[int]=None,
        right_keys: list[int]=None,
        **kwargs
    ):
        Driver.__init__(self, name, **kwargs)

        self.key_input = key_input

        self.up_keys    = up_keys    if up_keys    else DEFAULT_KEYS['up_key']
        self.down_keys  = down_keys  if down_keys  else DEFAULT_KEYS['down_key']
        self.left_keys  = left_keys  if left_keys  else DEFAULT_KEYS['left_key']
        self.right_keys = right_keys if right_keys else DEFAULT_KEYS['right_key']
        self.keys_held  = []

    
    ### COMPONENT METHODS ###

    def on_attach(self):
        super().on_attach()
        
        if not self.key_input:
            self.key_input = self.being.fetch_component('key_input')
            if not self.key_input:
                self.key_input = KeyInput('key_input')
                self.being.attach(self.key_input)


    def update(self, dt: float):
        def tickle_keys(keylist: list[int]):
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



class Seeker(Driver):

    ### FIELDS ###

    pix_mv_spd_sqrd: float = None
    lamp_post: Vector2     = None


    ### CONSTRUCTOR ###

    def __init__(self,
        name: str,
        **kwargs
    ):
        Driver.__init__(self, name, **kwargs)

        self.pix_mv_spd_sqrd = self.move_speed * self.move_speed * PIXEL_SIZE_SQUARED


    ### COMPONENT METHODS ###

    def update(self, dt: float):
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



class ClickSeeker(Seeker):

    ### FIELDS ###

    mouse_input: MouseInput = None


    ### CONSTRUCTOR ###

    def __init__(self,
        name: str,
        mouse_input: MouseInput=None,
        **kwargs
    ):
        Seeker.__init__(self, name, **kwargs)

        self.mouse_input = mouse_input

    
    ### COMPONENT METHODS ###

    def on_attach(self):
        super().on_attach()
        
        if not self.mouse_input:
            self.mouse_input = self.being.fetch_component('mouse_input')
            if not self.mouse_input:
                self.mouse_input = MouseInput('mouse_input')
                self.being.attach(self.mouse_input)


    def update(self, dt: float):
        super().update(dt)

        if self.mouse_input.pull_button(pygame.BUTTON_LEFT):
            if self.mouse_input.mouse_pos:
                self.set_lamp_post(self.mouse_input.mouse_pos)
