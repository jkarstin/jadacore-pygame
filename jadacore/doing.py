#################################
# doing.py       [v0.0.2-alpha] #
#===============================#
#                               #
#-------------------------------#
# J Karstin Neill    06.14.2022 #
#################################


### IMPORTS ###

from pathlib import Path
from pygame import Surface, Vector2

from jadacore.meta import PIXEL_SIZE
import jadacore.util as util
from jadacore.being import Being, Component


### CLASS STUBS ###

class Doing(Being):
    def __init__(self,
        sprite_sheet_path: Path,
        sprite_sheet_dims: Vector2=None,
        frames_per_second: float=None,
        animation_style: int=None,
        default_anim_name: str=None,
        **kwargs
    ): ...
class Animation(Component):
    def __init__(self,
        name: str,
        sprite_sheet_path: Path,
        sprite_sheet_dims: Vector2=None,
        frames_per_second: float=None,
        animation_style: int=None
    ): ...
class Animator(Component):
    def __init__(self,
        name: str,
        sprite_sheet_path: Path,
        sprite_sheet_dims: Vector2=None,
        frames_per_second: float=None,
        animation_style: int=None,
        default_anim_name: str=None
    ): ...
class Motor(Component):
    def __init__(self,
        name: str
    ): ...
class StepMotor(Motor):
    def __init__(self,
        name: str,
        step_size: int=None,
        steps_per_second: float=None
    ): ...

class Doing(Being):
    motor: Motor
    animator: Animator
    def __init__(self,
        sprite_sheet_path: Path,
        sprite_sheet_dims: Vector2=None,
        frames_per_second: float=None,
        animation_style: int=None,
        default_anim_name: str=None,
        **kwargs
    ): ...
    def move(self, move_vect: Vector2): ...
    def add_animation(self, anim_name: str, sprite_sheet_path: Path, **kwargs) -> Animation: ...
    def set_animation(self, anim_name: str) -> Animation: ...
class Animation(Component):
    ANIM_STYLE_LOOP: int
    ANIM_STYLE_ONCE: int
    ANIM_STYLE_BOUNCE: int
    ANIM_STATE_STOPPED: int
    ANIM_STATE_RUNNING: int
    ANIM_STATE_PAUSED:  int
    sprite_sheet: Surface
    sprite_sheet_dims: Vector2
    frames: list[Surface]
    frame_size: Vector2
    current_frame: Surface
    current_frame_index: int
    current_frame_time: float
    frame_seconds: float
    animation_style: int
    animation_state: int
    animation_time: float
    def __init__(self,
        name: str,
        sprite_sheet_path: Path,
        sprite_sheet_dims: Vector2=None,
        frames_per_second: float=None,
        animation_style: int=None
    ): ...
    def on_attach(self): ...
    def update(self, dt: float): ...
    def start(self) -> tuple[int, float, float, int, int]: ...
    def pause(self) -> tuple[int, float, float, int, int]: ...
    def stop(self) -> tuple[int, float, float, int, int]: ...
    def get_frame(self, i: int=None) -> Surface: ...
class Animator(Component):
    animations: dict[str, Animation]
    current_animation: Animation
    current_anim_name: str
    def __init__(self,
        name: str,
        sprite_sheet_path: Path,
        sprite_sheet_dims: Vector2=None,
        frames_per_second: float=None,
        animation_style: int=None,
        default_anim_name: str=None
    ): ...
    def on_attach(self): ...
    def update(self, dt: float): ...
    def on_detach(self): ...
    def start(self): ...
    def pause(self): ...
    def stop(self): ...
    def add_animation(self,
        anim_name: str,
        sprite_sheet_path: Path,
        sprite_sheet_dims: Vector2=None,
        frames_per_second: float=None,
        animation_style: int=None
    ) -> Animation: ...
    def set_animation(self, anim_name: str) -> Animation: ...
class Motor(Component):
    move_vect: Vector2
    def update(self, dt: float): ...
    def move(self, move_vect: Vector2): ...
class StepMotor(Motor):
    step_size: int
    min_step_time: float
    def __init__(self,
        name: str,
        step_size: int=None,
        steps_per_second: float=None
    ): ...
    def update(self, dt: float): ...
    def move(self, dir_vect: Vector2): ...


