from gui import DesktopApp
from simulation import Simulation
from engine import Engine


def main() -> None:
    gui = DesktopApp()
    simulation = Simulation()
    engine = Engine(gui=gui, simulation=simulation, fps=1)
    engine.start()

if __name__ == '__main__':
    main()