from tkinter import*
from PIL import ImageTk, Image

root = Tk()
root.title("GROCERY BILLING SYSTEM")
root.iconbitmap("D:\language\programming language\python\GUI\gbs.jfif")  # icon

my_img1 = ImageTk.PhotoImage(Image.open(
    "D:\language\programming language\python\GUI\gbs.jfif"))
my_img2 = ImageTk.PhotoImage(Image.open(
    "D:\language\programming language\python\GUI\i1.jfif"))
my_img3 = ImageTk.PhotoImage(Image.open(
    "D:\language\programming language\python\GUI\i2.jfif"))
my_img4 = ImageTk.PhotoImage(Image.open(
    "D:\language\programming language\python\GUI\i3.jfif"))
my_img5 = ImageTk.PhotoImage(Image.open(
    "D:\language\programming language\python\GUI\i4.jfif"))


image_list = [my_img1, my_img2, my_img3, my_img4, my_img5]


my_label = Label(image=my_img1)
my_label.grid(row=0, column=0, columnspan=3)


def forward(image_number):
    global my_label
    global button_forward
    global button_back

# if we click on next button the forward image will come which it will be overlap of present image to tackle such situation we have to delete the previous image.
# To get rid of that we use grid_forget it's just an internal function that the grid system can use to sort of get rid of something so our image is in my label so we're just gonna sort of delete that from the screen
    my_label.grid_forget()
    my_label = Label(image=image_list[image_number-1])
    button_forward = Button(root, text=">>", command=lambda: forward(image_number+1))
    button_back = Button(root, text="<<", command=lambda: back(image_number-1))
    if image_number == 5:
        button_forward = Button(root, text=">>", state=DISABLED)
    my_label.grid(row=0, column=0, columnspan=3)
    button_back.grid(row=1, column=0)
    button_forward.grid(row=1, column=2)


def back(image_number):
    global my_label
    global button_forward
    global button_back

    my_label.grid_forget()
    my_label = Label(image=image_list[image_number-1])
    button_forward = Button(root, text=">>", command=lambda: forward(image_number+1))
    button_back = Button(root, text="<<", command=lambda: back(image_number-1))
    if image_number == 1:
        button_back = Button(root, text="<<", state=DISABLED)

    my_label.grid(row=0, column=0, columnspan=3)
    button_back.grid(row=1, column=0)
    button_forward.grid(row=1, column=2)



# Lamda Functions (also referred to as Anonymous Function in Python) are very useful in building Tkinter GUI applications. They allow us to send multiple data through the callback function. Lambda can be inside any function that works as an anonymous function for expressions. In Button Command, lambda is used to pass the data to a callback function.

button_back=Button(root, text="<<", command=back)
button_exit=Button(root, text="exit program", command=root.quit)
button_forward=Button(root, text=">>", command=lambda: forward(2))

button_back.grid(row=1, column=0)
button_exit.grid(row=1, column=1)
button_forward.grid(row=1, column=2)


root.mainloop()