### CONSTANTS & FLAGS ###

# ::Animation
DEFAULT_SPRITE_SHEET_DIMS: Vector2 = Vector2(1)
DEFAULT_FRAME_SECONDS: float       = 0.5
DEFAULT_ANIM_STYLE: int            = 0

# ::Animator
DEFAULT_ANIM_NAME: str = 'anim_default'

# ::StepMotor
DEFAULT_STEP_SIZE: int       = 1
DEFAULT_MIN_STEP_TIME: float = 0.35


### CLASS DEFINITIONS ###

class Doing(Being):
    """
    Description:
    ------------

    """

    ### FIELDS ###

    motor: Motor = None
    animator: Animator = None


    ### CONSTRUCTOR ###

    def __init__(self,
        sprite_sheet_path: Path,
        sprite_sheet_dims: Vector2=None,
        frames_per_second: float=None,
        animation_style: int=None,
        default_anim_name: str=None,
        **kwargs
    ) -> None:
        """
        Usage:
        ------
        Doing(sprite_sheet_path: Path, sprite_sheet_dims: Vector2=None, frames_per_second: float=None, animation_style: int=None, default_anim_name: str=None, **kwargs)

        Description:
        ------------
        Constructor for Doing class

        Arguments:
        ----------
        - sprite_sheet_path: Path
        - sprite_sheet_dims: Vector2=None
        - frames_per_second: float=None
        - animation_style: int=None
        - default_anim_name: str=None
        - **kwargs:
            - pos: Vector2=None        [::Being]
            - size: Vector2=None       [::Being]
            - color: Color=None        [::Being]
            - image_path: Path=None    [::Being]
            - groups: list[Group]=None [::Being]
        
        Returns:
        --------
        - instance of Doing class
        """
        Being.__init__(self, **kwargs)

        self.motor = Motor('motor')
        self.attach(self.motor)

        self.animator = Animator(
            'animator',
            sprite_sheet_path,
            sprite_sheet_dims,
            frames_per_second,
            animation_style,
            default_anim_name
        )
        self.attach(self.animator)

        self.animator.start()


    ### WRAPPING METHODS ###

    def move(self, move_vect: Vector2):
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
        self.motor.move(move_vect)
        

    def add_animation(self,
        anim_name: str,
        sprite_sheet_path: Path,
        **kwargs
    ) -> Animation:
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
        return self.animator.add_animation(
            anim_name,
            sprite_sheet_path,
            **kwargs
        )
        
    
    def set_animation(self, anim_name: str) -> Animation:
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
        return self.animator.set_animation(anim_name)



