from Tkinter import *
import tkMessageBox


def helloButton1():
    tkMessageBox.showinfo("","Hello, here Tkinter")

def buttonColor():
    b1.configure(foreground = text)

root = Tk()
root.title("Hello Tkinter")
b1 = Button(root, text = "Witam", command = helloButton1).pack()

MODES = [
        ("green", 1),
        ("red", 2),
        ("black", 3),
    ]

for text, mode in MODES:
    b = Radiobutton(root, text=text, variable = (b1, text), value=mode).pack(anchor=W)
label = Label(root).pack()
root.mainloop()