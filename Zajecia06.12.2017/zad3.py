from Tkinter import *
def dodaj(e1, e2):
    e1 + e2

root = Tk()
e1 = Entry(root, text = "0")
e2 = Entry(root, text = "0")
b1 = Button(root, text = "+", variable = (e1, e2), command = dodaj).pack()

e1.pack()
e2.pack()
root.mainloop()