class Animation(Component):

    ### CONSTANTS & FLAGS ###

    ANIM_STYLE_LOOP: int   = 0
    ANIM_STYLE_ONCE: int   = 1
    ANIM_STYLE_BOUNCE: int = 2

    ANIM_STATE_STOPPED: int = 0
    ANIM_STATE_RUNNING: int = 1
    ANIM_STATE_PAUSED:  int = 2


    ### FIELDS ###

    sprite_sheet: Surface      = None
    sprite_sheet_dims: Vector2 = None

    frames: list[Surface]      = None
    frame_size: Vector2        = None
    current_frame: Surface     = None
    current_frame_index: int   = None
    current_frame_time: float  = None
    
    frame_seconds: float       = None
    animation_style: int       = None
    animation_state: int       = None
    animation_time: float      = None


    ### CONSTRUCTOR ###

    def __init__(self,
        name: str,
        sprite_sheet_path: Path,
        sprite_sheet_dims: Vector2=None,
        frames_per_second: float=None,
        animation_style: int=None
    ):
        Component.__init__(self, name)

        # read in constructor arguments
        self.sprite_sheet = util.load_pixel_image(sprite_sheet_path)
        self.sprite_sheet_dims = sprite_sheet_dims if sprite_sheet_dims else DEFAULT_SPRITE_SHEET_DIMS

        if frames_per_second and frames_per_second > 0.0:
            self.frame_seconds = 1.0 / frames_per_second
        else:
            self.frame_seconds = DEFAULT_FRAME_SECONDS
        
        self.animation_style = animation_style if animation_style else DEFAULT_ANIM_STYLE

        # generate frames list
        n: int = int(self.sprite_sheet_dims.x) if self.sprite_sheet_dims.x > 1 else 1
        m: int = int(self.sprite_sheet_dims.y) if self.sprite_sheet_dims.y > 1 else 1

        w, h = self.sprite_sheet.get_size()
        
        frame_w: int = w / n if w % n == 0 else w
        frame_h: int = h / m if h % m == 0 else h
        self.frame_size = Vector2(frame_w, frame_h)

        # account for final frame size values in n, m
        n = n if frame_w != w else 1
        m = m if frame_h != h else 1

        self.frames = []
        for v in range(m):
            for u in range(n):
                self.frames.append(
                    self.sprite_sheet.subsurface(
                        [frame_w * u, frame_h * v],
                        [frame_w    , frame_h    ]
                    )
                )

        self.current_frame_index = 0
        self.current_frame_time  = 0.0
        self.animation_time      = 0.0
        self.animation_state     = Animation.ANIM_STATE_STOPPED

        self.current_frame = self.frames[self.current_frame_index]


    ### COMPONENT METHODS ###

    def on_attach(self): 
        if self.being:
            self.being.image = self.get_frame()
            self.being.rect.w = self.frame_size.x
            self.being.rect.h = self.frame_size.y


    def update(self, dt: float):
        if self.being:
            if self.animation_state == Animation.ANIM_STATE_RUNNING and self.frame_seconds:
                self.animation_time += dt
                self.current_frame_time += dt

                if self.current_frame_time >= self.frame_seconds:
                    self.current_frame_index += int(self.current_frame_time / self.frame_seconds)
                    self.current_frame_time %= self.frame_seconds

                    if self.animation_style == Animation.ANIM_STYLE_LOOP:
                        if self.current_frame_index >= len(self.frames):
                            self.current_frame_index %= len(self.frames)

                    elif self.animation_style == Animation.ANIM_STYLE_ONCE:
                        if self.current_frame_index >= len(self.frames):
                            self.current_frame_index = len(self.frames) - 1
                            self.animation_state = Animation.ANIM_STATE_PAUSED
            
            self.current_frame = self.frames[self.current_frame_index]            
            self.being.image = self.current_frame


    ### OPERATIONAL METHODS ###

    def start(self) -> tuple[int, float, float, int, int]:
        frame_index: int     = self.current_frame_index
        frame_time: float    = self.current_frame_time
        anim_time: float     = self.animation_time
        prev_anim_state: int = self.animation_state

        if self.animation_state != Animation.ANIM_STATE_RUNNING:
            self.animation_state = Animation.ANIM_STATE_RUNNING
            self.update(0)

        curr_anim_state: int = self.animation_state

        return frame_index, frame_time, anim_time, prev_anim_state, curr_anim_state


    def pause(self) -> tuple[int, float, float, int, int]:
        frame_index: int     = self.current_frame_index
        frame_time: float    = self.current_frame_time
        anim_time: float     = self.animation_time
        prev_anim_state: int = self.animation_state

        if self.animation_state == Animation.ANIM_STATE_RUNNING:
            self.animation_state = Animation.ANIM_STATE_PAUSED
            self.update(0)

        curr_anim_state: int = self.animation_state

        return frame_index, frame_time, anim_time, prev_anim_state, curr_anim_state


    def stop(self) -> tuple[int, float, float, int, int]:
        frame_index: int     = self.current_frame_index
        frame_time: float    = self.current_frame_time
        anim_time: float     = self.animation_time
        prev_anim_state: int = self.animation_state

        if self.animation_state != Animation.ANIM_STATE_STOPPED:
            self.current_frame_index = 0
            self.current_frame_time  = 0.0
            self.animation_time      = 0.0
            self.animation_state     = Animation.ANIM_STATE_STOPPED
            self.update(0)

        curr_anim_state: int = self.animation_state

        return frame_index, frame_time, anim_time, prev_anim_state, curr_anim_state
    

    ### AUXILIARY METHODS ###

    def get_frame(self, i: int=None) -> Surface:
        if i:
            if i in range(len(self.frames)):
                return self.frames[i]

            return None

        return self.current_frame



