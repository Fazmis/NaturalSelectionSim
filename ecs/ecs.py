from ecs.entity_manager import EntityManager
from ecs.component_manager import ComponentManager
from ecs.system_manager import SystemManager


class Ecs:
    def __init__(self):
        self.entity_manager = EntityManager()
        self.component_manager = ComponentManager()
        self.system_manager = SystemManager()

    def update(self, dt):
        self.system_manager.simulate(dt)

    def create_entity(self, components: set):
        entity_id = self.entity_manager.create_entity()
        self.component_manager.add_entity(entity_id, components)

    def add_component(self, component):
        self.component_manager.add_component()

    def add_system(self, system):
        self.system_manager.add_system()
