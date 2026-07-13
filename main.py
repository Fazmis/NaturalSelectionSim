from gui import DesktopApp
from simulation import SimulationsManager
from engine import Engine


def main() -> None:
    gui = DesktopApp()
    simulation = SimulationsManager()
    engine = Engine(gui=gui, simulation=simulation, fps=1)
    engine.start()

if __name__ == '__main__':
    main()