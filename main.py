from gui import DesktopApp
from simulation import SimulationsManager
from engine import Engine


def main():
    gui = DesktopApp()
    simulation = SimulationsManager()
    engine = Engine(gui=gui, simulation=simulation)
    engine.start()

if __name__ == '__main__':
    main()