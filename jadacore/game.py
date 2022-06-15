#################################
# game.py        [v0.0.2-alpha] #
#===============================#
#                               #
#-------------------------------#
# J Karstin Neill    06.14.2022 #
#################################


### IMPORTS ###

import pygame
from pygame import Surface, Vector2
from pygame.event import Event
from pygame.sprite import Group
from pygame.time import Clock

from jadacore.meta import WINDOW_SIZE
from jadacore.being import Being
from jadacore.interact import Interactable


### CLASS STUBS ###

class Game:
    def __init__(self
    ): ...
class World:
    def __init__(self
    ): ...
class Screen:
    def __init__(self
    ): ...
class Window:
    def __init__(self
    ): ...

class Game:
    running: bool
    clock: Clock
    window: Window
    #input: Input
    def __init__(self
    ): ...
    def setup(self
    ): ...
    def handle_events(self,
        events: list[Event]
    ): ...
    def update(self,
        dt: float
    ): ...
    def run(self
    ): ...
    def set_world(self,
        world: World
    ): ...
class Window:
    size: Vector2
    screens: list[Screen]
    active_screen_index: int
    worlds: list[World]
    active_world_index: int
    def __init__(self
    ): ...
    def update(self,
        dt: float
    ): ...
    def render(self
    ): ...
    def add_screen(self,
        screen: Screen
    ): ...
    def set_screen(self,
        screen: Screen
    ): ...
    def add_world(self,
        world: World
    ): ...
    def set_world(self,
        world: World
    ): ...
class Screen:
    size: Vector2
    base_surface: Surface
    #input_manager: InputManager
    def __init__(self
    ): ...
class World:
    world_group: Group
    interact_group: Group
    icon_group: Group
    clear_surface: Surface
    def __init__(self
    ): ...
    def setup(self
    ): ...
    def update(self,
        dt: float
    ): ...
    def update_world(self,
        dt: float
    ): ...
    def draw(self,
        base_screen: Surface
    ): ...
    def add(self,
        *beings: Being
    ): ...


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


    ### PLACEHOLDER METHODS ###

    def setup(self): pass
    def handle_events(self, events: list[Event]): pass
    def update(self, dt: float): pass
    

    ### OPERATIONAL METHODS ###

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

    size: Vector2            = None
    screens: list[Screen]    = None
    active_screen_index: int = None
    worlds: list[World]      = None
    active_world_index: int  = None


    ### CONSTRUCTOR ###

    def __init__(self):
        self.size = WINDOW_SIZE
        self.screens = [pygame.display.set_mode(WINDOW_SIZE)]
        self.active_screen_index = 0
        self.worlds = []
        self.active_world_index = -1


    ### OPERATIONAL FUNCTIONS ###

    def update(self, dt: float):
        if self.active_world_index in range(len(self.worlds)):
            self.worlds[self.active_world_index].update(dt)

    
    def render(self):
        if self.active_screen_index in range(len(self.screens)) and \
            self.active_world_index in range(len(self.worlds)):
            self.worlds[self.active_world_index].draw(self.screens[self.active_screen_index])
            pygame.display.flip()


    ### UTILITY FUNCTIONS ###

    def add_screen(self,
        screen: Screen
    ):
        if screen and screen not in self.screens:
            self.screens.append(screen)


    def set_screen(self,
        screen: Screen
    ):
        self.add_screen(screen)
        self.active_screen_index = self.screens.index(screen)


    def add_world(self,
        world: World
    ):
        if world and world not in self.worlds:
            self.worlds.append(world)


    def set_world(self, world: World):
        self.add_world(world)
        self.active_world_index = self.worlds.index(world)
        



class World:

    ### FIELDS ###

    world_group: Group     = None
    interact_group: Group  = None
    icon_group: Group      = None
    clear_surface: Surface = None


    ### CONSTRUCTOR ###

    def __init__(self):
        self.world_group = Group()
        self.interact_group = Group()
        self.icon_group = Group()
        self.clear_surface = Surface(WINDOW_SIZE)
        self.setup()


    ### OPERATIONAL FUNCTIONS ###

    def setup(self): pass

    
    def update(self, dt: float):
        self.update_world(dt)
        

    def update_world(self, dt: float):
        self.world_group.update(dt)
        self.icon_group.update(dt)

    
    def draw(self, screen_surface: Surface):
        self.world_group.clear(screen_surface, self.clear_surface)
        self.icon_group.clear(screen_surface, self.clear_surface)

        for sprite in self.world_group.sprites():
            being: Being = sprite
            being.pre_render()

        self.world_group.draw(screen_surface)
        self.icon_group.draw(screen_surface)


    ### UTILITY FUNCTIONS ###

    def add(self, *beings: Being):
        for being in beings:
            if isinstance(being, Interactable):
                self.interact_group.add(being)
            self.world_group.add(*beings)
