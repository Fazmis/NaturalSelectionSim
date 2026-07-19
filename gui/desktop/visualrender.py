import tkinter as tk

class VisualRender:
    def __init__(self, root, width=100, height=100):
        self.width = width
        self.height = height
        self.canvas = tk.Canvas(root, width=self.width, height=self.height)
        self.canvas.pack()

    def render(self, render_data):
        self.canvas.delete("all")

        for item in render_data:
            position, obj = item
            if obj.shape == "circle":
                self.canvas.create_oval(
                    position.x + self.width//2,
                    position.y + self.height//2,
                    position.x + self.width//2 + obj.size,
                    position.y + self.height//2 + obj.size,
                    fill="green"
                )