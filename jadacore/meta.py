#################################
# meta.py        [v0.0.2-alpha] #
#===============================#
#                               #
#-------------------------------#
# J Karstin Neill    06.14.2022 #
#################################


### IMPORTS ###

from pathlib import Path


### SYSTEM CONSTANTS ###

RESOURCES_PATH: Path = Path('./resources')


### GAME CONSTANTS ###

PIXEL_SIZE: int = 4
PIXEL_SIZE_SQUARED: int = PIXEL_SIZE * PIXEL_SIZE
WINDOW_SIZE = WINDOW_WIDTH, WINDOW_HEIGHT = 160 * PIXEL_SIZE, 90 * PIXEL_SIZE
