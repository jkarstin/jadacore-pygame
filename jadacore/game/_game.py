#################################
# _game.py       [v0.0.1-alpha] #
#===============================#
#                               #
#-------------------------------#
# J Karstin Neill    06.03.2022 #
#################################


### IMPORTS ###

import pygame
from pygame import Surface, Vector2
from pygame.event import Event
from pygame.sprite import Group
from pygame.time import Clock

from jadacore.being import Being, Interactable
from jadacore.meta import WINDOW_SIZE


### CLASS STUBS ###

class Game:
    def __init__(self): ...
class World:
    def __init__(self): ...
class Window:
    def __init__(self,
        world: World=None
    ): ...

class Game:
    running: bool
    clock: Clock
    window: Window
    def __init__(self): ...
    def setup(self): ...
    def handle_events(self, events: list[Event]): ...
    def update(self, dt: float): ...
    def run(self): ...
    def set_world(self, world: World): ...
class Window:
    size: Vector2
    base_screen: Surface
    world: World
    def __init__(self,
        world: World=None
    ): ...
    def update(self, dt: float): ...
    def render(self): ...
    def set_world(self, world: World): ...
class World:
    world_group: Group
    interact_group: Group
    icon_group: Group
    world_screen: Surface
    def __init__(self): ...
    def setup(self): ...
    def update(self, dt: float): ...
    def update_world(self, dt: float): ...
    def draw(self, base_screen: Surface): ...
    def add(self, *beings: Being): ...


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

    def setup(self): pass
    def handle_events(self, events: list[Event]): pass
    def update(self, dt: float): pass
    

    def run(self):
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

    def set_world(self, world: World):
        self.window.set_world(world)



class Window:

    ### FIELDS ###

    size: Vector2        = None
    base_screen: Surface = None
    world: World         = None


    ### CONSTRUCTOR ###

    def __init__(self,
        world: World=None
    ):
        self.size = WINDOW_SIZE
        self.base_screen = pygame.display.set_mode(WINDOW_SIZE)
        self.world = world


    ### OPERATIONAL FUNCTIONS ###

    def update(self, dt: float):
        if self.world:
            self.world.update(dt)

    
    def render(self):
        if self.world:
            self.world.draw(self.base_screen)
            pygame.display.flip()


    ### UTILITY FUNCTIONS ###

    def set_world(self, world: World):
        self.world = world



class World:

    ### FIELDS ###

    world_group: Group    = None
    interact_group: Group = None
    icon_group: Group     = None
    world_screen: Surface = None


    ### CONSTRUCTOR ###

    def __init__(self):
        self.world_group = Group()
        self.interact_group = Group()
        self.icon_group = Group()
        self.world_screen = Surface(WINDOW_SIZE)
        self.setup()


    ### OPERATIONAL FUNCTIONS ###

    def setup(self): pass


    def update(self, dt: float):
        self.update_world(dt)
        

    def update_world(self, dt: float):
        self.world_group.update(dt)
        self.icon_group.update(dt)

    
    def draw(self, base_screen: Surface):
        self.world_group.clear(base_screen, self.world_screen)
        self.icon_group.clear(base_screen, self.world_screen)

        for sprite in self.world_group.sprites():
            being: Being = sprite
            being.pre_render()

        self.world_group.draw(base_screen)
        self.icon_group.draw(base_screen)


    ### UTILITY FUNCTIONS ###

    def add(self, *beings: Being):
        for being in beings:
            if isinstance(being, Interactable):
                self.interact_group.add(being)
            self.world_group.add(*beings)
