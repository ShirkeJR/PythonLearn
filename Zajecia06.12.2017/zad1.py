from Tkinter import *
import Tkinter as tk
import tkMessageBox

okno = tk.Tk()

MODES = [
        ("czerwony", "red"),
        ("zielony", "green"),
        ("niebieski", "blue")
    ]


var = StringVar()
var.set("red")  # initialize
btn = Button(okno, text="Klik", command=lambda: tkMessageBox.showinfo("Hello in Tkinter"))


def changeColor():
    btn.configure(foreground=var.get())


for text, mode in MODES:
    b = Radiobutton(okno, text=text, variable=var, value=mode, command=changeColor).pack(anchor=W)

btn.pack(anchor=W)

okno.mainloop()