from tkinter import*
from tkinter.font import BOLD
class Bill_App:
    def __init__(self,root): 
        self.root=root
        self.root.geometry("1350x700+0+0")
        self.root.title("Billing sodtware system")
        title=Label(self.root,text="Billing software",bd=12,relief=GROOVE,bg="gray",fg="white",font=("times new roman",30,"bold"),pady=2).pack(fill=X)

        #===CUSTOMER DETAIL FRAME
        F1=LabelFrame(self.root,bd=10,relief=GROOVE,text="Customer Details",font=("times new roman",15,"bold"),fg="gold",bg="gray")
        F1.place(x=10,y=80,relwidth=1)         
    
        cname_lbl=Label(F1,text="Customer Name",bg="gray",fg="white",font=("times new roman",18,"bold")).grid(row=0,column=0,padx=20,pady=5)
        cname=txt=Entry(F1,width=15,font="arial 15",bd=7,relief=SUNKEN).grid(row=0,column=1,pady=5,padx=10)
        
        cPhn_lbl=Label(F1,text="Phone No",bg="gray",fg="white",font=("times new roman",18,"bold")).grid(row=0,column=2,padx=20,pady=5)
        cPhn=txt=Entry(F1,width=15,font="arial 15",bd=7,relief=SUNKEN).grid(row=0,column=3,pady=5,padx=10)
        
        c_bill_lbl=Label(F1,text="Bill No",bg="gray",fg="white",font=("times new roman",18,"bold")).grid(row=0,column=4,padx=20,pady=5)
        c_bill_=txt=Entry(F1,width=15,font="arial 15",bd=7,relief=SUNKEN).grid(row=0,column=5,pady=5,padx=10)
        
        bill_btn=Button(F1,text="Search",width=10,bd=7,font="arial 12 bold").grid(row=0,column=6,padx=10,pady=10)

        #========COSMETTIC FRAME==========#
        F2=LabelFrame(self.root,bd=10,relief=GROOVE,text="Cosmatic",font=("times new roman",15,"bold"),fg="gold",bg="gray")
        F2.place(x=5,y=180,width=325,height=380)
        
        bath_Lbl=Label(F2,text="Bath soap",font=("times new roman",16,"bold"),bg="gray",fg="lightgreen").grid(row=0,column=0,padx=10,pady=10,sticky="w")
        bath_txt=Entry(F2,width=10,font=("times new roman",16,"bold"),bd=5,relief=SUNKEN).grid(row=0,column=1,padx=10,pady=10) 
        
        
        Face_cream_Lbl=Label(F2,text="Face Cream",font=("times new roman",16,"bold"),bg="gray",fg="lightgreen").grid(row=2,column=0,padx=10,pady=10,sticky="w")
        Face_cream_txt=Entry(F2,width=10,font=("times new roman",16,"bold"),bd=5,relief=SUNKEN).grid(row=2,column=1,padx=10,pady=10) 
        
        
        Face_w_Lbl=Label(F2,text="Face Wash",font=("times new roman",16,"bold"),bg="gray",fg="lightgreen").grid(row=3,column=0,padx=10,pady=10,sticky="w")
        Face_w__txt=Entry(F2,width=10,font=("times new roman",16,"bold"),bd=5,relief=SUNKEN).grid(row=3,column=1,padx=10,pady=10) 
        
        
        Hair_s_Lbl=Label(F2,text="Hair spray",font=("times new roman",16,"bold"),bg="gray",fg="lightgreen").grid(row=4,column=0,padx=10,pady=10,sticky="w")
        Hair_s_txt=Entry(F2,width=10,font=("times new roman",16,"bold"),bd=5,relief=SUNKEN).grid(row=4,column=1,padx=10,pady=10) 
        
        
        Hair_g_Lbl=Label(F2,text="Hair Gell",font=("times new roman",16,"bold"),bg="gray",fg="lightgreen").grid(row=5,column=0,padx=10,pady=10,sticky="w")
        Hair_g_txt=Entry(F2,width=10,font=("times new roman",16,"bold"),bd=5,relief=SUNKEN).grid(row=5,column=1,padx=10,pady=10) 
        
        
        Body_l_Lbl=Label(F2,text="Body Loshan",font=("times new roman",16,"bold"),bg="gray",fg="lightgreen").grid(row=6,column=0,padx=10,pady=10,sticky="w")
        Body_l_txt=Entry(F2,width=10,font=("times new roman",16,"bold"),bd=5,relief=SUNKEN).grid(row=6,column=1,padx=10,pady=10) 
        
        
        
        #========Grocery FRAME==========#
        F3=LabelFrame(self.root,bd=10,relief=GROOVE,text="Grocery",font=("times new roman",15,"bold"),fg="gold",bg="gray")
        F3.place(x=340,y=180,width=325,height=380)
        
        rice_Lbl=Label(F3,text="Rice",font=("times new roman",16,"bold"),bg="gray",fg="lightgreen").grid(row=0,column=0,padx=10,pady=10,sticky="w")
        rice_txt=Entry(F3,width=10,font=("times new roman",16,"bold"),bd=5,relief=SUNKEN).grid(row=0,column=1,padx=10,pady=10) 
        
        
        Food_oil_Lbl=Label(F3,text="Food Oil",font=("times new roman",16,"bold"),bg="gray",fg="lightgreen").grid(row=2,column=0,padx=10,pady=10,sticky="w")
        Food_oil_txt=Entry(F3,width=10,font=("times new roman",16,"bold"),bd=5,relief=SUNKEN).grid(row=2,column=1,padx=10,pady=10) 
        
        
        Daal_Lbl=Label(F3,text="Daal",font=("times new roman",16,"bold"),bg="gray",fg="lightgreen").grid(row=3,column=0,padx=10,pady=10,sticky="w")
        Daal_txt=Entry(F3,width=10,font=("times new roman",16,"bold"),bd=5,relief=SUNKEN).grid(row=3,column=1,padx=10,pady=10) 
        
        
        Wheat_Lbl=Label(F3,text="Wheat",font=("times new roman",16,"bold"),bg="gray",fg="lightgreen").grid(row=4,column=0,padx=10,pady=10,sticky="w")
        Wheat_txt=Entry(F3,width=10,font=("times new roman",16,"bold"),bd=5,relief=SUNKEN).grid(row=4,column=1,padx=10,pady=10) 
        
        
        sugar_Lbl=Label(F3,text="Hair Gell",font=("times new roman",16,"bold"),bg="gray",fg="lightgreen").grid(row=5,column=0,padx=10,pady=10,sticky="w")
        sugar_txt=Entry(F3,width=10,font=("times new roman",16,"bold"),bd=5,relief=SUNKEN).grid(row=5,column=1,padx=10,pady=10) 
        
        
        Tea_Lbl=Label(F3,text="Body Loshan",font=("times new roman",16,"bold"),bg="gray",fg="lightgreen").grid(row=6,column=0,padx=10,pady=10,sticky="w")
        Tea_txt=Entry(F3,width=10,font=("times new roman",16,"bold"),bd=5,relief=SUNKEN).grid(row=6,column=1,padx=10,pady=10) 
        
        
           
        #========Call Drinks==========#
        F4=LabelFrame(self.root,bd=10,relief=GROOVE,text="Cold Drinks",font=("times new roman",15,"bold"),fg="gold",bg="gray")
        F4.place(x=670,y=180,width=325,height=380)
        
        Maza_Lbl=Label(F4,text="Maze",font=("times new roman",16,"bold"),bg="gray",fg="lightgreen").grid(row=0,column=0,padx=10,pady=10,sticky="w")
        Maza_txt=Entry(F4,width=10,font=("times new roman",16,"bold"),bd=5,relief=SUNKEN).grid(row=0,column=1,padx=10,pady=10) 
        
        
        Cock_Lbl=Label(F4,text="Cock",font=("times new roman",16,"bold"),bg="gray",fg="lightgreen").grid(row=2,column=0,padx=10,pady=10,sticky="w")
        Cock_txt=Entry(F4,width=10,font=("times new roman",16,"bold"),bd=5,relief=SUNKEN).grid(row=2,column=1,padx=10,pady=10) 
        
        
        Frooti_Lbl=Label(F4,text="Footi",font=("times new roman",16,"bold"),bg="gray",fg="lightgreen").grid(row=3,column=0,padx=10,pady=10,sticky="w")
        Frooti_txt=Entry(F4,width=10,font=("times new roman",16,"bold"),bd=5,relief=SUNKEN).grid(row=3,column=1,padx=10,pady=10) 
        
        
        Thumbs_up_Lbl=Label(F4,text="Thumbs Up",font=("times new roman",16,"bold"),bg="gray",fg="lightgreen").grid(row=4,column=0,padx=10,pady=10,sticky="w")
        Thumbs_up_txt=Entry(F4,width=10,font=("times new roman",16,"bold"),bd=5,relief=SUNKEN).grid(row=4,column=1,padx=10,pady=10) 
        
        
        Sprite_Lbl=Label(F4,text="Sprite",font=("times new roman",16,"bold"),bg="gray",fg="lightgreen").grid(row=5,column=0,padx=10,pady=10,sticky="w")
        Sprite_txt=Entry(F4,width=10,font=("times new roman",16,"bold"),bd=5,relief=SUNKEN).grid(row=5,column=1,padx=10,pady=10) 
        
        
        Red_Bull_Lbl=Label(F4,text="Red Bull",font=("times new roman",16,"bold"),bg="gray",fg="lightgreen").grid(row=6,column=0,padx=10,pady=10,sticky="w")
        Red_Bull_txt=Entry(F4,width=10,font=("times new roman",16,"bold"),bd=5,relief=SUNKEN).grid(row=6,column=1,padx=10,pady=10) 
        
        
        #======= Bill Area ==========#
        F5=Frame(self.root,bd=10,relief=GROOVE)
        F5.place(x=1010,y=180,width=520,height=380)
        bill_title=Label(F5,text="Bill Area",font="arial 15 bold",bd=7,relief=GROOVE).pack(fill=X)
        scrol_y=Scrollbar(F5,orient=VERTICAL)
        self.textarea=Text(F5,yscrollcommand=scrol_y.set)
        scrol_y.pack(side=RIGHT,fill=Y)
        scrol_y.config(command=self.textarea.yview)
        self.textarea.pack(fill=BOTH,expand=1)
        
        #=======Button Frame ==========#
        F6=Label(self.root,bd=10,relief=GROOVE,text="",font=("times new roman",15,"bold"),fg="gold",bg="gray")
        F6.place(x=0,y=560,relwidth=1,height=240)
       
        m1_lbl=Label(F6,text="Total Cosemetic Price",bg="gray",fg="white",font=("times new roman ",14,"bold")).grid(row=0,column=0,padx=10,pady=1,sticky="w")
        m1_txt=Entry(F6,width=18,font="arial 10 bold",bd=7,relief=SUNKEN).grid(row=0,column=1,padx=10,pady=1)
        
        m2_lbl=Label(F6,text="Total Grocery Price",bg="gray",fg="white",font=("times new roman ",14,"bold")).grid(row=1,column=0,padx=10,pady=1,sticky="w")
        m2_txt=Entry(F6,width=18,font="arial 10 bold",bd=7,relief=SUNKEN).grid(row=1,column=1,padx=10,pady=1)
       
        m3_lbl=Label(F6,text="Total Cold drink Price",bg="gray",fg="white",font=("times new roman ",14,"bold")).grid(row=2,column=0,padx=10,pady=1,sticky="w")
        m3_txt=Entry(F6,width=18,font="arial 10 bold",bd=7,relief=SUNKEN).grid(row=2,column=1,padx=10,pady=1)
        
        
        c1_lbl=Label(F6,text="Cosemetic Tax",bg="gray",fg="white",font=("times new roman ",14,"bold")).grid(row=0,column=2,padx=10,pady=1,sticky="w")
        c1_txt=Entry(F6,width=18,font="arial 10 bold",bd=7,relief=SUNKEN).grid(row=0,column=3,padx=10,pady=1)
        
        c2_lbl=Label(F6,text="Grocery Tax",bg="gray",fg="white",font=("times new roman ",14,"bold")).grid(row=1,column=2,padx=10,pady=1,sticky="w")
        c2_txt=Entry(F6,width=18,font="arial 10 bold",bd=7,relief=SUNKEN).grid(row=1,column=3,padx=10,pady=1)
       
        c3_lbl=Label(F6,text="Cold drink Tax",bg="gray",fg="white",font=("times new roman ",14,"bold")).grid(row=2,column=2,padx=10,pady=1,sticky="w")
        c3_txt=Entry(F6,width=18,font="arial 10 bold",bd=7,relief=SUNKEN).grid(row=2,column=3,padx=10,pady=1)
        
        btn_F=Frame(F6,bd=7,relief=GROOVE)
        btn_F.place(x=740,width=770,height=105)
        
        total_btn=Button(btn_F,text="Total",bg="cadetblue",fg="white",bd=2,pady=15,width=11,font="arial 15 bold").grid=(row=0,column=0,padx=5,pady=5)

        
        GBill_btn=Button(btn_F,text="Generate Bill",bg="cadetblue",fg="white",bd=5,pady=15,width=11,font="arial 15 bold").grid=(row=0,column=0,padx=5,pady=5)

        
        Clear_btn=Button(btn_F,text="Clear",bg="cadetblue",fg="white",bd=5,pady=15,width=11,font="arial 15 bold").grid=(row=0,column=0,padx=5,pady=5)

        
        Exit_btn=Button(btn_F,text="Exit",bg="cadetblue",fg="white",bd=5,pady=15,width=11,font="arial 15 bold").grid=(row=0,column=0,padx=5,pady=5)

root=Tk()
obj=Bill_App(root)
root.mainloop()    