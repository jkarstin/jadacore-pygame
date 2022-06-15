#################################
# util.py        [v0.0.2-alpha] #
#===============================#
#                               #
#-------------------------------#
# J Karstin Neill    06.14.2022 #
#################################


### IMPORTS ###

from pathlib import Path
import pygame
from pygame import Surface, Vector2
import sys

from jadacore.meta import PIXEL_SIZE, RESOURCES_PATH


### FUNCTION DEFINITIONS ###

def pox(
    pos: Vector2,
    pix: int=PIXEL_SIZE
) -> Vector2:
    if not (pos and pix): return None
    if pix <= 0: return Vector2()

    pox: Vector2 = Vector2(
        int(pos.x / pix) * pix,
        int(pos.y / pix) * pix
    )

    return pox


def load_pixel_image(
    image_path: Path,
    pix: int=PIXEL_SIZE
) -> Surface:
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


### CLASS DEFINITIONS ###

class Stylist:

    ### CONSTANTS & FLAGS ###

    STYLE_TAGS = {
        'bold':                      '\u001b[1m',
        'underline':                 '\u001b[4m',
        'reversed':                  '\u001b[7m',
        'black':                     '\u001b[30m',
        'red':                       '\u001b[31m',
        'green':                     '\u001b[32m',
        'yellow':                    '\u001b[33m',
        'blue':                      '\u001b[34m',
        'magenta':                   '\u001b[35m',
        'cyan':                      '\u001b[36m',
        'white':                     '\u001b[37m',
        'background black':          '\u001b[40m',
        'background red':            '\u001b[41m',
        'background green':          '\u001b[42m',
        'background yellow':         '\u001b[43m',
        'background blue':           '\u001b[44m',
        'background magenta':        '\u001b[45m',
        'background cyan':           '\u001b[46m',
        'background white':          '\u001b[47m',
        'bright black':              '\u001b[30;1m',
        'bright red':                '\u001b[31;1m',
        'bright green':              '\u001b[32;1m',
        'bright yellow':             '\u001b[33;1m',
        'bright blue':               '\u001b[34;1m',
        'bright magenta':            '\u001b[35;1m',
        'bright cyan':               '\u001b[36;1m',
        'bright white':              '\u001b[37;1m',
        'background bright black':   '\u001b[40;1m',
        'background bright red':     '\u001b[41;1m',
        'background bright green':   '\u001b[42;1m',
        'background bright yellow':  '\u001b[43;1m',
        'background bright blue':    '\u001b[44;1m',
        'background bright magenta': '\u001b[45;1m',
        'background bright cyan':    '\u001b[46;1m',
        'background bright white':   '\u001b[47;1m',
        'reset':                     '\u001b[0m'
    }


    ### FUNCTION DEFINITIONS ###

    def style(
        *tags: str
    ) -> str:
        if tags:
            styled: str = ''
            for tag in tags:
                if tag in Stylist.STYLE_TAGS.keys():
                    styled += Stylist.STYLE_TAGS[tag]
            return styled
        return None



class Log:

    ### CONSTANTS & FLAGS ###

    LOG_STYLE_ERROR: str = Stylist.style('red', 'underline')

    # EXIT/ERROR CODES
    EXIT_SUCCESS: int            = 0
    ERROR_GENERIC: int           = 1
    ERROR_UNNAMED_COMPONENT: int = 2


    ### FUNCTION DEFINITIONS ###

    def error(msg: str, err_code: int=ERROR_GENERIC):
        Log.sprint(f"[ERROR]: {msg}", Log.LOG_STYLE_ERROR)
        sys.exit(err_code)


    def sprint(value: any, styletags: str='', **kwargs):
        if not styletags: styletags = ''
        print(f"{styletags}{value}{Stylist.style('reset')}", **kwargs)