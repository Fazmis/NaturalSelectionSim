class SystemManager:
    def __init__(self):
        self.systems = [

        ]

    def add_system(self, system):
        self.systems.append(system)

    def update(self, dt):
        for system in self.systems:
            system.update(dt)
        