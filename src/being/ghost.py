#################################
# ghost.py       [v0.0.1-alpha] #
#===============================#
#                               #
#-------------------------------#
# J Karstin Neill    05.06.2022 #
#################################


### IMPORTS ###

from pathlib import Path
from pygame import Surface, Vector2

from . import Being


### CONSTANTS & FLAGS ###

class AnimationStyle:
    ANIM_STYLE_LOOP:   int = 0
    ANIM_STYLE_ONCE:   int = 1
#    ANIM_STYLE_BOUNCE: int = 2


### CLASS DEFINITIONS ###

class Ghost(Being):

    ### FIELDS ###

    frames: list[Surface]     = None
    current_frame_index: int  = None
    current_frame_time: float = None
    frame_seconds: float      = None
    animation_style: int      = None
    animation_running: bool   = None


    ### CONSTRUCTOR ###

    def __init__(
        self,
        ghost_path: Path,
        sprite_sheet_size: Vector2=Vector2(1),
        frames_per_second: float=2,
        animation_style: int=AnimationStyle.ANIM_STYLE_LOOP,
        **kwargs
    ) -> None:
        Being.__init__(self, image_path=ghost_path, **kwargs)

        if frames_per_second and frames_per_second > 0.0:
            self.frame_seconds = 1.0 / frames_per_second
        self.animation_style = animation_style if animation_style else AnimationStyle.ANIM_STYLE_LOOP
        self.animation_running = False
    
        n = int(sprite_sheet_size.x) if sprite_sheet_size.x > 1 else 1
        m = int(sprite_sheet_size.y) if sprite_sheet_size.y > 1 else 1

        w, h = self.image.get_size()
        
        frame_w: int = w / n if w % n == 0 else w
        frame_h: int = h / m if h % m == 0 else h

        self.frames = []
        for v in range(m):
            for u in range(n):
                self.frames.append(
                    self.image.subsurface(
                        (frame_w * u), (frame_h * v), 
                        frame_w, frame_h
                    )
                )
        
        if len(self.frames) == 0: self.frames = None

        if self.frames:
            self.current_frame_index = 0
            self.current_frame_time  = 0.0
            self.animation_running   = True
            self.image = self.frames[self.current_frame_index]

        self.rect.w = frame_w
        self.rect.h = frame_h


    ### METHODS ###

    def update(self, dt: float) -> None:
        super().update(dt)

        if self.animation_running and self.frame_seconds:
            self.current_frame_time += dt

            if self.current_frame_time >= self.frame_seconds:
                self.current_frame_time %= self.frame_seconds
                self.current_frame_index += 1

                if self.animation_style == AnimationStyle.ANIM_STYLE_LOOP:
                    if self.current_frame_index >= len(self.frames):
                        self.current_frame_index %= len(self.frames)

                    self.image = self.frames[self.current_frame_index]

                elif self.animation_style == AnimationStyle.ANIM_STYLE_ONCE:
                    if self.current_frame_index >= len(self.frames):
                        self.animation_running = False

                    else:
                        self.image = self.frames[self.current_frame_index]
                        
