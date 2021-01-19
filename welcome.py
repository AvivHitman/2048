import tkinter as tk
from tkinter import *

import colors as c
from game import Game


class Welcome(tk.Frame):
    flag = 0
    new_window = None
    
    def __init__(self, master):
        self.master = master
        self.frame = tk.Frame(self.master)
        self.master.title('2048')
        tk.Frame.__init__(self)
        self.main_grid = tk.Frame(
            self, bg=c.GRID_COLOR, bd=5, width=400, height=400)
        self.main_grid.grid(pady=(0, 0))
        self.grid()
        button1 = tk.Button(self, text='New Game', command=lambda: self.create_new_window())
        button1.grid(row=0, column=0, padx=10, pady=10)
        button1.config(height=2, width=15)

    def on_close(self):
        self.master.destroy()

    def create_new_window(self):
        try:
            if (self.flag  == 0):
                self.new_window = tk.Toplevel(self.master)

            frame = Game(self.new_window, self)
            frame.tkraise()
            self.flag = 1

        except:
            print("You cannot create another Game window")
            text = tk.Label(self.master, bg=c.WARNING, text="You cannot open more then one game!")
            text.grid(row=1, column=0, padx=0, pady=10)
            text.config(height=2, width=40)

        self.new_window.protocol("WM_DELETE_WINDOW", self.on_close)