#################################
# _motor.py      [v0.0.1-alpha] #
#===============================#
#                               #
#-------------------------------#
# J Karstin Neill    05.11.2022 #
#################################


### IMPORTS ###

from pygame import Vector2

from jadacore.being import Component
from jadacore.meta import PIXEL_SIZE


### CLASS DEFINITIONS ###

class Motor(Component):

    ### FIELDS ###

    pos: Vector2       = None
    move_vect: Vector2 = None


    ### COMPONENT METHODS ###

    def on_attach(self): pass


    def update(self, dt: float):
        if self.being:
            if self.move_vect:
                self.being.pos.x += self.move_vect.x * PIXEL_SIZE * dt
                self.being.pos.y += self.move_vect.y * PIXEL_SIZE * dt
                self.move_vect = None
            
            self.being.rect.x = int(self.being.pos.x / PIXEL_SIZE) * PIXEL_SIZE
            self.being.rect.y = int(self.being.pos.y / PIXEL_SIZE) * PIXEL_SIZE

    
    def on_detach(self): pass


    ### OPERATIONAL METHODS ###

    def move(self, move_vect: Vector2):
        self.move_vect = move_vect
