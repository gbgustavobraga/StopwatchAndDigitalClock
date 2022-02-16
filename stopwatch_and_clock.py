from models import digital_clock, stopwatch

from tkinter import *


def main() -> None:
    _main_()


def _main_():
    clock = digital_clock.digitalclock
    stopowatch = stopwatch.watch

    main_window = Tk()
    main_window.title("Stopwatch and Clock")
    main_window.geometry("240x90")

    pane = Frame(main_window)
    pane.pack(fill=BOTH, expand=True)

    text_stopwatch = Button(pane, text="STOPWATCH", height=5, width=14, font=('Arial', 10),command=stopowatch)
    text_stopwatch.pack(side=LEFT, expand=True, fill=BOTH)

    text_clock = Button(pane, text="DIGITAL CLOCK", height=5, width=14, font=('Arial', 10), command=clock)
    text_clock.pack(side=LEFT, expand=True, fill=BOTH)

    main_window.mainloop()


if __name__ == '__main__':
    main()
