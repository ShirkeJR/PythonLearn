from Tkinter import *
import tkMessageBox


def helloButton1():
    tkMessageBox.showinfo("","Hello, here Tkinter")

def ChangeButtonColour():
   if(var.get() == 1):
       b.config(fg="red")
   elif(var.get() == 2):
       b.config(fg="green")
   elif(var.get() == 3):
       b.config(fg="blue")
       
def SelectColour():
   if(var.get() == 1):
       return "red"
   elif(var.get() == 2):
       return "green"
   elif(var.get() == 3):
       return "blue"


root = Tk()
root.title("Hello Tkinter")
root.geometry("200x100")
b1 = Button(root, text = "Witam", fg = "balck", command = helloButton1).pack()

MODES = [
        ("green", 1),
        ("red", 2),
        ("black", 3),
    ]
var = IntVar()
for text, mode in MODES:
    b = Radiobutton(root, text=text, variable = var, value=mode, command = ChangeButtonColour).pack(anchor=W)
label = Label(root).pack()
root.mainloop()
