#################################
# block.py       [v0.0.1-alpha] #
#===============================#
#                               #
#-------------------------------#
# J Karstin Neill    05.06.2022 #
#################################


### IMPORTS ###

from pygame import Color
from pygame import Rect
from pygame import Surface
from pygame import Vector2
from pygame.sprite import Group
from pygame.sprite import Sprite

from meta import PIXEL_SIZE


### CLASS DEFINITIONS ###

class Block(Sprite):

    image: Surface = None
    rect: Rect = None
    pos: Vector2 = None


    def __init__(
        self,
        size: Vector2,
        pos: Vector2=Vector2(),
        color: Color=Color('cyan'),
        groups: list[Group]=[]
    ) -> None:
        Sprite.__init__(self)

        self.image = Surface(size)
        self.rect = self.image.get_rect()

        self.image.fill(color)

        for group in groups: group.add(self)

        self.pos = pos if pos else Vector2()

        self.rect.x = int(self.pos.x)
        self.rect.y = int(self.pos.y)
    
    
    def update(self, dt: float) -> None:
        self.pos.x += 80 * dt
        self.pos.y += 45 * dt

        self.rect.x = int(self.pos.x / PIXEL_SIZE) * PIXEL_SIZE
        self.rect.y = int(self.pos.y / PIXEL_SIZE) * PIXEL_SIZE
