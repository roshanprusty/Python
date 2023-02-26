from tkinter import*
from PIL import ImageTk, Image

root = Tk()
root.title("GROCERY BILLING SYSTEM")


#the image didn't show bcz the variable which we were calling is local variable right we need this to be a global variable because for some reason when we're in a function like this with a second window python sees this local variable and it thinks it's garbage it gets swept up in the Python garbage collection and it doesn't get displayed so all we need to do is call global.

def open():
    global my_img2
    top=Toplevel()
    my_img2=ImageTk.PhotoImage(Image.open("D:\language\programming language\python\GUI\i2.jfif"))
    my_lbl2=Label(top,image=my_img2).pack()
    my_lbl2_2=Label(top,text="second window").pack(anchor=W)
    btn2=Button(top,text="close window",command=top.destroy).pack()
    




btn=Button(root,text="open second window",command=open).pack()



my_img1=ImageTk.PhotoImage(Image.open("D:\language\programming language\python\GUI\i1.jfif"))
my_lbl1=Label(root,image=my_img1).pack()
my_lbl1_1=Label(root,text="first window").pack(anchor=W)




mainloop()