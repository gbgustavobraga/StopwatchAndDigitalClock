from models import digital_clock, stopwatch

from tkinter import *


def main() -> None:
    _main_()


def _main_():
    clock = digital_clock.digitalclock
    stopowatch = stopwatch.stopwatch
    main_window = Tk()
    main_window.title("Stopwatch and Clock")
    main_window.geometry("290x200")

    text_title = Label(main_window, text="Click on your Option")
    text_title.grid(column=4, row=2)

    text_stopwatch = Button(main_window, text="STOPWATCH", command=stopowatch)
    text_stopwatch.grid(column=1, row=10)

    text_clock = Button(main_window, text="DIGITAL CLOCK", command=clock)
    text_clock.grid(column=6, row=10)
    main_window.mainloop()


if __name__ == '__main__':
    main()
