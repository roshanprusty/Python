from tkinter import*
from PIL import ImageTk, Image
from tkinter import filedialog

root = Tk()
root.title("GROCERY BILLING SYSTEM")

# root.filename = filedialog.askopenfilename(initialdir="D:\language\programming language\python\GUI",title="select a file",filetypes=(("jfif files", "*.jfif"),("all files","*.*")))
# my_image=ImageTk.PhotoImage(Image.open(root.filename))
# my_image_label=Label(image=my_image).pack()


def open():
    global my_image
    root.filename = filedialog.askopenfilename(initialdir="D:\language\programming language\python\GUI",title="select a file",filetypes=(("jfif files", "*.jfif"),("all files","*.*")))
    my_image=ImageTk.PhotoImage(Image.open(root.filename))
    my_image_label=Label(image=my_image).pack()

my_btn=Button(root,text="open file", command=open).pack()


mainloop()