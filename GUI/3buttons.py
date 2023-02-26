from tkinter import*
root = Tk()

def myclick():
    mylabel=Label(root, text="your form is sucessfully submitted")
    mylabel.pack()

mybutton=Button(root,text="submit", state=DISABLED, padx=50, pady=50)
mybutton2=Button(root,text="submit",command=myclick,fg="blue",bg="grey") #if you write myclick() then you don't need to click on the button. it will already showing there
mybutton.pack()
mybutton2.pack()

root.mainloop()
