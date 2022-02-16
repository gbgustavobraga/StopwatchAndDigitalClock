from tkinter import *
from tkinter.ttk import *

from time import strftime


def digitalclock():
    root = Tk()
    root.title("Digital Clock")

    def clock():
        string = strftime("%H:%M:%S")
        label.config(text=string)
        label.after(1000, clock)

    label = Label(root, font=("DS-Digital", 140), background="black", foreground="red")
    label.pack(anchor="center")
    clock()
    mainloop()


digitalclock()