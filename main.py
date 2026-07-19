from gui import DesktopApp
from ecs import Ecs
from simulation import Simulation
from engine import Engine


def main() -> None:
    gui = DesktopApp()
    ecs = Ecs()
    simulation = Simulation(ecs)
    simulation.initialize()
    engine = Engine(gui=gui, simulation=simulation, fps=1)
    engine.start()

if __name__ == '__main__':
    main()