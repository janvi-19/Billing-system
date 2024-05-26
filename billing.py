from tkinter import *
from tkinter import messagebox
import math,os
import random

class Bill_App():
    def __init__(self,root):
        self.root=root
        self.root.geometry('1350x700+0+0')
        self.root.title("Billing System created by Faizan Khan")
        self.root.iconbitmap('icon.ico')
        bg_color='gray20'


        title=Label(self.root,text="Billing System",font=('times new roman',30,'bold'),bg=bg_color,fg='gold',bd=12,relief=GROOVE,pady=2).pack(fill=X)

        #variables
        #cosmetic variables
        self.soap=IntVar()
        self.facecream=IntVar()
        self.facewash=IntVar()
        self.spray = IntVar()
        self.gel = IntVar()
        self.lotion = IntVar()

        #grocery variables

        self.rice = IntVar()
        self.oil = IntVar()
        self.daal = IntVar()
        self.wheat = IntVar()
        self.sugar = IntVar()
        self.tea = IntVar()

        #colddrink variables

        self.maza = IntVar()
        self.pepsi = IntVar()
        self.sprite = IntVar()
        self.dew = IntVar()
        self.frooti = IntVar()
        self.cocacola = IntVar()

        #total product price and tax variables

        self.cosmeticprice = StringVar()
        self.groceryprice = StringVar()
        self.colddrinkprice = StringVar()

        self.cosmetictax = StringVar()
        self.grocerytax = StringVar()
        self.colddrinktax = StringVar()

        #customer details variables
        self.cname = StringVar()
        self.cphone = StringVar()

        self.billnumber = StringVar()
        x = random.randint(1000, 9999)
        self.billnumber.set(str(x))
        self.searchbill=StringVar()










        #customer detail frame
        F1=LabelFrame(self.root,text='Customer Details',bd=10,relief=GROOVE,font=('times new roman',15,'bold'),bg=bg_color,fg='gold')
        F1.place(x=0,y=80,relwidth=1)
        cname_label=Label(F1,text='Name',font=('times new roman',18,'bold'),bg=bg_color,fg='white').grid(row=0,column=0,padx=20,pady=2)
        cname_text=Entry(F1,width=18,textvariable=self.cname,font=('arial',15),bd=7,relief=SUNKEN).grid(row=0,column=1,pady=5,padx=10)

        cphone_label = Label(F1, text='Phone Number', font=('times new roman', 18, 'bold'), bg=bg_color,
                            fg='white').grid(row=0, column=2, padx=20, pady=2)
        cphone_text = Entry(F1, width=18,textvariable=self.cphone,font=('arial', 15), bd=7, relief=SUNKEN).grid(row=0, column=3, pady=5, padx=10)

        cbill_label = Label(F1, text='Bill Number', font=('times new roman', 18, 'bold'), bg=bg_color,
                            fg='white').grid(row=0, column=4, padx=20, pady=2)
        cbill_text = Entry(F1, width=18,textvariable=self.searchbill, font=('arial', 15), bd=7, relief=SUNKEN).grid(row=0, column=5, pady=5, padx=10)

        billsearch_btn=Button(F1,text="search",command=self.find_bill,width=10,bd=7,font=('arial',12,'bold')).grid(row=0,column=6,padx=18,pady=10)
        #cosmetics frame
        F2=LabelFrame(self.root,text='Cosmetics',bd=10,relief=GROOVE,font=('times new roman',15,'bold'),bg=bg_color,fg='gold')
        F2.place(x=5,y=185,width=325,height=380)
        bath_label=Label(F2,text="Bath Soap",font=('times new roman',16,'bold'),bg=bg_color,
                         fg='white').grid(row=0,column=0,padx=10,pady=10,sticky='w')
        bath_text=Entry(F2,width=10,textvariable=self.soap,font=('times new roman',16,'bold'),
                        bd=5,relief=SUNKEN).grid(row=0,column=1,padx=10,pady=10)
        facecream_label = Label(F2, text="Face Cream", font=('times new roman', 16, 'bold'), bg=bg_color,
                           fg='white').grid(row=1, column=0, padx=10, pady=10, sticky='w')
        facecream_text = Entry(F2, width=10,textvariable=self.facecream, font=('times new roman', 16, 'bold'),
                          bd=5, relief=SUNKEN).grid(row=1, column=1,padx=10,pady=10)
        facewash_label = Label(F2, text="Face Wash", font=('times new roman', 16, 'bold'), bg=bg_color,
                           fg='white').grid(row=2, column=0, padx=10, pady=10, sticky='w')
        facewash_text = Entry(F2, width=10,textvariable=self.facewash, font=('times new roman', 16, 'bold'),
                          bd=5, relief=SUNKEN).grid(row=2, column=1, padx=10, pady=10)
        hairspray_label = Label(F2, text="Hair Spray", font=('times new roman', 16, 'bold'), bg=bg_color,
                           fg='white').grid(row=3, column=0, padx=10, pady=10, sticky='w')
        hairspray_text = Entry(F2, width=10,textvariable=self.spray, font=('times new roman', 16, 'bold'),
                          bd=5, relief=SUNKEN).grid(row=3, column=1, padx=10, pady=10)
        hairgel_label = Label(F2, text="Hair Gel", font=('times new roman', 16, 'bold'), bg=bg_color,
                           fg='white').grid(row=4, column=0, padx=10, pady=10, sticky='w')
        hairgel_text = Entry(F2, width=10, textvariable=self.gel,font=('times new roman', 16, 'bold'),
                          bd=5, relief=SUNKEN).grid(row=4, column=1, padx=10, pady=10)
        bodylotion_label = Label(F2, text="Body Lotion", font=('times new roman', 16, 'bold'), bg=bg_color,
                           fg='white').grid(row=5, column=0, padx=10, pady=10, sticky='w')
        bodylotion_text = Entry(F2, width=10, textvariable=self.lotion,font=('times new roman', 16, 'bold'),
                          bd=5, relief=SUNKEN).grid(row=5, column=1, padx=10,pady=10)

        #grocery frame

        F3 = LabelFrame(self.root, text='Grocery', bd=10, relief=GROOVE, font=('times new roman', 15, 'bold'),
                        bg=bg_color, fg='gold')
        F3.place(x=340, y=185, width=325, height=380)
        rice_label = Label(F3, text="Rice", font=('times new roman', 16, 'bold'), bg=bg_color,
                           fg='white').grid(row=0, column=0, padx=10, pady=10, sticky='w')
        rice_text = Entry(F3, width=10,textvariable=self.rice, font=('times new roman', 16, 'bold'),
                          bd=5, relief=SUNKEN).grid(row=0, column=1, padx=10, pady=10)
        Oil_label = Label(F3, text="Oil", font=('times new roman', 16, 'bold'), bg=bg_color,
                                fg='white').grid(row=1, column=0, padx=10, pady=10, sticky='w')
        Oil_text = Entry(F3, width=10,textvariable=self.oil, font=('times new roman', 16, 'bold'),
                               bd=5, relief=SUNKEN).grid(row=1, column=1, padx=10, pady=10)
        daal_label = Label(F3, text="Daal", font=('times new roman', 16, 'bold'), bg=bg_color,
                               fg='white').grid(row=2, column=0, padx=10, pady=10, sticky='w')
        daal_text = Entry(F3, width=10,textvariable=self.daal, font=('times new roman', 16, 'bold'),
                              bd=5, relief=SUNKEN).grid(row=2, column=1, padx=10, pady=10)
        wheat_label = Label(F3, text="Wheat", font=('times new roman', 16, 'bold'), bg=bg_color,
                                fg='white').grid(row=3, column=0, padx=10, pady=10, sticky='w')
        wheat_text = Entry(F3, width=10, textvariable=self.wheat,font=('times new roman', 16, 'bold'),
                               bd=5, relief=SUNKEN).grid(row=3, column=1, padx=10, pady=10)
        sugar_label = Label(F3, text="Sugar", font=('times new roman', 16, 'bold'), bg=bg_color,
                              fg='white').grid(row=4, column=0, padx=10, pady=10, sticky='w')
        sugar_text = Entry(F3, width=10,textvariable=self.sugar, font=('times new roman', 16, 'bold'),
                             bd=5, relief=SUNKEN).grid(row=4, column=1, padx=10, pady=10)
        tea_label = Label(F3, text="Tea", font=('times new roman', 16, 'bold'), bg=bg_color,
                                 fg='white').grid(row=5, column=0, padx=10, pady=10, sticky='w')
        tea_text = Entry(F3, width=10,textvariable=self.tea, font=('times new roman', 16, 'bold'),
                                bd=5, relief=SUNKEN).grid(row=5, column=1, padx=10, pady=10)

        #coldrinkFrame

        F4 = LabelFrame(self.root, text='Cold Drinks', bd=10, relief=GROOVE, font=('times new roman', 15, 'bold'),
                        bg=bg_color, fg='gold')
        F4.place(x=670, y=185, width=325, height=380)
        maza_label = Label(F4, text="Maaza", font=('times new roman', 16, 'bold'), bg=bg_color,
                           fg='white').grid(row=0, column=0, padx=10, pady=10, sticky='w')
        maza_text = Entry(F4, width=10, textvariable=self.maza,font=('times new roman', 16, 'bold'),
                          bd=5, relief=SUNKEN).grid(row=0, column=1, padx=10, pady=10)
        pepsi_label = Label(F4, text="Pepsi", font=('times new roman', 16, 'bold'), bg=bg_color,
                                fg='white').grid(row=1, column=0, padx=10, pady=10, sticky='w')
        pepsi_text = Entry(F4, width=10, textvariable=self.pepsi,font=('times new roman', 16, 'bold'),
                               bd=5, relief=SUNKEN).grid(row=1, column=1, padx=10, pady=10)
        sprite_label = Label(F4, text="Sprite", font=('times new roman', 16, 'bold'), bg=bg_color,
                               fg='white').grid(row=2, column=0, padx=10, pady=10, sticky='w')
        sprite_text = Entry(F4, width=10,textvariable=self.sprite, font=('times new roman', 16, 'bold'),
                              bd=5, relief=SUNKEN).grid(row=2, column=1, padx=10, pady=10)
        dew_label = Label(F4, text="Dew", font=('times new roman', 16, 'bold'), bg=bg_color,
                                fg='white').grid(row=3, column=0, padx=10, pady=10, sticky='w')
        dew_text = Entry(F4, width=10,textvariable=self.dew, font=('times new roman', 16, 'bold'),
                               bd=5, relief=SUNKEN).grid(row=3, column=1, padx=10, pady=10)
        frooti_label = Label(F4, text="Frooti", font=('times new roman', 16, 'bold'), bg=bg_color,
                              fg='white').grid(row=4, column=0, padx=10, pady=10, sticky='w')
        frooti_text = Entry(F4, width=10,textvariable=self.frooti, font=('times new roman', 16, 'bold'),
                             bd=5, relief=SUNKEN).grid(row=4, column=1, padx=10, pady=10)
        cocacola_label = Label(F4, text="Coca cola", font=('times new roman', 16, 'bold'), bg=bg_color,
                                 fg='white').grid(row=5, column=0, padx=10, pady=10, sticky='w')
        cocacola_text = Entry(F4, width=10,textvariable=self.cocacola, font=('times new roman', 16, 'bold'),
                                bd=5, relief=SUNKEN).grid(row=5, column=1, padx=10, pady=10)

        #bill area

        F5 =Frame(self.root, bd=10, relief=GROOVE)
        F5.place(x=1010, y=185, width=340, height=380)

        bill_title=Label(F5,text='Bill Area', font=('times new roman', 16, 'bold'),bd=7,relief=GROOVE).pack(fill=X)

        scroll_y=Scrollbar(F5,orient=VERTICAL)
        self.textarea=Text(F5,yscrollcommand=scroll_y.set,)
        scroll_y.pack(side=RIGHT,fill=Y)
        scroll_y.config(command=self.textarea.yview)
        self.textarea.pack(fill=BOTH,expand=1)


        #bill menu

        F6 = LabelFrame(self.root, text='Bill Menu', bd=10, relief=GROOVE, font=('times new roman', 15, 'bold'),
                        bg=bg_color, fg='gold')
        F6.place(x=0, y=560, relwidth=1, height=140)

        totalcosmeticprice_label = Label(F6, text="Total Cosmetic Price", font=('times new roman', 14, 'bold'), bg=bg_color,
                          fg='white').grid(row=0, column=0, padx=10, pady=3, sticky='w')
        totalcosmeticprice_text = Entry(F6, width=18,textvariable=self.cosmeticprice, font=('times new roman', 10, 'bold'),
                         bd=5, relief=SUNKEN).grid(row=0, column=1, padx=10, pady=3)

        totalgroceryprice_label = Label(F6, text="Total Grocery Price", font=('times new roman', 14, 'bold'), bg=bg_color,
                          fg='white').grid(row=1, column=0, padx=10, pady=3, sticky='w')
        totalgroceryprice_text = Entry(F6, width=18,textvariable=self.groceryprice, font=('times new roman', 10, 'bold'),
                         bd=5, relief=SUNKEN).grid(row=1, column=1, padx=10, pady=3)

        totalcolddrinkprice_label = Label(F6, text="Total Cold Drink Price ", font=('times new roman', 14, 'bold'), bg=bg_color,
                          fg='white').grid(row=2, column=0, padx=10, pady=3, sticky='w')
        totalcolddrinkprice_text = Entry(F6, width=18,textvariable=self.colddrinkprice, font=('times new roman', 10, 'bold'),
                         bd=5, relief=SUNKEN).grid(row=2, column=1, padx=10, pady=3)

        cosmetictax_label = Label(F6, text="Cosmetic Tax", font=('times new roman', 14, 'bold'),
                                         bg=bg_color,
                                         fg='white').grid(row=0, column=2, padx=10, pady=3, sticky='w')
        cosmetictax_text = Entry(F6, width=18,textvariable=self.cosmetictax, font=('times new roman', 10, 'bold'),
                                        bd=5, relief=SUNKEN).grid(row=0, column=3, padx=10, pady=3)

        grocerytax_label = Label(F6, text="Grocery Tax", font=('times new roman', 14, 'bold'),
                                        bg=bg_color,
                                        fg='white').grid(row=1, column=2, padx=10, pady=3, sticky='w')
        grocerytax_text = Entry(F6, width=18,textvariable=self.grocerytax, font=('times new roman', 10, 'bold'),
                                       bd=5, relief=SUNKEN).grid(row=1, column=3, padx=10, pady=3)

        colddrinktax_label = Label(F6, text="Cold Drink Tax", font=('times new roman', 14, 'bold'),
                                          bg=bg_color,
                                          fg='white').grid(row=2, column=2, padx=10, pady=3, sticky='w')
        colddrinktax_text = Entry(F6, width=18,textvariable=self.colddrinktax, font=('times new roman', 10, 'bold'),
                                         bd=5, relief=SUNKEN).grid(row=2, column=3, padx=10, pady=3)

        btn_frame=Frame(F6,bd=7,relief=GROOVE)
        btn_frame.place(x=720,width=590,height=105)

        total_btn=Button(btn_frame,text='Total',bg=bg_color,fg='white',pady=15, width=10,bd=3,
                         font=('arial', 15, 'bold'),command=self.total).grid(row=0,column=0,padx=5,pady=5)

        bill_btn = Button(btn_frame, text='Bill',command=self.bill_area, bg=bg_color, fg='white', pady=15, width=10, bd=3,
                           font=('arial', 15, 'bold')).grid(row=0, column=1, padx=5, pady=5)

        clear_btn = Button(btn_frame, text='Clear', bg=bg_color, fg='white', pady=15, width=10, bd=3,command=self.clear,
                           font=('arial', 15, 'bold')).grid(row=0, column=2, padx=5, pady=5)
        exit_btn = Button(btn_frame, text='Exit', bg=bg_color, fg='white', pady=15, width=10, bd=3,command=self.exit_,
                           font=('arial', 15, 'bold')).grid(row=0, column=3, padx=5, pady=5)



    def total(self):
        self.soapprice=(self.soap.get()*20)
        self.facecreamprice=(self.facecream.get()*60)
        self.facewashprice= (self.facewash.get()*100)
        self.sprayprice=(self.spray.get()*120)
        self.gelprice=(self.gel.get()*120)
        self.lotionprice=(self.lotion.get()*80)
        self.total_cosmetic_price=float(
            (self.soap.get()*20)+
            (self.facecream.get()*60)+
            (self.facewash.get()*100)+
            (self.spray.get()*120)+
            (self.gel.get()*80)+
            (self.lotion.get()*80)

        )
        self.ctax=round((self.total_cosmetic_price*0.05),2)
        self.cosmeticprice.set(str(self.total_cosmetic_price)+' Rs')
        self.cosmetictax.set(str(self.ctax)+' Rs')

        self.oilprice=(self.oil.get() * 100)
        self.daalprice=(self.daal.get() * 80)
        self.teaprice=(self.tea.get() * 50)
        self.wheatprice=(self.wheat.get() * 30)
        self.riceprice=(self.rice.get() * 70)
        self.sugarprice=(self.sugar.get() * 40)
        self.total_grocery_price = float(
            (self.oil.get() * 100) +
            (self.daal.get() * 80) +
            (self.tea.get() * 50) +
            (self.wheat.get() * 30) +
            (self.rice.get() * 70) +
            (self.sugar.get() * 40)
        )
        self.gtax=round((self.total_grocery_price * 0.08),2)
        self.groceryprice.set(str(self.total_grocery_price) + ' Rs')
        self.grocerytax.set(str(self.gtax)+' Rs')


        self.mazaprice=(self.maza.get() * 20)
        self.frootiprice=(self.frooti.get() * 20)
        self.cocacolaprice=(self.cocacola.get() * 80)
        self.dewprice=(self.dew.get() * 80)
        self.spriteprice=(self.sprite.get() * 80)
        self.pepsiprice=(self.pepsi.get() * 80)

        self.total_colddrink_price = float(
            (self.maza.get() * 20) +
            (self.frooti.get() * 20) +
            (self.cocacola.get() * 80) +
            (self.dew.get() * 80) +
            (self.sprite.get() * 80) +
            (self.pepsi.get() * 80)

        )
        self.coldtax=round((self.total_colddrink_price * 0.02),2)
        self.colddrinkprice.set(str(self.total_colddrink_price) + ' Rs')
        self.colddrinktax.set(str(self.coldtax)+' Rs')

        self.total_bill=round(self.total_cosmetic_price+self.total_grocery_price+self.total_colddrink_price+self.ctax+self.gtax+self.coldtax)

    def welcome_bill(self):

        self.textarea.insert(END,"\t ** Welcome Customer **\n ")
        self.textarea.insert(END,f'\n Bill Number : {self.billnumber.get()}')
        self.textarea.insert(END, f'\n Customer Name : {self.cname.get()}')
        self.textarea.insert(END, f'\n Phone Number : {self.cphone.get()}')
        self.textarea.insert(END, f'\n ====================================')
        self.textarea.insert(END, f'\n Products\t\tQTY\t\tPrice')


        self.textarea.insert(END, f'\n ====================================')

    def bill_area(self):
        if self.cname.get()==''or self.cphone.get()=='':
            messagebox.showerror("Error","Customer Details Required")
        elif self.cosmeticprice.get()=='0.0 Rs'and self.groceryprice.get()=='0.0 Rs'and self.colddrinkprice.get()=='0.0 Rs':
            messagebox.showerror("Error", "No Product Purchased")

        else:
            self.welcome_bill()
            #cosmetics
            if self.soap.get()!=0:
                self.textarea.insert(END, f'\n Bath Soap\t\t{self.soap.get()}\t\t{self.soapprice}')

            if self.facecream.get() != 0:
                self.textarea.insert(END, f'\n Face Cream\t\t{self.facecream.get()}\t\t{self.facecreamprice}')

            if self.facewash.get() != 0:
                self.textarea.insert(END, f'\n Face Wash\t\t{self.facewash.get()}\t\t{self.facewashprice}')

            if self.spray.get() != 0:
                self.textarea.insert(END, f'\n Hair Spray\t\t{self.spray.get()}\t\t{self.sprayprice}')

            if self.gel.get() != 0:
                self.textarea.insert(END, f'\n Hair Gel\t\t{self.gel.get()}\t\t{self.gelprice}')

            if self.lotion.get() != 0:
                self.textarea.insert(END, f'\n Body Lotion\t\t{self.lotion.get()}\t\t{self.lotionprice}')

                #grocery

            if self.daal.get() != 0:
                self.textarea.insert(END, f'\n Daal\t\t{self.daal.get()}\t\t{self.daalprice}')

            if self.wheat.get() != 0:
                self.textarea.insert(END, f'\n Wheat\t\t{self.wheat.get()}\t\t{self.wheatprice}')

            if self.sugar.get() != 0:
                self.textarea.insert(END, f'\n Sugar\t\t{self.sugar.get()}\t\t{self.sugarprice}')

            if self.tea.get() != 0:
                self.textarea.insert(END, f'\n Tea\t\t{self.tea.get()}\t\t{self.teaprice}')

            if self.oil.get() != 0:
                self.textarea.insert(END, f'\n Oil\t\t{self.oil.get()}\t\t{self.oilprice}')

            if self.rice.get() != 0:
                self.textarea.insert(END, f'\n Rice\t\t{self.rice.get()}\t\t{self.riceprice}')


            #colddrink

            if self.maza.get() != 0:
                self.textarea.insert(END, f'\n Maaza\t\t{self.maza.get()}\t\t{self.mazaprice}')

            if self.frooti.get() != 0:
                self.textarea.insert(END, f'\n Frooti\t\t{self.frooti.get()}\t\t{self.frootiprice}')

            if self.dew.get() != 0:
                self.textarea.insert(END, f'\n Dew\t\t{self.dew.get()}\t\t{self.dewprice}')

            if self.cocacola.get() != 0:
                self.textarea.insert(END, f'\n Coca cola\t\t{self.cocacola.get()}\t\t{self.cocacolaprice}')

            if self.sprite.get() != 0:
                self.textarea.insert(END, f'\n Sprite\t\t{self.sprite.get()}\t\t{self.spriteprice}')

            if self.pepsi.get() != 0:
                self.textarea.insert(END, f'\n Pepsi\t\t{self.pepsi.get()}\t\t{self.pepsiprice}')

            self.textarea.insert(END, f'\n ------------------------------------')
            if self.cosmetictax.get()!='0.0 Rs':
                self.textarea.insert(END, f'\n Cosmetic Tax\t\t\t{self.cosmetictax.get()}')

            if self.grocerytax.get()!='0.0 Rs':
                self.textarea.insert(END, f'\n Grocery Tax\t\t\t{self.grocerytax.get()}')

            if self.colddrinktax.get()!='0.0 Rs':
                self.textarea.insert(END, f'\n Cold drink Tax\t\t\t{self.colddrinktax.get()}')


            self.textarea.insert(END, f'\n\n Total Bill\t\t\t{self.total_bill} Rs')

            self.textarea.insert(END, f'\n ------------------------------------')
            self.save_bill()

    def save_bill(self):
        op=messagebox.askyesno("Save Bill","Do you want to save the Bill?")
        if op:
            self.bill_data=self.textarea.get('1.0',END)
            f1=open("bills/"+str(self.billnumber.get())+'.txt','w')
            f1.write(self.bill_data)
            f1.close()
            messagebox.showinfo("Saved",f'Bill No {self.billnumber.get()} is saved successfully!')
        else:
            return

    def find_bill(self):
        present='no'
        for i in os.listdir('bills/'):
            if i.split('.')[0]==self.searchbill.get():
                f1=open(f'bills/{i}','r')
                self.textarea.delete('1.0',END)
                for d in f1:
                    self.textarea.insert(END,d)
                f1.close()
                present='yes'
        if present=='no':
            messagebox.showerror("Error","Invalid Bill No")

    def clear(self):
        op=messagebox.askyesno("Clear","Do you really want to clear? ")
        if op:
            self.soap.set(0)
            self.facecream.set(0)
            self.facewash.set(0)
            self.spray.set(0)
            self.gel.set(0)
            self.lotion.set(0)

            # grocery variables

            self.rice.set(0)
            self.oil.set(0)
            self.daal.set(0)
            self.wheat.set(0)
            self.sugar.set(0)
            self.tea.set(0)

            # colddrink variables

            self.maza.set(0)
            self.pepsi.set(0)
            self.sprite.set(0)
            self.dew.set(0)
            self.frooti.set(0)
            self.cocacola.set(0)

            # total product price and tax variables

            self.cosmeticprice.set('')
            self.groceryprice.set('')
            self.colddrinkprice.set('')

            self.cosmetictax.set('')
            self.grocerytax.set('')
            self.colddrinktax.set('')

            # customer details variables
            self.cname.set('')
            self.cphone.set('')

            self.billnumber.set('')

            self.searchbill.set('')

    def exit_(self):
        op=messagebox.askyesno("Exit","Do you really want to exit?")
        if op:
            self.root.destroy()





root=Tk()
obj=Bill_App(root)
root.mainloop()