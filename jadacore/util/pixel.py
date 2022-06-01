#################################
# pixel.py       [v0.0.1-alpha] #
#===============================#
#                               #
#-------------------------------#
# J Karstin Neill    06.01.2022 #
#################################


### IMPORTS ###

from pathlib import Path
import pygame
from pygame import Surface, Vector2

from jadacore.meta import PIXEL_SIZE, RESOURCES_PATH


### FUNCTION DEFINITIONS ###

def pox(pos: Vector2, pix: int=PIXEL_SIZE) -> Vector2:
    if not (pos and pix): return None
    if pix <= 0: return Vector2()

    pox: Vector2 = Vector2(
        int(pos.x / pix) * pix,
        int(pos.y / pix) * pix
    )

    return pox


def load_pixel_image(image_path: Path, pix: int=PIXEL_SIZE) -> Surface:
    if not image_path or pix <= 0: return None

    image_raw: Surface = pygame.image.load(RESOURCES_PATH/image_path)
    pixel_image = pygame.transform.scale(
        image_raw.convert_alpha(),
        [
            image_raw.get_width()  * PIXEL_SIZE,
            image_raw.get_height() * PIXEL_SIZE
        ]
    )

    return pixel_image
