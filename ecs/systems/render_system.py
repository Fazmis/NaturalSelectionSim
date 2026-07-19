from simulation.systems.base_system import BaseSystem
from simulation.components import Position, RenderAble


class RenderSystem(BaseSystem):
    def __init__(self, component_manager):
        super().__init__(component_manager)

    def get_render_data(self):
        render_data = self.component_manager.query(Position, RenderAble)
        return render_data
