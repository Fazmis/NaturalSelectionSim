from .base_system import BaseSystem

class PrintAllSystem(BaseSystem):
    def __init__(self, component_manager):
        super().__init__(component_manager)

    def update(self, dt):
        for key, value in self.component_manager.entity_components.items():
            print(key, value)
