import time

from engine.clock import Clock


class Engine:
    def __init__(self, gui, simulation, fps=60):
        self.gui = gui
        self.simulation = simulation
        self.clock = Clock(fps)
        self.running = False

    def loop(self):
        while self.running:
            print(time.time())
            # user input
            pass
            # simulation
            pass
            # render
            pass
            dt = self.clock.tick()

    def start(self):
        print("Стартую")
        self.running = True
        self.loop()

    def stop(self):
        self.running = False
        print("Остановился")