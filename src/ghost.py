#################################
# ghost.py       [v0.0.1-alpha] #
#===============================#
#                               #
#-------------------------------#
# J Karstin Neill    05.09.2022 #
#################################


### IMPORTS ###

from pathlib import Path

from jadacore.being import Doing


### CONSTANTS & FLAGS ###


### CLASS DEFINITIONS ###

class Ghost(Doing):

    ### FIELDS ###


    ### CONSTRUCTOR ###

    def __init__(
        self,
        ghost_path: Path,
        *args,
        **kwargs
    ) -> None:
        Doing.__init__(self, ghost_path, *args, **kwargs)


    ### METHODS ###
