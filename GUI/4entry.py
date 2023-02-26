from tkinter import*
root = Tk()



def myclick():
    hello = "hello "+ent.get()
    mylabel = Label(root, text=hello)
    mylabel.pack()

ent=Entry(root,width=50)
ent.pack()
ent.insert(0,"enter your name")
mybutton=Button(root, text="submit", command=myclick)
mybutton.pack()


root.mainloop()