class Animator(Component):

    ### FIELDS ###

    animations: dict[str, Animation] = None
    current_animation: Animation     = None
    current_anim_name: str           = None


    ### CONSTRUCTOR ###

    def __init__(self,
        name: str,
        sprite_sheet_path: Path,
        sprite_sheet_dims: Vector2=None,
        frames_per_second: float=None,
        animation_style: int=None,
        default_anim_name: str=None
    ):
        Component.__init__(self, name)

        self.animations = {}
        self.animations['default'] = Animation(
            (default_anim_name if default_anim_name else DEFAULT_ANIM_NAME),
            sprite_sheet_path,
            sprite_sheet_dims,
            frames_per_second,
            animation_style
        )
        self.current_anim_name = default_anim_name if default_anim_name else 'default'
        if self.current_anim_name not in self.animations:
            self.animations[self.current_anim_name] = self.animations['default']
        self.current_animation = self.animations[self.current_anim_name]


    ### COMPONENT METHODS ###

    def on_attach(self):
        if self.being:
            self.being.attach(self.current_animation)


    def update(self, dt: float):
        self.current_animation = self.animations[self.current_anim_name]
        if self.being:
            self.being.attach(self.current_animation)


    def on_detach(self): 
        if self.being:
            self.being.detach(self.current_animation)


    ### WRAPPER METHODS ###

    def start(self):
        self.current_animation.start()


    def pause(self):
        self.current_animation.pause()


    def stop(self):
        self.current_animation.stop()


    ### OPERATIONAL METHODS ###

    def add_animation(self,
        anim_name: str,
        sprite_sheet_path: Path,
        sprite_sheet_dims: Vector2=Vector2(1),
        frames_per_second: float=2,
        animation_style: int=Animation.ANIM_STYLE_LOOP
    ) -> Animation:
        self.animations[anim_name] = Animation(
            anim_name,
            sprite_sheet_path,
            sprite_sheet_dims,
            frames_per_second,
            animation_style
        )

        return self.animations[anim_name]


    def set_animation(self, anim_name: str) -> Animation:
        if not anim_name or anim_name not in self.animations:
            return None

        self.current_anim_name = anim_name
        self.update(0)
        return self.current_animation



class Motor(Component):

    ### FIELDS ###

    move_vect: Vector2 = None


    ### COMPONENT METHODS ###

    def update(self, dt: float):
        if self.being:
            if self.move_vect:
                self.being.pos.x += self.move_vect.x * PIXEL_SIZE * dt
                self.being.pos.y += self.move_vect.y * PIXEL_SIZE * dt
                self.move_vect = None

    
    ### OPERATIONAL METHODS ###

    def move(self, move_vect: Vector2):
        self.move_vect = move_vect



class StepMotor(Motor):

    ### FEILDS ###

    step_size: int       = None
    min_step_time: float = None


    ### CONSTRUCTOR ###

    def __init__(self,
        name: str,
        step_size: int=None,
        steps_per_second: float=None
    ):
        Motor.__init__(self, name)

        self.step_size = step_size if step_size and step_size > 0 else DEFAULT_STEP_SIZE

        if steps_per_second and steps_per_second > 0.0:
            self.min_step_time = 1.0 / steps_per_second
        if not (self.min_step_time and self.min_step_time > 0.0):
            self.min_step_time = DEFAULT_MIN_STEP_TIME


    ### COMPONENT METHODS ###

    def update(self, dt: float):
        if self.being:
            pixel_step: int = PIXEL_SIZE * self.step_size

            if self.move_vect:
                self.being.pos.x += self.move_vect.x * pixel_step * dt / self.min_step_time
                self.being.pos.y += self.move_vect.y * pixel_step * dt / self.min_step_time
                self.move_vect = None
            
            #self.being.rect.x = int(self.being.pos.x / pixel_step) * pixel_step
            #self.being.rect.y = int(self.being.pos.y / pixel_step) * pixel_step


    ### WRAPPER METHODS ###

    def move(self, dir_vect: Vector2):
        super().move(dir_vect.normalize())
