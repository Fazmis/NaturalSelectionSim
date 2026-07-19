class ComponentManager:
    def __init__(self):
        self.entity_components_dict = {} # entity_id: (components)
        self.component_entities_dict = {} # component: (entity_id's)

    def add_entity(self, entity_id:int, components:set|list):
        self.entity_components_dict[entity_id] = components
        for component in components:
            self._add_component(component, entity_id)

    def _add_component(self, component, entity_id):
        if type(component) not in self.component_entities_dict:
            self.component_entities_dict[type(component)] = dict()
        self.component_entities_dict[type(component)][entity_id] = component

    def queue(self, *components_types):
        queue = self.component_entities_dict[components_types[0]]
        for component in components_types[1:]:
            queue = queue & component
        return queue
