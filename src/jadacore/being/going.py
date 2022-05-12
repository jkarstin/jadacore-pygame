#################################
# going.py       [v0.0.1-alpha] #
#===============================#
#                               #
#-------------------------------#
# J Karstin Neill    05.10.2022 #
#################################


### IMPORTS ###

import pygame
from pygame import Vector2

from . import Doing


### CONSTANTS & FLAGS ###

DEFAULT_KEYS: dict[str, list[int]] = {
    'up_key':    [pygame.K_UP,    pygame.K_w],
    'down_key':  [pygame.K_DOWN,  pygame.K_s],
    'left_key':  [pygame.K_LEFT,  pygame.K_a],
    'right_key': [pygame.K_RIGHT, pygame.K_d]
}
DEFAULT_MOVE_SPEED: float = 2.0


### CLASS DEFINITIONS ###

class Going(Doing):

    ### FIELDS ###

    up_keys: list[int]    = None
    down_keys: list[int]  = None
    left_keys: list[int]  = None
    right_keys: list[int] = None
    keys_held: list[int]  = None
    move_speed: float     = None


    ### CONSTRUCTOR ###

    def __init__(self,
        up_keys: list[int]=None,
        down_keys: list[int]=None,
        left_keys: list[int]=None,
        right_keys: list[int]=None,
        move_speed: float=None,
        **kwargs
    ) -> None:
        """
        Going() -> Going
        Going(up_keys: list[int], down_keys: list[int], left_keys: list[int], right_keys: list[int], move_speed: float, **kwargs) -> Going

        Arguments:
        ----------
            up_keys
            down_keys
            left_keys
            right_keys
            move_speed
            **kwargs
        """
        Doing.__init__(self, **kwargs)

        self.up_keys    = up_keys    if up_keys    else DEFAULT_KEYS['up_key']
        self.down_keys  = down_keys  if down_keys  else DEFAULT_KEYS['down_key']
        self.left_keys  = left_keys  if left_keys  else DEFAULT_KEYS['left_key']
        self.right_keys = right_keys if right_keys else DEFAULT_KEYS['right_key']
        self.keys_held  = []

        self.move_speed = move_speed if move_speed else DEFAULT_MOVE_SPEED


    ### METHODS ###

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
        self.move(move_vect)

        super().update(dt)
