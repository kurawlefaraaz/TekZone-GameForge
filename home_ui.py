import tkinter as tk
from utils import BorderedButton

class Home(tk.Frame):
    def __init__(self, master):
        super().__init__(master, name="home", bg="white")

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
        for text in ("Play!", "How to play?", "About"):
            BorderedButton(self, font="times 15 bold", text=text).place(relx=0.5, rely=rely, anchor="center")
            rely+=0.1