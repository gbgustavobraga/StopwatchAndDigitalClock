
from tkinter import *
from tkinter.ttk import *

from time import strftime, time, process_time
from tracemalloc import stop
from turtle import update

from pip import main
from soupsieve import select_one

root = Tk()
root.title("Clock")

def time():
    string = strftime("%H:%M:%S")
    label.config(text=string)
    label.after(1000, time)

label = Label(root, font = ("DS-Digital", 140), background ="black", foreground = "red")
label.pack(anchor = "center")
time()
mainloop()