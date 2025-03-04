# import requests

# def gen_random_word() -> str:

#     api_url = "https://api.api-ninjas.com/v1/randomword"
#     response = requests.get(api_url, headers={"X-Api-Key": "iobLA+aelJyLQz1xjspPng==oJSGEbMMctKjKzTC"})
#     if response.status_code == requests.codes.ok:
#         index_1 = response.text.find("[") + 2
#         index_2 = response.text.rfind("]") - 1
#         return response.text[index_1: index_2]
#     else:
#         print("Error:", response.status_code, response.text)
#         return None
    
# def get_word_description(word) -> str:
#     api_url = "https://api.dictionaryapi.dev/api/v2/entries/en/" + word
#     response = requests.get(api_url)

#     if response.status_code == requests.codes.ok:
#         res_text = response.text

#         index_meaning = res_text.find("meanings") + len('meanings')
#         res_text = res_text[index_meaning: -1]

#         index_def = res_text.find('[{"definition":') + len('[{"definition":"')
#         res_text = res_text[index_def: -1]
        
#         end_index = res_text.find('",')
#         res_text = res_text[0: end_index]
#         return res_text
#     else:
#         print("Error:", response.status_code, response.text)
#         return None
        

# get_word_description("oversimplification")


import tkinter as tk
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


def movex(widget, xreset_pos, xpace=1, xreset_value=0):
    xcord, ycord = widget.winfo_x() + xpace, widget.winfo_y()
    if xcord == xreset_pos:
        xcord = xreset_value
    widget.place(x=xcord, y=ycord)

def cloud_motion_xcord(root):
    root.update()
    for i in range(5):
        widget = root.nametowidget(f"cloud{i}")
        movex(
            widget=widget,
            xreset_pos=500,
            xreset_value=-100,
            xpace=1,
        )
    root.after(50, root.cloud_motion_xcord)

def make_clouds(self):
    xcordinates = (329, 50, 163, 282, 23)
    ycords = (20, 250, 400, 500, 600)
    for i, xcord in enumerate(xcordinates):
        cloud_display = tk.Label(self, image=self.cloud_img, bg="white", name=f"cloud{i}")
        cloud_display.config(image = self.cloud_img)
        cloud_display.place(x=xcord, y=ycords[i])
    self.cloud_motion_xcord()

class PlaceholderedEntry(tk.Entry):
    def __init__(self, master=None, placeholder= "", **options):
        self.placeholder = placeholder
        super().__init__(master, **options)

        self.bind("<FocusIn>", self.foc_in)
        self.bind("<FocusOut>", self.foc_out)
        self.add_placeholder()
        
    def add_placeholder(self):
        self.insert(0, self.placeholder)

    def foc_in(self, event): 
        self.delete(0, len(self.placeholder))
            
    def foc_out(self, event): 
        self.add_placeholder()

class SetupEntry(PlaceholderedEntry):
    def __init__(self, master=None, placeholder="", name= None):
        super().__init__(master, placeholder, name= name, background= "white", borderwidth= "25", font= "Courier 15", foreground= "black", highlightbackground= "#5185b4", highlightthickness= "3", relief= "flat")
        self.indicate_normal()

    def indicate_error(self, error_text, timeout=500):
        self.configure(highlightcolor="red", highlightbackground="red")

        error_label = tk.Label(self, text=error_text, background="white", font="Courier 15", foreground="SystemWindowText", anchor="w", padx=0, pady=0)
        error_label.pack(fill="x")
        error_label.after(timeout, error_label.destroy)

        self.after(timeout, self.indicate_normal)
    
    def indicate_normal(self):
        self.configure(highlightcolor="green", highlightbackground="#5185b4")