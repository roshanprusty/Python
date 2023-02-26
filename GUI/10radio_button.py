from tkinter import*
from PIL import ImageTk, Image

root = Tk()
root.title("PIZZA HUT")

# tKinter variable
# here we want this to be an integer because the value we've assigned to it is either 1 or 2 and 1 or 2 is an integer right so the variable needs to be an integer variable
# this function tkinter to keep track of  change over time to this variable so when we click on thing it'll know that
# if somebody clicks on a different radio button we want to be able to get so that's why we're using these instead of just regular Python variables that's just a sort of a function of radio buttons.
# r = IntVar()
# r.get()
# r.set("2")  # in tKinter you can set and get
# now it will set 2 automatically

TOPPINGS = [
    ("pepperoni","pepperoni"),
    ("cheese","cheese"),("mushroom","mushroom"),("onion","onion")
    ] #(text,toppings)

pizza=StringVar()
pizza.set(1)

def clicked(value):
    mylabel = Label(root, text=value)
    mylabel.pack()


# Radiobutton(root, text="option 1", variable=r, value=1,
#             command=lambda: clicked(r.get())).pack()
# Radiobutton(root, text="option 2", variable=r, value=2,command=lambda: clicked(pizza.get())).pack()

for text,toppings in TOPPINGS:
    Radiobutton(root,text=text,variable=pizza,value=toppings).pack(anchor=W)

# mylabel = Label(root, text=pizza.get())
# mylabel.pack()

mybutton=Button(root,text="ORDER",command=lambda:clicked(pizza.get()))
mybutton.pack()

root.mainloop()
