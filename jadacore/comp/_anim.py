#################################
# _anim.py       [v0.0.1-alpha] #
#===============================#
#                               #
#-------------------------------#
# J Karstin Neill    05.12.2022 #
#################################


### IMPORTS ###

from pathlib import Path
import pygame
from pygame import Surface, Vector2

from jadacore.being import Component
from jadacore.meta import PIXEL_SIZE, RESOURCES_PATH


### CONSTANTS & FLAGS ###

DEFAULT_ANIM_NAME: str = 'anim_default'


### CLASS DEFINITIONS ###

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
        sprite_sheet_dims: Vector2=Vector2(1),
        frames_per_second: float=2,
        animation_style: int=ANIM_STYLE_LOOP
    ) -> None:
        Component.__init__(self, name)

        # read in constructor arguments
        sprite_sheet_raw: Surface = pygame.image.load(RESOURCES_PATH/sprite_sheet_path)
        self.sprite_sheet = pygame.transform.scale(
            sprite_sheet_raw.convert_alpha(),
            [
                sprite_sheet_raw.get_width()  * PIXEL_SIZE,
                sprite_sheet_raw.get_height() * PIXEL_SIZE
            ]
        )
        self.sprite_sheet_dims = sprite_sheet_dims if sprite_sheet_dims else Vector2(1)

        if frames_per_second and frames_per_second > 0.0:
            self.frame_seconds = 1.0 / frames_per_second
        
        self.animation_style = animation_style if animation_style else Animation.ANIM_STYLE_LOOP

        # generate frames list
        n: int = int(sprite_sheet_dims.x) if sprite_sheet_dims.x > 1 else 1
        m: int = int(sprite_sheet_dims.y) if sprite_sheet_dims.y > 1 else 1

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

    def on_attach(self) -> None: 
        if self.being:
            self.being.image = self.get_frame()
            self.being.rect.w = self.frame_size.x
            self.being.rect.h = self.frame_size.y


    def update(self, dt: float) -> None:
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


    def on_detach(self) -> None: pass


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
            if i >= 0 and i < len(self.frames):
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
        sprite_sheet_dims: Vector2=Vector2(1),
        frames_per_second: float=2,
        animation_style: int=Animation.ANIM_STYLE_LOOP,
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

    def on_attach(self) -> None:
        if self.being:
            self.being.attach_component(self.current_animation)


    def update(self, dt: float) -> None:
        self.current_animation = self.animations[self.current_anim_name]
        if self.being:
            self.being.attach_component(self.current_animation)


    def on_detach(self) -> None: 
        if self.being:
            self.being.detach_component(self.current_animation)


    ### OPERATIONAL METHODS ###

    def start(self) -> None:
        self.current_animation.start()


    def pause(self) -> None:
        self.current_animation.pause()


    def stop(self) -> None:
        self.current_animation.stop()


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
