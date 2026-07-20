from .base_system import BaseSystem
from ..components import Velocity, Position
from random import randint

class MovementSystem(BaseSystem):
    def __init__(self, component_manager):
        super().__init__(component_manager)

    def update(self, dt):
        components = self.component_manager.query(Position, Velocity)

        if not components:
            return

        for position, velocity in components:
            velocity.speed_x += randint(-1, 1)
            velocity.speed_y += randint(-1, 1)
            position.x += velocity.speed_x * dt
            position.y += velocity.speed_y * dt