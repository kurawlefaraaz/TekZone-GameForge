import tkinter as tk, sys

sys.path.append(r"C:\Users\Faraaz\Documents\Programming\Python\Tk Creator\Refactorised")
from tkinter_builder import GUI

class BorderedButton(tk.Button):
    def __init__(self, master, name=None, text="", command=None, font=None):
        nbg, nfg= ("white", "black")
        afg, abg = (nbg, nfg)

        self.border_frame = tk.Frame(master, highlightthickness=2, borderwidth=0, highlightbackground=nfg)
        super().__init__(self.border_frame, name=name, text=text, command=command,  borderwidth=0, border=0, width=20, padx=0, pady=0, relief="flat", font=font, activebackground=abg, activeforeground=afg, background=nbg, foreground=nfg)
        super().pack()

        text_meths = vars(tk.Button).keys()
        methods = vars(tk.Pack).keys() | vars(tk.Grid).keys() | vars(tk.Place).keys()
        methods = methods.difference(text_meths)

        for m in methods:
            if m[0] != '_' and m != 'config' and m != 'configure':
                setattr(self, m, getattr(self.border_frame, m))

class Home(tk.Tk):
    def __init__(self):
        super().__init__()
        self.geometry("500x700")
        self.resizable(0,0)

        self.title("Mine Sweeper")
        self.configure(bg="white")

        self.cloud_img = tk.PhotoImage(name="cloud_img", master=self, file="./assets/cloud.png")
        self.logo_img = tk.PhotoImage(name="logo_img", master=self, file="./assets/logo.png")

        self.make_clouds()
        self.add_buttons()

    @staticmethod
    def movex(widget, xreset_pos, xpace=1, xreset_value=0):
        xcord, ycord = widget.winfo_x() + xpace, widget.winfo_y()
        if xcord == xreset_pos:
            xcord = xreset_value
        widget.place(x=xcord, y=ycord)

    def cloud_motion_xcord(self):
        self.update()
        for i in range(5):
            widget = self.nametowidget(f"cloud{i}")
            self.movex(
                widget=widget,
                xreset_pos=500,
                xreset_value=-100,
                xpace=1,
            )
        self.after(50, self.cloud_motion_xcord)

    def make_clouds(self):
        xcordinates = (329, 50, 163, 282, 23)
        ycords = (20, 250, 400, 500, 600)
        for i, xcord in enumerate(xcordinates):
            cloud_display = tk.Label(self, image=self.cloud_img, bg="white", name=f"cloud{i}")
            cloud_display.config(image = self.cloud_img)
            cloud_display.place(x=xcord, y=ycords[i])
        self.cloud_motion_xcord()

    def add_buttons(self):
        logo = tk.Label(
            self,
            image=self.logo_img,
            bg="white",
            relief="flat",
            fg="white",
        )
        logo.place(relx=0.5, rely=0.25, anchor="center")

        rely=0.5
        for text in ("Play!", "How to play?", "Settings"):
            BorderedButton(self, font="times 15 bold", text=text).place(relx=0.5, rely=rely, anchor="center")
            rely+=0.1

if __name__ == "__main__":
    Home().mainloop()
