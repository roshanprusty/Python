from tkinter import*
from PIL import ImageTk, Image

root = Tk()
root.title("GROCERY BILLING SYSTEM")

frame=LabelFrame(root, text="this is my frame.....", padx=50, pady=50)  #adding padx and pady it will give space inside the container the container
frame.pack(padx=100, pady=100)  #adding padx and pady it will give space outside the container the container
#we usually use pack when we don't care the things

b=Button(frame,text="don't click here!")
b.grid(row=0,column=0)

root.mainloop()