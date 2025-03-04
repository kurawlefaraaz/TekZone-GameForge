import tkinter as tk

class Cell(tk.Button):
    """
    parem name: format- "cell_r,c
    """
    def __init__(self, master, name, **options): 
        super().__init__(master, name=name, relief="flat", width=5, height=2, font="Times 15 bold", fg="black",**options)

        self._mine = 0
        self._flag = 0
    
    @property
    def is_mine(self):
        return self._mine
    
    def setmine(self):
        self._mine = 1
    
    @property
    def flag(self):
        return self._flag
    
    def deflag(self):
        self.configure(text="", state="normal", background="white")
        self._flag = 0
    
    def setflag(self):
        self.configure(state="disabled", text="F", bg="red", disabledforeground="white")
        self._flag = 1

    #def deter_fg_color(self, text):
     #   if text 
    
    def settext(self, text):
        self.configure(relief="sunken")
        self.update()
        self.after(150)
        self.configure(state= "disabled", text=text)

class Grid(tk.Frame):
    from random import sample
    CELLS = {}
    CELL_COUNT = 0

    MINES = []
    MINE_COUNT = (CELL_COUNT ** 2) // 4

    def __init__(self, master):
        super().__init__(master)
        
        for r in range(5):
            for c in range(5):
                if (r+c)%2: bg="white"
                else: bg="cyan"
                cell = Cell(self, f"cell_{r},{c}", bg=bg)
                cell.bind("<Button-1>", self.first_left_click_act)
                
                cell.grid(row=r, column=c)
                Grid.CELLS.update({f"{r},{c}": cell})

                Grid.CELL_COUNT += 1

    def show_mines(self):
        for mine in Grid.MINES:
            mine.settext("*")

    @staticmethod
    def get_surrounding_cells(widget):
        x= widget.grid_info()["row"]
        y= widget.grid_info()["column"]
        cells = [
            Grid.CELLS.get(f"{x - 1},{y - 1}"),
            Grid.CELLS.get(f"{x - 1},{y}"),
            Grid.CELLS.get(f"{x - 1},{y + 1}"),
            Grid.CELLS.get(f"{x},{y + 1}"),
            Grid.CELLS.get(f"{x + 1},{y + 1}"),
            Grid.CELLS.get(f"{x + 1},{y}"),
            Grid.CELLS.get(f"{x + 1},{y - 1}"),
            Grid.CELLS.get(f"{x},{y - 1}")
        ]
        return tuple(filter(lambda cell: bool(cell), cells))
    
    def surrounding_mines_count(self, widget): 
        count = 0
        for cell in self.get_surrounding_cells(widget):
            if cell.is_mine:
                count += 1

        return count

    @staticmethod
    def used_cells():
        opened_count = 0
        flag_count = 0
        for cell in Grid.CELLS.values():
            if cell.cget("state") == "disabled" and not cell.flag: opened_count += 1
            elif cell.flag: flag_count += 1

        return (opened_count + flag_count)

    def finish(self): 
        good_cells = Grid.CELL_COUNT - Grid.MINE_COUNT

        if good_cells == self.used_cells(): return 1
        else: return 0
    
    def gameover(self, gamestate):
        if gamestate: print("you won")
        else: 
            self.show_mines()
            print("you lose")

    def first_left_click_act(self, event):
        button = event.widget
        surrounding_cells = self.get_surrounding_cells(button)
        filtered_cells = tuple(filter(lambda cell: 0 if cell in surrounding_cells else 1, Grid.CELLS.values()))
        Grid.MINES = Grid.sample(filtered_cells, 5)
        Grid.MINE_COUNT = len(Grid.MINES)

        for cell in Grid.MINES:
            cell.setmine()
        
        for cell in Grid.CELLS.values():
            cell.bind("<Button-1>", self.left_click_act)
            cell.bind("<Button-3>", self.right_click_act)
        
        count = self.surrounding_mines_count(button)
        button.settext(count if count else "")

    def left_click_act(self, event): 
        widget = event.widget
        if (widget.cget("state") == "disabled" or widget.flag): return None
        
        count = self.surrounding_mines_count(widget)
        widget.settext(count if count else "")

        if widget.is_mine: return self.gameover(0)
        elif self.finish(): return self.gameover(1)
        
    def right_click_act(self, event):
        cell = event.widget
        cstate = cell.cget("state")

        if cell.flag and cstate == "disabled": cell.deflag()
        elif cstate != "disabled": cell.setflag()

        if self.finish(): return self.gameover(1)

def test():
    root = tk.Tk()
    Grid(root).pack()
    root.mainloop()

if __name__ == "__main__":
    test()
