import tkinter as tk
from home_ui import Home

class GUI(tk.Tk):
    def __init__(self):
        super().__init__()
        self.geometry("500x700")
        self.resizable(0,0)

        self.title("Word Scramble")

        Home(self).pack(fill="both", expand=1)

if __name__ == "__main__":
    GUI().mainloop()
