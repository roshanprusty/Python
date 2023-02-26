from tkinter import*
from PIL import ImageTk, Image

root = Tk()
root.title("GROCERY BILLING SYSTEM")
root.geometry("400x400")

def show():
    mylabel=Label(root,text=var.get()).pack()


var=StringVar()
c=Checkbutton(root,text="click here, i have suprise for you",variable=var, onvalue="on", offvalue="off").pack()

my_button=Button(root,text="click here", command=show).pack()
root.mainloop()
