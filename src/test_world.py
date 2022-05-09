
from pygame import Vector2

from being import Block, Ghost
from game import World


class TestWorld(World):

    block: Block = None
    ghost: Ghost = None


    def setup(self):
        self.block = Block()
        self.ghost = Ghost('ghost.ss.gif', Vector2(2, 2), pos=Vector2(650, 125))
        self.add(self.block, self.ghost)

    
    def update(self, dt: float):
        self.block.move(Vector2(80, 45))
        self.ghost.move(Vector2(-5, 0.0))
        self.world_group.update(dt)