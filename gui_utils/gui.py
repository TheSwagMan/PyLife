import tkinter as tk

class Gui(tk.Tk):
    def __init__(self):
        super().__init__()
        self.bind("<<close>>", self.close)

    def close(self, *args):
        self.destroy()
