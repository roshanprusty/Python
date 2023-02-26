import os
from tkinter import *
from tkinter import ttk
import random
from tkinter import font
from tkinter import messagebox
import tempfile
import  requests
import json


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

        self.product=StringVar()
        self.prices=IntVar()
        self.qty=IntVar()
        self.sub_total=StringVar()
        self.tax_input=StringVar()
        self.total=StringVar()



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
        bg_color = "white"
        fg_color = "deepskyblue4"
        lbl_color = 'deepskyblue4'
        # Title of App
        title = Label(self.root, text="Grocery Billing System", bd=12, relief=GROOVE,
                      fg=fg_color, bg=bg_color, font=("times new roman", 30, "bold"), pady=3).pack(fill=X)

        #==========Customers Frame==========#
        F1 = LabelFrame(text="Customer Details", font=(
            "time new roman", 12, "bold"), fg="black", bg=bg_color, relief=GROOVE, bd=10)
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
        F2 = LabelFrame(self.root, text='Product', bd=10, relief=GROOVE,
                        bg=bg_color, fg="black", font=("times new roman", 13, "bold"))
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
            F2, value=[""], font=("arial", 12, "bold"), width=24, state="readonly")
        self.combo_sub_category.grid(row=1, column=1, sticky=W, padx=5, pady=2)
        self.combo_sub_category.bind("<<ComboboxSelected>>",self.product_add)

        # ===========product
        self.sub_product = Label(F2, font=("times new roman", 15, "bold"),
                                 fg=lbl_color, bg=bg_color, text="           select product")
        self.sub_product.grid(row=2, column=0, sticky=W, padx=10, pady=20)

        self.combo_product = ttk.Combobox(
            F2, textvariable=self.product, font=("arial", 12, "bold"), width=24, state="readonly")
        self.combo_product.grid(row=2, column=1, sticky=W, padx=5, pady=2)
        self.combo_product.bind("<<ComboboxSelected>>",self.price)

        # ===========price
        self.price_lbl = Label(F2, font=("times new roman", 15, "bold"),
                                 fg=lbl_color, bg=bg_color, text="                 Price")
        self.price_lbl.grid(row = 3,column = 0, sticky=W, padx = 10,pady = 20)

        self.combo_price = ttk.Combobox(
            F2, textvariable=self.prices, font=("arial", 12, "bold"), width=24, state="readonly")
        self.combo_price.grid(row = 3,column = 1,sticky=W, padx=5, pady=2)

        # ===========quantity
        self.quantity_lbl = Label(F2, font=("times new roman", 15, "bold"),
                             fg=lbl_color, bg=bg_color, text=" select product quantity")
        self.quantity_lbl.grid(row = 4,column = 0, sticky=W, padx = 10,pady = 20)

        self.combo_quantity = ttk.Entry(
            F2, font=("arial", 12, "bold"), width=24,textvariable=self.qty)
        self.combo_quantity.grid(row = 4,column = 1,sticky=W, padx=5, pady=2)

        #==================bill counter=====================#

        F3 = LabelFrame(self.root, text='Bill counter', bd=10, relief=GROOVE,
                        bg=bg_color, fg="black", font=("times new roman", 13, "bold"))
        F3.place(x=655, y=180, width=325, height=380)

        # ===========Frame Content

        # ===========sub total
        sub_total_lbl = Label(F3, font=(
            "times new roman", 15, "bold"), fg=lbl_color, bg=bg_color, text="Sub total")
        sub_total_lbl.grid(row=0, column=0, padx=10, pady=20)
        sub_total_en = Entry(F3, textvariable=self.sub_total, bd=8, relief=GROOVE)
        sub_total_en.grid(row=0, column=1, ipady=5, ipadx=5)

        # ===========gov tax
        gov_tax_lbl = Label(F3, font=("times new roman", 15, "bold"),
                            fg=lbl_color, bg=bg_color, text="Gov tax")
        gov_tax_lbl.grid(row=1, column=0, padx=10, pady=20)
        gov_tax_en = Entry(F3,textvariable=self.tax_input, bd=8, relief=GROOVE)
        gov_tax_en.grid(row=1, column=1, ipady=5, ipadx=5)

        # ===========total
        total_lbl = Label(F3, font=("times new roman", 15, "bold"),
                          fg=lbl_color, bg=bg_color, text="Total")
        total_lbl.grid(row=2, column=0, padx=10, pady=20)
        total_en = Entry(F3,textvariable=self.total, bd=8, relief=GROOVE)
        total_en.grid(row=2, column=1, ipady=5, ipadx=5)




        #===================Bill Aera================#
        F4 = Label(self.root,bd = 10,relief = GROOVE)
        F4.place(x = 960,y = 180,width = 325,height = 380)
        #===========
        bill_title = Label(F4,text = "Bill List",font = ("Lucida",13,"bold"),bd= 7,relief = GROOVE)
        bill_title.pack(fill = X)


        #============
        scroll_y = Scrollbar(F4,orient = VERTICAL)
        self.txt = Text(F4,yscrollcommand = scroll_y.set)
        scroll_y.pack(side = RIGHT,fill = Y)
        scroll_y.config(command = self.txt.yview)
        self.txt.pack(fill = BOTH,expand = 1)


        #===========Buttons Frame=============#
        F5 = LabelFrame(self.root, text='Bill Menu', bd=10, relief=GROOVE,
                        bg=bg_color, fg="black", font=("times new roman", 13, "bold"))
        F5.place(x=0, y=560, relwidth=1, height=145)

        # ====================add to cart
        add_to_cart_btn = Button(F5,command=self.additem, text="add to cart", bg=bg_color, fg=fg_color, font=(
            "lucida", 12, "bold"), bd=7, relief=GROOVE)
        add_to_cart_btn.grid(row=1, column=2,sticky=W,padx=20, pady=30)

        # ====================print
        print_btn = Button(F5,command=self.iprint, text="print", bg=bg_color, fg=fg_color, font=(
            "lucida", 12, "bold"), bd=7, relief=GROOVE)
        print_btn.grid(row=1,column=3,sticky=W,padx=20, pady=30)

        # ====================total
        total_btn = Button(F5, text="Total", bg=bg_color, fg=fg_color, font=(
            "lucida", 12, "bold"), bd=7, relief=GROOVE)
        total_btn.grid(row=1, column=4,sticky=W,padx=20, pady=30)

        # ========================generate bill
        genbill_btn = Button(F5, command=self.gen_bill, text="Generate Bill", bg=bg_color, fg=fg_color, font=(
            "lucida", 12, "bold"), bd=7, relief=GROOVE)
        genbill_btn.grid(row=1, column=5, sticky=W,padx=20, pady=30)

        # ====================clear
        clear_btn = Button(F5, command=self.clear, text="Clear", bg=bg_color, fg=fg_color, font=(
            "lucida", 12, "bold"), bd=7, relief=GROOVE)
        clear_btn.grid(row=1, column=6, sticky=W,padx=20, pady=30)

        # ======================exit
        exit_btn = Button(F5, command=self.exit, text="Exit", bg=bg_color, fg=fg_color, font=(
            "lucida", 12, "bold"), bd=7, relief=GROOVE)
        exit_btn.grid(row=1, column=7, sticky=W,padx=20, pady=30)

        self.welcome_soft()

        self.l=[]

    # =========== FUNCTION DECLARATION ====================
    
    #Function For Text Area
    def welcome_soft(self):
        self.txt.delete('1.0',END)
        self.txt.insert(END,"  Welcome To Roshan Store's Retail\n")
        self.txt.insert(END,f"\nBill No. : {str(self.c_bill_no.get())}")
        self.txt.insert(END,f"\nCustomer Name : {str(self.cus_name.get())}")
        self.txt.insert(END,f"\nPhone No. : {str(self.c_phone.get())}")
        self.txt.insert(END,"\n===================================")
        self.txt.insert(END,"\nProduct          Qty         Price")
        self.txt.insert(END,"\n===================================\n")

    #additem
    def additem(self):
        Tax=1
        self.n=self.prices.get()
        self.m=self.qty.get()*self.n
        self.l.append(self.m)
        if self.product.get() =="":
            messagebox.showerror("error", "please select the product name")
        else:
            self.txt.insert(END,f"\n {self.product.get()}\t\t{self.qty.get()}\t\t{self.m}")
            self.sub_total.set(str('Rs.%.2f'%(sum(self.l))))
            self.tax_input.set(str('Rs.%.2f'%((((sum(self.l)) - (self.prices.get()))*Tax)/100)))
            self.total.set(str('Rs.%.2f'%(((sum(self.l)) + ((((sum(self.l)) - (self.prices.get()))*Tax)/100)))))

    #generate bill

    #sending sms to given phone number
    def send_sms(self):
        url = "https://www.fast2sms.com/dev/bulkV2"

        prams = {
        "authorization" : "CW7tOQhzax5V0M9bHGeZ8vBk6KYAXJSmTRnIi3su2UNp1Lqlrd5ZNPeJo6VqhAvlCHLcakfY3bB4zyg0",
        "sender_id" : "FSTSMS",
        "route" : "p",
        "language" : "unicode",
        "numbers" : self.c_phone.get(),
        "message" : "Hope you are happy with your purchase! Thank you for being a valued xyz mart customer!"
        }
        response = requests.get(url, params= prams)
        dic = response.json()
        # print(dic)
        # return dic.get('return')

    def gen_bill(self):
        if self.product.get()=="":
            messagebox.showerror("error", "please add to cart product")
        else:
            text=self.txt.get(10.0,(10.0+float(len(self.l))))    
            self.welcome_soft()
            self.txt.insert(END,text)
            self.txt.insert(END,"\n===================================")
            self.txt.insert(END,f"\n sub  ammount:\t\t\t{self.sub_total.get()}")
            self.txt.insert(END,f"\n tax amount:\t\t\t{self.tax_input.get()}")
            self.txt.insert(END,f"\n total  ammount:\t\t\t{self.total.get()}")
            self.txt.insert(END,"\n===================================")
        self.send_sms()
        

    #print
    def iprint(self):
        q=self.txt.get(1.0,"end-1c")
        filename=tempfile.mktemp('.txt')
        open(filename,'w').write(q)
        os.startfile(filename,"print")

    #Function to clear the bill area
    def clear(self):
        self.txt.delete(1.0,END)
        self.cus_name.set("")
        self.c_phone.set("")
        x=random.randint(1000,9999)
        self.bill_no.set(str(X))
        self.product.set("")
        self.prices.set(0)
        self.qty.set(0)
        self.l=[0]
        self.total.set("")
        self.sub_total.set("")
        self.tax_input.set('')
        self.welcome()

    def exit(self):
        self.root.destroy()


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
            
    def product_add(self, event=""):
        #cosmetic
        if self.combo_sub_category.get()=="BATH SOAP" :
            self.combo_product.config(value=self.bathsoap)
            self.combo_product.current(0)

        if self.combo_sub_category.get()=="FACE WASH" :
            self.combo_product.config(value=self.facewash)
            self.combo_product.current(0)

        if self.combo_sub_category.get()=="SHAMPOO" :
            self.combo_product.config(value=self.shampoo)
            self.combo_product.current(0)

        #grocery
        if self.combo_sub_category.get()=="WHEAT" :
            self.combo_product.config(value=self.wheat)
            self.combo_product.current(0)

        if self.combo_sub_category.get()=="TEA" :
            self.combo_product.config(value=self.tea)
            self.combo_product.current(0)

        if self.combo_sub_category.get()=="FOOD OIL" :
            self.combo_product.config(value=self.food_oil)
            self.combo_product.current(0)

        #others
        if self.combo_sub_category.get()=="COLD DRINKS" :
            self.combo_product.config(value=self.cold_drink)
            self.combo_product.current(0)

        if self.combo_sub_category.get()=="CHOCOLATE" :
            self.combo_product.config(value=self.choclate)
            self.combo_product.current(0)

        if self.combo_sub_category.get()=="BISCUITS" :
            self.combo_product.config(value=self.biscuit)
            self.combo_product.current(0)

    def price(self, event=""):
        #cosmetic
        #bathsoap
        if self.combo_product.get()=="CINTHOL":
            self.combo_price.config(value=self.price_cinthol)
            self.combo_price.current(0)
            self.qty.set(1)

        if self.combo_product.get()=="DOVE":
            self.combo_price.config(value=self.price_dove)
            self.combo_price.current(0)
            self.qty.set(1)

        if self.combo_product.get()=="LIFE BUOY":
            self.combo_price.config(value=self.price_life_buoy)
            self.combo_price.current(0)
            self.qty.set(1)

        #cosmetic
        #facewash
        if self.combo_product.get()=="NIVEA":
            self.combo_price.config(value=self.price_nivea)
            self.combo_price.current(0)
            self.qty.set(1)

        if self.combo_product.get()=="GARNIER":
            self.combo_price.config(value=self.price_garnier)
            self.combo_price.current(0)
            self.qty.set(1)

        if self.combo_product.get()=="HIMALAYA":
            self.combo_price.config(value=self.price_himalaya)
            self.combo_price.current(0)
            self.qty.set(1)

        #cosmetic
        #shampoo
        if self.combo_product.get()=="LOREAL":
            self.combo_price.config(value=self.price_loreal)
            self.combo_price.current(0)
            self.qty.set(1)

        if self.combo_product.get()=="MAMA EARTH":
            self.combo_price.config(value=self.price_mama_earth)
            self.combo_price.current(0)
            self.qty.set(1)

        if self.combo_product.get()=="HEAD & SHOULDERS":
            self.combo_price.config(value=self.price_head_shoulders)
            self.combo_price.current(0)
            self.qty.set(1)

        #grocery
        #wheat
        if self.combo_product.get()=="AASHIRVAAD":
            self.combo_price.config(value=self.price_aaashrivad)
            self.combo_price.current(0)
            self.qty.set(1)

        if self.combo_product.get()=="NATURE FRESH":
            self.combo_price.config(value=self.price_nature_fresh)
            self.combo_price.current(0)
            self.qty.set(1)

        if self.combo_product.get()=="PATANJALI":
            self.combo_price.config(value=self.price_patanjali)
            self.combo_price.current(0)
            self.qty.set(1)

        #grocery
        #tea
        if self.combo_product.get()=="RED LABEL":
            self.combo_price.config(value=self.price_red_label)
            self.combo_price.current(0)
            self.qty.set(1)

        if self.combo_product.get()=="TATA TEA":
            self.combo_price.config(value=self.price_tata_tea)
            self.combo_price.current(0)
            self.qty.set(1)

        if self.combo_product.get()=="LIPTON":
            self.combo_price.config(value=self.price_lipton)
            self.combo_price.current(0)
            self.qty.set(1)

        #grocery
        #food oil
        if self.combo_product.get()=="SAFFOLA GOLD":
            self.combo_price.config(value=self.price_saffola_gold)
            self.combo_price.current(0)
            self.qty.set(1)

        if self.combo_product.get()=="FORTUNE":
            self.combo_price.config(value=self.price_fortune)
            self.combo_price.current(0)
            self.qty.set(1)

        if self.combo_product.get()=="SUNDROP":
            self.combo_price.config(value=self.price_sundrop)
            self.combo_price.current(0)
            self.qty.set(1)

        #others
        #cold drinks
        if self.combo_product.get()=="SPRITE":
            self.combo_price.config(value=self.price_sprite)
            self.combo_price.current(0)
            self.qty.set(1)

        if self.combo_product.get()=="FENTA":
            self.combo_price.config(value=self.price_fenta)
            self.combo_price.current(0)
            self.qty.set(1)

        if self.combo_product.get()=="COCA COLA":
            self.combo_price.config(value=self.price_coca_cola)
            self.combo_price.current(0)
            self.qty.set(1)

        #others
        #choclates
        if self.combo_product.get()=="DAIRY MILK":
            self.combo_price.config(value=self.price_dairy_milk)
            self.combo_price.current(0)
            self.qty.set(1)

        if self.combo_product.get()=="KIT KAT":
            self.combo_price.config(value=self.price_kitkat)
            self.combo_price.current(0)
            self.qty.set(1)

        if self.combo_product.get()=="SNICKERS":
            self.combo_price.config(value=self.price_snickers)
            self.combo_price.current(0)
            self.qty.set(1)

        #others
        #biscuits
        if self.combo_product.get()=="DARK FANTASY":
            self.combo_price.config(value=self.price_dark_fantasy)
            self.combo_price.current(0)
            self.qty.set(1)

        if self.combo_product.get()=="OREO":
            self.combo_price.config(value=self.price_oreo)
            self.combo_price.current(0)
            self.qty.set(1)

        if self.combo_product.get()=="TREAT":
            self.combo_price.config(value=self.price_treat)
            self.combo_price.current(0)
            self.qty.set(1)







root = Tk()
object = Bill_App(root)
root.mainloop()
