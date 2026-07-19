from engine.clock import Clock


class Engine:
    def __init__(self, gui, simulation, fps=60):
        self.gui = gui
        self.simulation = simulation
        self.clock = Clock(fps)
        self.running = False

    def loop(self):
        dt = 0

        while self.running:
            print(dt)
            # user input
            pass
            # simulation
            self.simulation.simulate(dt)
            # render
            render_data = self.simulation.get_render_data()
            self.gui.render(render_data)

            dt = self.clock.tick()

    def start(self):
        print("Стартую")
        self.running = True
        self.clock.reset()
        self.loop()

    def stop(self):
        self.running = False
        print("Остановился")