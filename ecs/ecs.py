from ecs.entity_manager import EntityManager
from ecs.component_manager import ComponentManager
from ecs.system_manager import SystemManager


class Ecs:
    def __init__(self):
        self.entity_manager = EntityManager()
        self.component_manager = ComponentManager()
        self.system_manager = SystemManager()

    def simulate(self, dt):
        self.system_manager.simulate(dt)
