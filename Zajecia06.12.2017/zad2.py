from Tkinter import *

def ShowTimer(s):
    while (s >= 0):
        e.config(text=s)
        s = s - 1
        if (s == 0):
            e.config(text="Zakonczono odliczanie")


root = Tk()
root.title("Timer")
e = Label(root)
b1 = Button(root, text="Start", command=lambda: ShowTimer(100))
e.grid(row=0, column=0, columnspan=2)
b1.grid(row=1, column=0)
root.mainloop()
