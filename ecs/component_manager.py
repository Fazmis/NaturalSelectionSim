class ComponentManager:
    def __init__(self):
        self.entity_components = {} # entity_id: (components)
        self.component_entities = {} # component_type: id: component_obj

    def add_entity(self, entity_id:int, components:set|list):
        self.entity_components[entity_id] = components
        for component in components:
            self._add_component(component, entity_id)

    def _add_component(self, component, entity_id):
        if type(component) not in self.component_entities:
            self.component_entities[type(component)] = dict()
        self.component_entities[type(component)][entity_id] = component

    def query(self, *components_types) -> list[list] | None:
        if not components_types:
            return None

        keys = self.component_entities[components_types[0]].keys()
        for component in components_types[1:]:
            keys &= self.component_entities[component].keys()
        query = []
        for key in keys:
            selected_components = []
            for component in components_types:
                selected_components.append(self.component_entities[component][key])
            query.append(selected_components)
        return query