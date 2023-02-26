#positioning with tkinter's grid system
from tkinter import *
root = Tk()

# creating the label widget
mylabel = Label(root, text="hello world")
mylabel2 = Label(root, text="my name is roshan prusty")
mylabel3 = Label(root, text="                        ")
# showing it onto the screen

mylabel.grid(row=0,column=0)
mylabel2.grid(row=1,column=5)
mylabel3.grid(row=1,column=1)

root.mainloop()