#################################
# log.py         [v0.0.1-alpha] #
#===============================#
#                               #
#-------------------------------#
# J Karstin Neill    05.10.2022 #
#################################


### IMPORTS ###

import sys

from jadacore.meta import ERROR_GENERIC
from . import Stylist


### CONSTANTS & FLAGS ###

LOG_STYLE_ERROR: str = Stylist.style('red', 'underline')


### CLASS DEFINITIONS ###


### FUNCTION DEFINITIONS ###

def error(msg: str, err_code: int=ERROR_GENERIC) -> None:
    sprint(f"[ERROR]: {msg}", LOG_STYLE_ERROR)
    sys.exit(err_code)


def sprint(value: any, styletags: str='', **kwargs) -> None:
    if not styletags: styletags = ''
    print(f"{styletags}{value}{Stylist.style('reset')}", **kwargs)