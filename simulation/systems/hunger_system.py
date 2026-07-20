from .base_system import BaseSystem
from ..components import Hunger


class HungerSystem(BaseSystem):
    def __init__(self, component_manager):
        super().__init__(component_manager)

    def update(self, dt):
        components = self.component_manager.query(Hunger)

        if not components:
            return

        for hunger in self.component_manager.query(Hunger):
            hunger.level = max(0, hunger.level - 1 * dt)
