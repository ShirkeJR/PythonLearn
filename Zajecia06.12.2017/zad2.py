#prosty sekundnik
from Tkinter import *
import tkMessageBox


def ShowTimer():
   s = int(e.get())
   
   if(s == 0 or s < 0):
       messagebox.showinfo("Message", "Time has expired!")
       return
   else:
       e.delete(0, END)
       s -= 1
       e.insert(END, s)
       print(s)
       
   e.after(1000,ShowTimer)
       
def Clear():
   e.delete(0, END)
   
root = Tk()
root.title("Timer")
e = Entry(root)
b1 = Button(root, text="Start", command=ShowTimer)
b2 = Button(root, text="Clear", command=Clear)
e.grid(row = 0, column = 0, columnspan=2)
b1.grid(row = 1, column = 0)
b2.grid(row = 1, column = 1)
root.mainloop()
