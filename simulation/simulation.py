from .components import Position, Velocity, Health, RenderAble
from .systems import PrintAllSystem, MovementSystem


class Simulation:
    def __init__(self, ecs):
        self.ecs = ecs

    def initialize(self):
        for _ in range(10):
            species = [
                Position(0, 0),
                Velocity(),
                Health(10),
                RenderAble(),
                       ]
            self.ecs.add_entity(species)

        self.ecs.add_system(PrintAllSystem)
        self.ecs.add_system(MovementSystem)


    def simulate(self, dt):
        self.ecs.update(dt)

    def get_render_data(self):
        return self.ecs.get_render_data()