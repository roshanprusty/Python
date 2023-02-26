from tkinter import*
from tkinter import font
from PIL import ImageTk
from tkinter import messagebox

class Login:
    def __init__(self,root):
        self.root=root
        self.root.title("Login System")
        self.root.geometry("1199x600+100+50")
        # self.root.resizable(False,False)

        #bg image
        self.bg=ImageTk.PhotoImage(file="D:\language\programming language\python\projects\grocery billing system/b2.jpg")
        self.bg_image=Label(self.root,image=self.bg).place(x=0, y=0,relwidth=1, relheight=1)

        #login frame
        Frame_login=Frame(self.root, bg="white")
        Frame_login.place(x=480, y=250, height=340, width=500)

        title=Label(Frame_login, text="Login here", font=("Impact",35,"bold"),bg="white", fg="#d77337").place(x=90,y=30)
        desc=Label(Frame_login, text="Accountant Employee Area", font=("Goudy old style",15,"bold"),bg="white", fg="#d25d17").place(x=90,y=100)
        
        lbl_user=Label(Frame_login, text="USERNAME", font=("Goudy old style",15,"bold"),bg="white", fg="gray").place(x=90,y=140)
        self.txt_user=Entry(Frame_login, font=("times new roman",15),bg="lightgray")
        self.txt_user.place(x=90,y=170,width=350,height=35)

        lbl_pass=Label(Frame_login, text="PASSWORD", font=("Goudy old style",15,"bold"),bg="white", fg="gray").place(x=90,y=210)
        self.txt_pass=Entry(Frame_login, font=("times new roman",15),bg="lightgray", show='*')
        self.txt_pass.place(x=90,y=240,width=350,height=35)

        forget_btn=Button(Frame_login,text="Forget Password?",bg="white", fg="#d77337", bd=0, font=("times new roman", 15)).place(x=90, y=280)
        
        login_btn=Button(self.root,command=self.login_fun,cursor="hand2", text="Login",fg="white", bg="#d77337",  font=("times new roman", 20)).place(x=640, y=570, width=180, height=40)




    def login_fun(self):
        if self.txt_pass.get()=="" or self.txt_user.get()=="":
           messagebox.showerror("Error","All fields are required", parent=self.root) 
        elif self.txt_pass.get()!="12345" or self.txt_user.get()!="roshan":
           messagebox.showerror("Error","Invalid Username/Password", parent=self.root) 
        else:
            self.responce=messagebox.showinfo("Welcome",f"Welcome {self.txt_user.get()}", parent=self.root)
            root.destroy()
            import new_gbs
    









root=Tk()
obj=Login(root)
root.mainloop() 