class SystemManager:
    def __init__(self):
        self.systems = [

        ]

    def simulate(self, dt):
        for system in self.systems:
            system.update(dt)
        