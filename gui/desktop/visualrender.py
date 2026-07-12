import tkinter as tk

class VisualRender:
    def __init__(self, root, width=100, height=100):
        self.canvas = tk.Canvas(root, width=width, height=height)
        self.canvas.pack()