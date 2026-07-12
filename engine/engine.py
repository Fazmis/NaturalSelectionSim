import time as t


class Engine:
    def __init__(self, gui, simulation):
        self.gui = gui
        self.simulation = simulation
        self.tick = 10
        self.running = False

    def loop(self):
        while self.running:
            t0 = t.time()
            print("Работаю")
            # user input
            pass
            # simulation

            pass
            # render

    def start(self):
        print("Стартую")
        self.running = True
        self.loop()

    def stop(self):
        self.running = False
        print("Остановился")