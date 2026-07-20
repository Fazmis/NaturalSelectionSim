from .components import Position, Velocity, Health, RenderAble, Hunger
from .systems import PrintAllSystem, MovementSystem, BordersSystem, HungerSystem, HealthSystem, DeathSystem


class Simulation:
    def __init__(self, ecs):
        self.ecs = ecs

    def initialize(self):
        for _ in range(10):
            species = [
                Position(0, 0),
                Velocity(),
                Health(5),
                RenderAble(),
                Hunger(level=0),
                       ]
            self.ecs.add_entity(species)

        self.ecs.add_system(PrintAllSystem)
        self.ecs.add_system(MovementSystem)
        self.ecs.add_system(BordersSystem)
        self.ecs.add_system(HealthSystem)
        self.ecs.add_system(HungerSystem)
        self.ecs.add_system(DeathSystem)

    def simulate(self, dt):
        self.ecs.update(dt)

    def get_render_data(self):
        return self.ecs.get_render_data()