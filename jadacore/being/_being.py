#################################
# _being.py      [v0.0.1-alpha] #
#===============================#
#                               #
#-------------------------------#
# J Karstin Neill    05.31.2022 #
#################################


### IMPORTS ###

from pathlib import Path
import pygame
from pygame import Color, Surface, Rect, Vector2
from pygame.sprite import Group, Sprite

from jadacore.meta import RESOURCES_PATH, PIXEL_SIZE
import jadacore.util as util
import jadacore.util.log as log
from jadacore.util import ERROR_UNNAMED_COMPONENT


### CLASS STUBS ###

class Being(Sprite):
    def __init__(self,
        pos: Vector2=None,
        size: Vector2=None,
        color: Color=None,
        image_path: Path=None,
        groups: list[Group]=None
    ): ...
class Component:
    def __init__(self,
        name: str
    ): ...
class Component:
    def __init__(self, name: str): ...
    def attach_to(self, being: Being=None) -> Component: ...
    def detach_from(self, being: Being=None) -> Component: ...
    def on_attach(self): ...
    def on_detach(self): ...
    def update(self, dt: float): ...


### CONSTANTS & FLAGS ###

# ::Being
DEFAULT_POS: Vector2 = Vector2()
DEFAULT_SIZE: Vector2 = Vector2(1)
DEFAULT_COLOR: Color  = Color('pink')


### CLASS DEFINITIONS ###

class Being(Sprite):
    """
    Description:
    ------------

    """

    ### FIELDS ###

    pos: Vector2   = None
    size: Vector2  = None
    image: Surface = None
    rect: Rect     = None

    components: dict[str, Component] = None


    ### CONSTRUCTOR ###

    def __init__(self,
        pos: Vector2=None,
        size: Vector2=None,
        color: Color=None,
        image_path: Path=None,
        groups: list[Group]=None
    ):
        """
        Usage:
        ------
        Being(pos: Vector2=None, size: Vector2=None, color: Color=None, image_path: Path=None, groups: list[Group]=None) -> <Being>

        Description:
        ------------
        Constructor for Being Sprite subclass.

        Arguments:
        ----------
        - pos: Vector2=None -
        - size: Vector2=None - 
        - color: Color=None - 
        - image_path: Path=None - 
        - groups: list[Group]=None - 

        Returns:
        --------
        - <Being> - Instance of Being class.
        """
        Sprite.__init__(self)

        self.pos = pos if pos else DEFAULT_POS
        self.size = PIXEL_SIZE * (size if size else DEFAULT_SIZE)

        if image_path:
            image_raw: Surface = pygame.image.load(RESOURCES_PATH/image_path)
            self.image = pygame.transform.scale(
                image_raw.convert_alpha(),
                [image_raw.get_width() * self.size.x, image_raw.get_height() * self.size.y]
            )
        else:
            self.image = Surface(self.size)
            self.image.fill(color if color else DEFAULT_COLOR)
        
        self.rect = self.image.get_rect()

        if groups:
            for group in groups: group.add(self)

        self.components = {}


    ### OPERATIONAL METHODS ###

    def update(self, dt: float):
        """
        Usage:
        ------


        Description:
        ------------


        Arguments:
        ----------
        

        Returns:
        --------

        """
        for name in self.components:
            self.components[name].update(dt)

        
    def pre_render(self):
        if self.pos:
            pox: Vector2 = util.pox(self.pos)
            self.rect.centerx = pox.x
            self.rect.bottom  = pox.y

    
    ### AUXILIARY METHODS ###
    
    def attach(self, component: Component=None):
        """
        Usage:
        ------


        Description:
        ------------


        Arguments:
        ----------
        

        Returns:
        --------

        """
        if component and component.name not in self.components:
            self.components[component.name] = component
            component.attach_to(self)


    def fetch_component(self, name: str) -> Component:
        """
        Usage:
        ------


        Description:
        ------------


        Arguments:
        ----------
        

        Returns:
        --------

        """
        if name and name in self.components:
            return self.components[name]
        return None

    
    def detach(self, component: Component=None):
        """
        Usage:
        ------


        Description:
        ------------


        Arguments:
        ----------
        

        Returns:
        --------

        """
        if component and component.name in self.components:
            self.components.pop(component.name)
            component.detach_from(self)
    


class Component:
    """
    Description:
    ------------
    Components are a basic building block for Being behavior in jadacore. They are very closely linked with the Being class,
    and function as extendable virtual plug-ins that allow for modular customization of specilized characteristics.

    In short: this is a superclass template which provides three specific methods that can be used to initialize (on_attach),
    adjust/maintain/interact during the game loop (update) and then clean up when no longer needed (on_detach). Some important
    and commonly-used Component subclasses are already made in the jadacore library in the jadacore.comp package, if you would
    like to see different implementations of Component behavior.

    Every Component has a name string, for look-up in their attached Being instances, and a reference to said attached Being, if
    one exists. This Being instance is automatically assigned when attached to a Being (by the Being class), and removed upon
    detaching (again, by the Being class), so you can check to see if a given Component is attached by checking if the Being
    instance is None or not. The on_attach and on_detach methods are provided for further design control, and do not need to call
    their overridden parent methods in order to maintain the Being assignment, since it is handled by the Being class.

    Constructor:
    ------------
    Component(name: str) -> <Component>
    """
    name: str    = None
    being: Being = None


    def __init__(self, name: str):
        """
        Usage:
        ------
        Component(name: str) -> <Component>

        Description:
        ------------
        Constructor for Component class.

        Arguments:
        ----------
        - name: str - Name of the Component instance.        

        Returns:
        --------
        - <Component> - Instance of Component class.
        """
        if not name: log.error("Cannot initialize Component without a name!", ERROR_UNNAMED_COMPONENT)
        self.name = name

    
    def on_attach(self):
        """
        Usage:
        ------


        Description:
        ------------


        Arguments:
        ----------
        

        Returns:
        --------

        """
        pass
    def on_detach(self):
        """
        Usage:
        ------


        Description:
        ------------


        Arguments:
        ----------
        

        Returns:
        --------

        """
        pass
    def update(self, dt: float):
        """
        Usage:
        ------


        Description:
        ------------


        Arguments:
        ----------
        

        Returns:
        --------

        """
        pass


    def attach_to(self, being: Being=None):
        """
        Usage:
        ------


        Description:
        ------------


        Arguments:
        ----------
        

        Returns:
        --------

        """
        if being:
            if self.being:
                self.being.detach(self)
            self.being = being
            self.on_attach()

    
    def detach_from(self, being: Being=None):
        """
        Usage:
        ------


        Description:
        ------------


        Arguments:
        ----------
        

        Returns:
        --------

        """
        if being and self.being == being:
            self.on_detach()
            self.being = None
