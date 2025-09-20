import tkinter
from tkinter import messagebox


def work_message () :
    root = tkinter.Tk()
    root.withdraw()
    messagebox.askokcancel("","---> Work time <---")

work_message()