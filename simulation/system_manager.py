class SimulationsManager:
    def __init__(self):
        self.simulations = [

        ]

    def simulate(self):
        for simulation in self.simulations:
            simulation.simulate()
        