#################################
# pixel.py       [v0.0.1-alpha] #
#===============================#
#                               #
#-------------------------------#
# J Karstin Neill    05.31.2022 #
#################################


### IMPORTS ###

from pygame import Vector2

from jadacore.meta import PIXEL_SIZE


### FUNCTION DEFINITIONS ###

def pox(pos: Vector2, pix: int=PIXEL_SIZE) -> Vector2:
    if not (pos and pix): return None
    if pix == 0: return Vector2()

    pox: Vector2 = Vector2(
        int(pos.x / pix) * pix,
        int(pos.y / pix) * pix
    )

    return pox
