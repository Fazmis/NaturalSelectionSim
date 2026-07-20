from .base_system import BaseSystem
from ..components import Health


class DeathSystem(BaseSystem):
    def __init__(self, component_manager):
        super().__init__(component_manager)

    def update(self, dt):
        components = self.component_manager.query(Health)

        if not components:
            return

        for health in components:
            if health.hp <= 0:
                self.component_manager.delete_entity(health)
                print(f"Entity {health.entity_id} died")