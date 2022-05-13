#################################
# _game.py       [v0.0.1-alpha] #
#===============================#
#                               #
#-------------------------------#
# J Karstin Neill    05.10.2022 #
#################################


### IMPORTS ###

import pygame
from pygame.event import Event
from pygame.time import Clock

from . import Window, World


### CONSTANTS & FLAGS ###


### CLASS DEFINITIONS ###

class Game:

    ### FIELDS ###

    running: bool  = None
    clock: Clock   = None
    window: Window = None


    ### CONSTRUCTOR ###

    def __init__(self):
        pygame.init()
        self.running = False
        self.window = Window()
        self.setup()


    ### OPERATIONAL METHODS ###

    def setup(self) -> None: pass
    def handle_events(self, events: list[Event]) -> None: pass
    def update(self, dt: float) -> None: pass
    

    def run(self) -> None:
        """
        run() -> None

        Starts up the Game instance, and returns upon pygame.QUIT event.
        """

        self.running = True
        self.clock = Clock()

        while self.running:
            events: list[Event] = pygame.event.get()
            for event in events:
                if event.type == pygame.QUIT:
                    self.running = False
                    break
            
            if self.running:
                self.handle_events(events)

                dt: float = self.clock.tick() / 1000.
                self.update(dt)
                self.window.update(dt)

                self.window.render()

        pygame.quit()

    
    ### AUXILIARY METHODS ###

    def set_world(self, world: World) -> None:
        self.window.set_world(world)
