from tkinter import*
import tkinter as tk
from tkinter import ttk


class Bill_app:
    def __init__(self, root):
        self.root = root
        self.root.geometry("1300x700+0+0")
        self.root.title("grocery Billing System")
        title = Label(self.root, text="BILLING SYSTEM", font=(
            "times new roman", 30, "bold"), pady=2).pack()

        self.soap = IntVar()
        self.face_cream = IntVar()
        self.face_wash = IntVar()
        self.spray = IntVar()
        self.gell = IntVar()
        self.loshan = IntVar()

        self.rice = IntVar()
        self.food_oil = IntVar()
        self.daal = IntVar()
        self.wheat = IntVar()
        self.sugar = IntVar()
        self.tea = IntVar()

        self.maza = IntVar()
        self.cock = IntVar()
        self.frooti = IntVar()
        self.thumbsup = IntVar()
        self.limca = IntVar()
        self.sprite = IntVar()

        self.cosmetic_price = StringVar()
        self.grocery_price = StringVar()
        self.cold_drink_price = StringVar()

        self.c_name = StringVar()
        self.c_phon = StringVar()
        self.bill_no = StringVar()
        self.search = StringVar()

        #==========Customers Frame==========#
        F1 = LabelFrame(text="Customer Details", fg="black",
                        font=("time new roman", 12, "bold"))
        F1.place(x=0, y=80, relwidth=1)

        #===============Customer Name===========#
        cname_lbl = Label(F1, text="Customer Name", fg="black", font=(
            "times new roman", 15, "bold")).grid(row=0, column=0, padx=20, pady=5)
        cname_txt = Entry(F1, width=20, textvariable=self.c_name, font="arial 15").grid(
            row=0, column=1, pady=5, padx=10)

        cphn_lbl = Label(F1, text="customer phone no", fg="black", font=(
            "times new roman", 15, "bold")).grid(row=0, column=2, padx=20, pady=5)
        cphn_txt = Entry(F1, width=20, textvariable=self.c_phon, font="arial 15").grid(
            row=0, column=3, pady=5, padx=10)

        cbill_lbl = Label(F1, text="bill number", fg="black", font=(
            "times new roman", 15, "bold")).grid(row=0, column=4, padx=20, pady=5)
        cbill_txt = Entry(F1, width=20, textvariable=self.search_bill,
                          font="arial 15").grid(row=0, column=5, pady=5, padx=10)

        F2 = LabelFrame(self.root, text="Cosmetic", fg="black",
                        font=("time new roman", 12, "bold"))
        F2.place(x=5, y=180, width=325, height=380)

        bath_lbl = Label(F2, text="Bath soaps", font=("times new roman", 16, "bold")).grid(
            row=0, column=0, padx=10, pady=10, sticky="w")
        bath_txt = Entry(F2, width=10, textvariable=self.soap, font=(
            "times new roman", 16, "bold")).grid(row=0, column=1, padx=10, pady=10)

        face_cream_lbl = Label(F2, text="face cream", font=(
            "times new roman", 16, "bold")).grid(row=1, column=0, padx=10, pady=10, sticky="w")
        face_cream_txt = Entry(F2, width=10, textvariable=self.face_cream(), font=(
            "times new roman", 16, "bold")).grid(row=1, column=1, padx=10, pady=10)

        face_w_lbl = Label(F2, text="face wash", font=("times new roman", 16, "bold")).grid(
            row=2, column=0, padx=10, pady=10, sticky="w")
        face_w_txt = Entry(F2, width=10, textvariable=self.face_wash(), font=(
            "times new roman", 16, "bold")).grid(row=2, column=1, padx=10, pady=10)

        hair_s_lbl = Label(F2, text="hair spray", font=("times new roman", 16, "bold")).grid(
            row=3, column=0, padx=10, pady=10, sticky="w")
        hair_s_txt = Entry(F2, width=10, textvariable=self.spray(), font=(
            "times new roman", 16, "bold")).grid(row=3, column=1, padx=10, pady=10)

        hair_g_lbl = Label(F2, text="hair gel", font=("times new roman", 16, "bold")).grid(
            row=4, column=0, padx=10, pady=10, sticky="w")
        hair_g_txt = Entry(F2, width=10, textvariable=self.gell(), font=(
            "times new roman", 16, "bold")).grid(row=4, column=1, padx=10, pady=10)

        body_l_lbl = Label(F2, text="Body lotion", font=("times new roman", 16, "bold")).grid(
            row=5, column=0, padx=10, pady=10, sticky="w")
        body_l_txt = Entry(F2, width=10, textvariable=self.loshan(), font=(
            "times new roman", 16, "bold")).grid(row=5, column=1, padx=10, pady=10)

        F3 = LabelFrame(self.root, text="grocery", fg="black",
                        font=("time new roman", 12, "bold"))
        F3.place(x=340, y=180, width=325, height=380)

        bath_lbl = Label(F3, text="Rice", font=("times new roman", 16, "bold")).grid(row=0, column=0, padx=10,
                                                                                     pady=10, sticky="w")
        bath_txt = Entry(F3, width=10, textvariable=self.rice(), font=(
            "times new roman", 16, "bold")).grid(row=0, column=1, padx=10, pady=10)

        face_cream_lbl = Label(F3, text="Food oil", font=("times new roman", 16, "bold")).grid(row=1, column=0,
                                                                                               padx=10, pady=10,
                                                                                               sticky="w")
        face_cream_txt = Entry(F3, width=10, textvariable=self.food_oil(), font=("times new roman", 16, "bold")).grid(row=1, column=1, padx=10,
                                                                                                                      pady=10)

        face_w_lbl = Label(F3, text="Daal", font=("times new roman", 16, "bold")).grid(row=2, column=0, padx=10,
                                                                                       pady=10, sticky="w")
        face_w_txt = Entry(F3, width=10, textvariable=self.daal(), font=(
            "times new roman", 16, "bold")).grid(row=2, column=1, padx=10, pady=10)

        hair_s_lbl = Label(F3, text="Wheat", font=("times new roman", 16, "bold")).grid(row=3, column=0, padx=10,
                                                                                        pady=10, sticky="w")
        hair_s_txt = Entry(F3, width=10, textvariable=self.wheat(), font=(
            "times new roman", 16, "bold")).grid(row=3, column=1, padx=10, pady=10)

        hair_g_lbl = Label(F3, text="Sugar", font=("times new roman", 16, "bold")).grid(row=4, column=0, padx=10,
                                                                                        pady=10, sticky="w")
        hair_g_txt = Entry(F3, width=10, textvariable=self.sugar(), font=(
            "times new roman", 16, "bold")).grid(row=4, column=1, padx=10, pady=10)

        body_l_lbl = Label(F3, text="Tea", font=("times new roman", 16, "bold")).grid(row=5, column=0, padx=10,
                                                                                      pady=10, sticky="w")
        body_l_txt = Entry(F3, width=10, textvariable=self.tea(), font=(
            "times new roman", 16, "bold")).grid(row=5, column=1, padx=10, pady=10)

        F4 = LabelFrame(self.root, text="Cold drink", fg="black",
                        font=("time new roman", 12, "bold"))
        F4.place(x=670, y=180, width=325, height=380)

        bath_lbl = Label(F4, text="Maza", font=("times new roman", 16, "bold")).grid(row=0, column=0, padx=10,
                                                                                     pady=10, sticky="w")
        bath_txt = Entry(F4, width=10, textvariable=self.maza(), font=(
            "times new roman", 16, "bold")).grid(row=0, column=1, padx=10, pady=10)

        face_cream_lbl = Label(F4, text="Cock", font=("times new roman", 16, "bold")).grid(row=1, column=0,
                                                                                           padx=10, pady=10,
                                                                                           sticky="w")
        face_cream_txt = Entry(F4, width=10, textvariable=self.cock(), font=("times new roman", 16, "bold")).grid(row=1, column=1, padx=10,
                                                                                                                  pady=10)

        face_w_lbl = Label(F4, text="Frooti", font=("times new roman", 16, "bold")).grid(row=2, column=0, padx=10,
                                                                                         pady=10, sticky="w")
        face_w_txt = Entry(F4, width=10, textvariable=self.Frooti(), font=(
            "times new roman", 16, "bold")).grid(row=2, column=1, padx=10, pady=10)

        hair_s_lbl = Label(F4, text="Thumbs up", font=("times new roman", 16, "bold")).grid(row=3, column=0, padx=10,
                                                                                            pady=10, sticky="w")
        hair_s_txt = Entry(F4, width=10, textvariable=self.thumbsup(), font=(
            "times new roman", 16, "bold")).grid(row=3, column=1, padx=10, pady=10)

        hair_g_lbl = Label(F4, text="Limca", font=("times new roman", 16, "bold")).grid(row=4, column=0, padx=10,
                                                                                        pady=10, sticky="w")
        hair_g_txt = Entry(F4, width=10, textvariable=self.limca(), font=(
            "times new roman", 16, "bold")).grid(row=4, column=1, padx=10, pady=10)

        body_l_lbl = Label(F4, text="sprite", font=("times new roman", 16, "bold")).grid(row=5, column=0, padx=10,
                                                                                         pady=10, sticky="w")
        body_l_txt = Entry(F4, width=10, textvariable=self.sprite(), font=(
            "times new roman", 16, "bold")).grid(row=5, column=1, padx=10, pady=10)

        F5 = Frame(self.root, bd=10, relief=GROOVE)
        F5.place(x=1010, y=180, width=500, height=380)
        bill_title = Label(
            F5, text="Bill area", font="arial 15 bold", bd=7, relief=GROOVE).pack(fill=X)
        scrol_y = Scrollbar(F5, orient=VERTICAL)
        self.textarea = Text(F5, yscrollcommand=scrol_y.set)
        scrol_y.pack(side=RIGHT, fill=Y)
        scrol_y.config(command=self.textarea.yview)
        self.textarea.pack(fill=BOTH, expand=1)

        F6 = LabelFrame(self.root, text="Bill menu", fg="black",
                        font=("time new roman", 12, "bold"))
        F6.place(x=0, y=560, relwidth=1, height=180)
        m1_lbl = Label(F6, text="Total cosmetic price", font=(
            "times new roman", 14, "bold")).grid(row=0, column=0, padx=20, pady=1, sticky="w")
        m1_txt = Entry(F6, width=18, font="arial 15 bold", bd=7,
                       relief=SUNKEN).grid(row=0, column=1, padx=10, pady=1)

        m2_lbl = Label(F6, text="Total grocery price", font=("times new roman", 14, "bold")).grid(row=1, column=0,
                                                                                                  padx=20, pady=1,
                                                                                                  sticky="w")
        m2_txt = Entry(F6, width=18, font="arial 15 bold", bd=7,
                       relief=SUNKEN).grid(row=1, column=1, padx=10, pady=1)

        m3_lbl = Label(F6, text="Total coldrink price", font=("times new roman", 14, "bold")).grid(row=2, column=0,
                                                                                                   padx=20, pady=1,
                                                                                                   sticky="w")
        m3_txt = Entry(F6, width=18, font="arial 15 bold", bd=7,
                       relief=SUNKEN).grid(row=2, column=1, padx=10, pady=1)

        c1_lbl = Label(F6, text="Total cosmetic price", font=("times new roman", 14, "bold")).grid(row=0, column=0,
                                                                                                   padx=20, pady=1,
                                                                                                   sticky="w")
        c1_txt = Entry(F6, width=18, font="arial 15 bold", bd=7,
                       relief=SUNKEN).grid(row=0, column=1, padx=10, pady=1)

        c2_lbl = Label(F6, text="Total grocery price", font=("times new roman", 14, "bold")).grid(row=1, column=0,
                                                                                                  padx=20, pady=1,
                                                                                                  sticky="w")
        c2_txt = Entry(F6, width=18, font="arial 15 bold", bd=7,
                       relief=SUNKEN).grid(row=1, column=1, padx=10, pady=1)

        c3_lbl = Label(F6, text="Total coldrink price", font=("times new roman", 14, "bold")).grid(row=2, column=0,
                                                                                                   padx=20, pady=1,
                                                                                                   sticky="w")
        c3_txt = Entry(F6, width=18, font="arial 15 bold", bd=7,
                       relief=SUNKEN).grid(row=2, column=1, padx=10, pady=1)

        btn_F = Frame(F6, bd=7, relief=GROOVE)
        btn_F.place(x=750, width=635, height=105)

        total_btn = Button(btn_F, text="Total", bg="cadetblue", fg="white", pady=15,
                           width=11, font="arial 15 bold").grid(row=0, column=0, padx=5, pady=5)
        Gbill_btn = Button(btn_F, text="Generate bill", bg="cadetblue", fg="white",
                           pady=15, width=11, font="arial 15 bold").grid(row=0, column=1, padx=5, pady=5)
        clear_btn = Button(btn_F, text="Clear", bg="cadetblue", fg="white", pady=15,
                           width=11, font="arial 15 bold").grid(row=0, column=2, padx=5, pady=5)
        exit_btn = Button(btn_F, text="Exit", bg="cadetblue", fg="white", pady=15,
                          width=11, font="arial 15 bold").grid(row=0, column=3, padx=5, pady=5)

        # face_lbl = Label(F2,font = ("times new roman",15,"bold"),text = "Candy")
        # face_lbl.grid(row = 1,column = 0,padx = 10,pady = 20)
        # face_en = Entry(F2,bd = 8,relief = GROOVE)
        # face_en.grid(row = 1,column = 1,ipady = 5,ipadx = 5)

        # labelframe = LabelFrame(F2, text="This is a Label")
        # labelframe.pack(fill="both", expand="yes")
        # l1 = Label(F2, text="select the category", font=("times new roman", 16))
        # l1.grid(row=0, column=0, padx=10, pady=10, sticky="w")
        # category = ["Cosmetic", "grocery", "cold drink"]
        # cmb = ttk.Combobox(F2, value=category, width=45)
        # cmb.grid(row=1, column=0, padx=10, pady=10, sticky="w")
        # cmb.current(0)
        # for x in category:
        #     if x == "cosmetic":
        #         l2 = Label(F2, text="select the sub-category", font=("times new roman", 16))
        #         l2.grid(row=2, column=0, padx=10, pady=10, sticky="w")
        #         subcategory = ["roshan", "grocery", "cold drink"]
        #         cmb = ttk.Combobox(F2, value=subcategory, width=45)
        #         cmb.grid(row=3, column=0, padx=10, pady=10, sticky="w")
        #         cmb.current(0)
        #     elif x == "grocery":
        #         l2 = Label(F2, text="select the sub-category", font=("times new roman", 16))
        #         l2.grid(row=2, column=0, padx=10, pady=10, sticky="w")
        #         subcategory = ["prusty", "grocery", "cold drink"]
        #         cmb = ttk.Combobox(F2, value=subcategory, width=45)
        #         cmb.grid(row=3, column=0, padx=10, pady=10, sticky="w")
        #         cmb.current(0)
        #     else:
        #         l2 = Label(F2, text="select the sub-category", font=("times new roman", 16))
        #         l2.grid(row=2, column=0, padx=10, pady=10, sticky="w")
        #         subcategory = ["anita", "grocery", "cold drink"]
        #         cmb = ttk.Combobox(F2, value=subcategory, width=45)
        #         cmb.grid(row=3, column=0, padx=10, pady=10, sticky="w")
        #         cmb.current(0)
        #
        # l3 = Label(F2, text="select the quantity", font=("times new roman", 16))
        # l3.grid(row=4, column=0, padx=10, pady=10, sticky="w")
        # quantity = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]
        # cmb = ttk.Combobox(F2, value=quantity, width=45)
        # cmb.grid(row=5, column=0, padx=10, pady=10, sticky="w")
        # cmb.current(0)


root = Tk()
obj = Bill_app(root)
root.mainloop()
