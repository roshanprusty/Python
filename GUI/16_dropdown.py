from tkinter import*
from PIL import ImageTk, Image

root = Tk()
root.title("GROCERY BILLING SYSTEM")
root.geometry("400x400")

#drop down menu
def show():
    myLabel= Label(root, text=clicked.get()).pack()

options1 =[
    "COSMETIC",
    "GROCERY",
    "COLD DRINK"
]
clicked= StringVar()
clicked.set("category")

drop=OptionMenu(root, clicked , *options1).pack()

# mybutton =Button(root, text="show selection", command=show).pack()
if (clicked.get()== "COSMETIC"):
    options2 =[
    "BREAD",
    "CANDY",
    "HAMBURGER",
    "HOTDOG",
    "SANDWICH"
    ]
    clicked= StringVar()
    clicked.set(options2[0])

    drop=OptionMenu(root, clicked , *options2).pack()

elif(clicked.get()== "GROCERY"):
    options3 =[
    "RICE",
    "FOOD OIL",
    "SALT",
    "WHEAT",
    "SUGAR"
    ]
    clicked= StringVar()
    clicked.set(options3[0])

    drop=OptionMenu(root, clicked , *options3).pack()

elif(clicked.get()== "COLD DRINK"):
    options4 =[
    "COCO COLA",
    "SPRITE",
    "SLICE",
    "FENTA",
    "PEPSI"
    ]
    clicked= StringVar()
    clicked.set(options4[0])

    drop=OptionMenu(root, clicked , *options4).pack()


root.mainloop()
