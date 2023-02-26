from tkinter import*
from PIL import ImageTk, Image

root = Tk()
root.title("GROCERY BILLING SYSTEM")
root.geometry("400x400")

vertical=Scale(root,from_=0, to=200).pack()
horizental=Scale(root, from_=0, to=400, orient=HORIZONTAL).pack()

def slide():
    my_label=Label(root, text=horizental.get()).pack()
    root.geometry(str(horizental.get()) + "x" + str(vertical.get()))

my_btn=Button(root,text="click me", command=slide).pack()

root.mainloop()

#littel bit problem is there in this program whenever we are clicking on "click me " it is not printing