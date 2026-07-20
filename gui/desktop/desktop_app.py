import tkinter as tk
from gui.desktop.visualrender import VisualRender

class DesktopApp:
    def __init__(self):
        self.WIDTH = 1024
        self.HEIGHT = 512
        self.root = tk.Tk()
        self.visual_render = VisualRender(self.root, self.WIDTH, self.HEIGHT)
        self.fps_label = tk.Label(self.root)
        self.fps_label.pack()
        self.root.update()

    def render(self, render_data, dt):
        self.visual_render.render(render_data)
        dt = max(dt, 0.001)
        fps = 1/dt
        self.draw_fps(fps)
        self.root.update()

    def draw_fps(self, fps):
        self.fps_label.configure(text=fps)
        self.fps_label.update()