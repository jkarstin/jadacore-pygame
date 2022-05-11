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

    def __init__(
        self,
        up_keys: list[int]=None,
        down_keys: list[int]=None,
        left_keys: list[int]=None,
        right_keys: list[int]=None,
        move_speed: float=10.0,
        **kwargs
    ) -> None:
        Doing.__init__(self, **kwargs)

        self.up_keys    = up_keys    if up_keys    else [pygame.K_w, pygame.K_UP]
        self.down_keys  = down_keys  if down_keys  else [pygame.K_s, pygame.K_DOWN]
        self.left_keys  = left_keys  if left_keys  else [pygame.K_a, pygame.K_LEFT]
        self.right_keys = right_keys if right_keys else [pygame.K_d, pygame.K_RIGHT]
        self.keys_held  = []

        self.move_speed = move_speed if move_speed else 10.0


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


        def record_movement(keylist: list[int], delta: Vector2) -> None:
            for key in keylist:
                if key in self.keys_held:
                    if self.move_vect:
                        self.move_vect += delta
                    else:
                        self.move_vect = delta
                    break

        record_movement(self.up_keys,    Vector2(               0, -self.move_speed))
        record_movement(self.down_keys,  Vector2(               0,  self.move_speed))
        record_movement(self.left_keys,  Vector2(-self.move_speed,                0))
        record_movement(self.right_keys, Vector2( self.move_speed,                0))


        super().update(dt)
