from .base_system import BaseSystem
from ..components import Position, Velocity


class BordersSystem(BaseSystem):
    def __init__(self, component_manager, size: tuple[int, int] = (512, 512) ):
        super().__init__(component_manager)
        self.x_border = (0 - size[0] // 2, size[0] // 2)
        self.y_border = (0 - size[1] // 2, size[1] // 2)


    def update(self, dt):
        components = self.component_manager.query(Position, Velocity)

        if not components:
            return

        for position, velocity in components:
            position.x = max(self.x_border[0], min(self.x_border[1], position.x))
            position.y = max(self.y_border[0], min(self.y_border[1], position.y))
            if position.x in self.x_border:
                velocity.speed_x = 0
            if position.y in self.y_border:
                velocity.speed_y = 0