from tkinter import*
from PIL import ImageTk, Image
from tkinter import messagebox

root = Tk()
root.title("GROCERY BILLING SYSTEM")

#different message box
#showinfo, showwarning, showerror, askquestion, askokcancel, askyesno
#it will reflect sound also

def popup():
    responce=messagebox.askyesno("this is my popup !","hello world")
    # Label(root,text=responce).pack()
    if responce ==1:
         Label(root,text="you clicked yes!").pack()
    else:
         Label(root,text="you clicked No!").pack()
        

Button(root,text="popup", command=popup).pack()


root.mainloop()