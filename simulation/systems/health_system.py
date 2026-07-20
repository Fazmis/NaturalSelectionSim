from .base_system import BaseSystem
from ..components import Health, Hunger


class HealthSystem(BaseSystem):
    def __init__(self, component_manager):
        super().__init__(component_manager)

    def update(self, dt):
        components = self.component_manager.query(Health, Hunger)

        if not components:
            return

        for health, hunger in components:
            if not hunger.level:
                health.hp -= 1 * dt
