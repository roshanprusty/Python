from tkinter import *
from tkinter import ttk
import random
from tkinter import font

root = Tk()
root.title("GROCERY BILLING SYSTEM")

def open():
    class Bill_App:
        def __init__(self, root):
            self.root = root
            self.root.geometry("1300x700+0+0")
            self.root.maxsize(width=1280, height=700)
            self.root.minsize(width=1280, height=700)
            self.root.title("Grocery Billing System")

            #====================Variables========================#
            self.cus_name = StringVar()
            self.c_phone = StringVar()
            # For Generating Random Bill Numbers
            x = random.randint(1000, 9999)
            self.c_bill_no = StringVar()
            # Seting Value to variable
            self.c_bill_no.set(str(x))

            # self.bread = IntVar()
            # self.candy = IntVar()
            # self.hamburger = IntVar()
            # self.hotdog = IntVar()
            # self.sandwich = IntVar()
            # self.rice = IntVar()
            # self.salt = IntVar()
            # self.food_oil = IntVar()
            # self.wheat = IntVar()
            # self.sugar = IntVar()
            # self.gatorade = IntVar()
            # self.coke = IntVar()
            # self.juice = IntVar()
            # self.waffer = IntVar()
            # self.biscuits = IntVar()
            self.total_food = StringVar()
            # self.total_grocery = StringVar()
            # self.total_other = StringVar()
            # self.tax_cos = StringVar()
            # self.tax_groc = StringVar()
            # self.tax_other = StringVar()

            # product categories list
            self.category = ["select options",
                             "COSMETIC",
                             "GROCERY",
                             "OTHER STUFF"]

            #subcat_cosmetic
            self.subcat_cosmetic = ["BATH SOAP",
                                    "FACE WASH",
                                    "SHAMPOO"]

            self.bathsoap = ["CINTHOL",
                             "DOVE",
                             "LIFE BUOY"]
            self.price_cinthol=30
            self.price_dove=40
            self.price_life_buoy=35

            self.facewash = ["NIVEA",
                             "GARNIER",
                             "HIMALAYA"]
            self.price_nivea=130
            self.price_garnier=140
            self.price_himalaya=135

            self.shampoo = ["LOREAL",
                             "MAMA EARTH",
                             "HEAD & SHOULDERS"]
            self.price_loreal=80
            self.price_mama_earth=100
            self.price_head_shoulders=110

            #subcat_grocery
            self.subcat_grocery = ["WHEAT",
                                    "TEA",
                                    "FOOD OIL"]

            self.wheat = ["AASHIRVAAD",
                             "NATURE FRESH",
                             "PATANJALI"]

            self.price_aaashrivad=200
            self.price_nature_fresh=180
            self.price_patanjali=195

            self.tea = ["RED LABEL",
                             "TATA TEA",
                             "LIPTON"]
            self.price_red_label=60
            self.price_tata_tea=80
            self.price_lipton=90

            self.food_oil = ["SAFFOLA GOLD",
                             "FORTUNE",
                             "SUNDROP"]
            self.price_saffola_gold=130
            self.price_fortune=140
            self.price_sundrop=135


            #subcat_OTHER_STUFFS
            self.subcat_others = ["COLD DRINKS",
                                    "CHOCOLATE",
                                    "BISCUITS"]

            self.cold_drink = ["SPRITE",
                             "FENTA",
                             "COCA COLA"]
            self.price_sprite=25
            self.price_fenta=22
            self.price_coca_cola=21

            self.choclate = ["DAIRY MILK",
                             "KIT KAT",
                             "SNICKERS"]
            self.price_dairy_milk=30
            self.price_kitkat=40
            self.price_snickers=35

            self.biscuit = ["DARK FANTASY",
                             "OREO",
                             "TREAT"]
            self.price_dark_fantasy=80
            self.price_oreo=100
            self.price_treat=110



            # ===================================
            bg_color = "green"
            fg_color = "white"
            lbl_color = 'white'
            # Title of App
            title = Label(self.root, text="Grocery Billing System", bd=12, relief=GROOVE,
                          fg=fg_color, bg=bg_color, font=("times new roman", 30, "bold"), pady=3).pack(fill=X)

            #==========Customers Frame==========#
            F1 = LabelFrame(text="Customer Details", font=(
                "time new roman", 12, "bold"), fg="gold", bg=bg_color, relief=GROOVE, bd=10)
            F1.place(x=0, y=80, relwidth=1)

            #===============Customer Name===========#
            cname_lbl = Label(F1, text="Customer Name", bg=bg_color, fg=fg_color, font=(
                "times new roman", 15, "bold")).grid(row=0, column=0, padx=10, pady=5)
            cname_en = Entry(F1, bd=8, relief=GROOVE, textvariable=self.cus_name)
            cname_en.grid(row=0, column=1, ipady=4, ipadx=30, pady=5)

            #=================Customer Phone==============#
            cphon_lbl = Label(F1, text="Phone No", bg=bg_color, fg=fg_color, font=(
                "times new roman", 15, "bold")).grid(row=0, column=2, padx=20)
            cphon_en = Entry(F1, bd=8, relief=GROOVE, textvariable=self.c_phone)
            cphon_en.grid(row=0, column=3, ipady=4, ipadx=30, pady=5)

            #====================Customer Bill No==================#
            cbill_lbl = Label(F1, text="Bill No.", bg=bg_color,
                              fg=fg_color, font=("times new roman", 15, "bold"))
            cbill_lbl.grid(row=0, column=4, padx=20)
            cbill_en = Entry(F1, bd=8, relief=GROOVE, textvariable=self.c_bill_no)
            cbill_en.grid(row=0, column=5, ipadx=30, ipady=4, pady=5)

            #==================product Frame=====================#
            F2 = LabelFrame(self.root, text='product', bd=10, relief=GROOVE,
                            bg=bg_color, fg="gold", font=("times new roman", 13, "bold"))
            F2.place(x=5, y=180, width=650, height=380)

            # ===========category
            self.category_lbl = Label(F2, font=("times new roman", 15, "bold"),
                                 fg=lbl_color, bg=bg_color, text=" select product category")
            self.category_lbl.grid(row=0, column=0, padx=10, pady=20)

            self.combo_category = ttk.Combobox(
                F2, value=self.category, font=("arial", 12, "bold"), width=24, state="readonly")
            self.combo_category.current(0)
            self.combo_category.grid(row=0, column=1, sticky=W, padx=5, pady=2)
            self.combo_category.bind("<<ComboboxSelected>>",self.Categories)

            # ===========sub category
            self.sub_category_lbl = Label(F2, font=("times new roman", 15, "bold"),
                                     fg=lbl_color, bg=bg_color, text=" select product sub-category")
            self.sub_category_lbl.grid(row=1, column=0, sticky=W, padx=10, pady=20)

            self.combo_sub_category = ttk.Combobox(
                F2, font=("arial", 12, "bold"), width=24, state="readonly")
            self.combo_sub_category.grid(row=1, column=1, sticky=W, padx=5, pady=2)

            # ===========product
            self.sub_product = Label(F2, font=("times new roman", 15, "bold"),
                                     fg=lbl_color, bg=bg_color, text="           select product")
            self.sub_product.grid(row=2, column=0, sticky=W, padx=10, pady=20)

            self.combo_product = ttk.Combobox(
                F2, font=("arial", 12, "bold"), width=24, state="readonly")
            self.combo_product.grid(row=2, column=1, sticky=W, padx=5, pady=2)

            # ===========quantity
            self.quantity_lbl = Label(F2, font=("times new roman", 15, "bold"),
                                 fg=lbl_color, bg=bg_color, text=" select product quantity")
            self.quantity_lbl.grid(row = 3,column = 0, sticky=W, padx = 10,pady = 20)

            self.combo_quantity = ttk.Combobox(
                F2, font=("arial", 12, "bold"), width=24, state="readonly")
            self.combo_quantity.grid(row = 3,column = 1,sticky=W, padx=5, pady=2)

            #==================bill counter=====================#

            F2 = LabelFrame(self.root, text='Bill counter', bd=10, relief=GROOVE,
                            bg=bg_color, fg="gold", font=("times new roman", 13, "bold"))
            F2.place(x=655, y=180, width=325, height=380)

            # ===========Frame Content

            # ===========sub total
            sub_total_lbl = Label(F2, font=(
                "times new roman", 15, "bold"), fg=lbl_color, bg=bg_color, text="Sub total")
            sub_total_lbl.grid(row=0, column=0, padx=10, pady=20)
            sub_total_en = Entry(F2, bd=8, relief=GROOVE,
                                 textvariable=self.total_food)
            sub_total_en.grid(row=0, column=1, ipady=5, ipadx=5)

            # ===========gov tax
            gov_tax_lbl = Label(F2, font=("times new roman", 15, "bold"),
                                fg=lbl_color, bg=bg_color, text="Gov tax")
            gov_tax_lbl.grid(row=1, column=0, padx=10, pady=20)
            gov_tax_en = Entry(F2, bd=8, relief=GROOVE,
                               textvariable=self.total_food)
            gov_tax_en.grid(row=1, column=1, ipady=5, ipadx=5)

            # ===========total
            total_lbl = Label(F2, font=("times new roman", 15, "bold"),
                              fg=lbl_color, bg=bg_color, text="Total")
            total_lbl.grid(row=2, column=0, padx=10, pady=20)
            total_en = Entry(F2, bd=8, relief=GROOVE, textvariable=self.total_food)
            total_en.grid(row=2, column=1, ipady=5, ipadx=5)

            #===========Buttons Frame=============#
            F4 = LabelFrame(self.root, text='Bill Menu', bd=10, relief=GROOVE,
                            bg=bg_color, fg="gold", font=("times new roman", 13, "bold"))
            F4.place(x=0, y=560, relwidth=1, height=145)

            # ====================add to cart
            add_to_cart_btn = Button(F4, text="add to cart", bg=bg_color, fg=fg_color, font=(
                "lucida", 12, "bold"), bd=7, relief=GROOVE)
            add_to_cart_btn.grid(row=1, column=2, ipadx=20, padx=30)

            # ====================print
            print_btn = Button(F4, text="print", bg=bg_color, fg=fg_color, font=(
                "lucida", 12, "bold"), bd=7, relief=GROOVE)
            print_btn.grid(row=1, column=3, ipadx=20)

            # ====================total
            total_btn = Button(F4, text="Total", bg=bg_color, fg=fg_color, font=(
                "lucida", 12, "bold"), bd=7, relief=GROOVE)
            total_btn.grid(row=1, column=4, ipadx=20, padx=30)

            # ========================generate bill
            genbill_btn = Button(F4, text="Generate Bill", bg=bg_color, fg=fg_color, font=(
                "lucida", 12, "bold"), bd=7, relief=GROOVE)
            genbill_btn.grid(row=1, column=5, ipadx=20)

            # ====================
            clear_btn = Button(F4, text="Clear", bg=bg_color, fg=fg_color, font=(
                "lucida", 12, "bold"), bd=7, relief=GROOVE)
            clear_btn.grid(row=1, column=6, ipadx=20, padx=30)

            # ======================
            exit_btn = Button(F4, text="Exit", bg=bg_color, fg=fg_color, font=(
                "lucida", 12, "bold"), bd=7, relief=GROOVE)
            exit_btn.grid(row=1, column=7, ipadx=20)


            #===================Bill Aera================#
            F3 = Label(self.root, bd=10, relief=GROOVE)
            F3.place(x=960, y=180, width=325, height=380)
            # ===========
            bill_title = Label(F3, text="Bill List", font=(
                "Lucida", 13, "bold"), bd=7, relief=GROOVE)
            bill_title.pack(fill=X)

            # ============
            scroll_y = Scrollbar(F3, orient=VERTICAL)
            self.txt = Text(F3, yscrollcommand=scroll_y.set)
            scroll_y.pack(side=RIGHT, fill=Y)
            scroll_y.config(command=self.txt.yview)
            self.txt.pack(fill=BOTH, expand=1)


    def Categories(self,event=""):
        if self.combo_category.get()=="COSMETIC":
            self.combo_sub_category.config(value=self.subcat_cosmetic)
            self.combo_sub_category.current(0)

        if self.combo_category.get()=="GROCERY":
            self.combo_sub_category.config(value=self.subcat_grocery)
            self.combo_sub_category.current(0)

        if self.combo_category.get()=="OTHER STUFF":
            self.combo_sub_category.config(value=self.subcat_others)
            self.combo_sub_category.current(0)
    object = Bill_App(root)




btn=Button(root,text="open second window",command=open).pack()






root = Tk()

root.mainloop()
