import tkinter as tk
from gui.desktop.visualrender import VisualRender

class DesktopApp:
    def __init__(self):
        self.WIDTH = 1024
        self.HEIGHT = 512
        self.root = tk.Tk()
        self.visual_render = VisualRender(self.root, self.WIDTH, self.HEIGHT)
        self.root.mainloop()

    def render(self, render_data):
        pass