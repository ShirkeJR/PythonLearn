#prosty sekundnik
from Tkinter import *
import tkMessageBox


def helloButton1():
    tkMessageBox.showinfo("","Czas sie skonczyl")

def buttonStart():
    pass


root = Tk()
root.title("Hello Tkinter")
label = Label(root).configure(text = "100")

b1 = Button(root, text = "Witam", variable = label, command = buttonStart).pack()


root.mainloop()