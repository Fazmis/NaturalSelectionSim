from ecs.component_manager import ComponentManager

class BaseSystem:
    def __init__(self, component_manager:ComponentManager):
        self.component_manager = component_manager