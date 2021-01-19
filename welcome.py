import tkinter as tk
import colors as c
from game import Game


class Welcome(tk.Frame):
    flag = 0
    newWindow = None

    def __init__(self, master):
        self.master = master
        self.frame = tk.Frame(self.master)
        self.master.title('2048')
        tk.Frame.__init__(self)
        self.main_grid = tk.Frame(
            self, bg=c.GRID_COLOR, bd=5, width=400, height=400)
        self.main_grid.grid(pady=(0, 0))
        self.grid()
        button1 = tk.Button(self, text='New Game', command=lambda: self.new_window())
        button1.grid(row=0, column=0, padx=10, pady=10)
        button1.config(height=2, width=15)


    def new_window(self):
        try:
            if (self.flag  == 0):
                self.newWindow = tk.Toplevel(self.master)

            frame = Game(self.newWindow, self)
            frame.tkraise()
            self.flag = 1

        except Exception as e:
            print(str(e))
            text = tk.Label(self.master, bg=c.WARNING, text="You cannot open more than one game!")
            text.grid(row=1, column=0, padx=0, pady=10)
            text.config(height=2, width=40)

        def on_close():
            self.master.destroy()

        self.newWindow.protocol("WM_DELETE_WINDOW", on_close)
