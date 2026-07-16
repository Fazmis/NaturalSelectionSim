class ComponentManager:
    def __init__(self):
        self.entity_components_dict = {} # entity_id: (components)
        self.component_entities_dict = {} # component: (entity_id's)

    def add_entity(self, entity_id, components):
        self.entity_components_dict[entity_id] = components
        for component in components:
            if type(component) not in self.component_entities_dict:
                self.component_entities_dict[type(component)] = set()
            self.component_entities_dict[type(component)].add(entity_id)

    def add_component(self, component):
        pass
