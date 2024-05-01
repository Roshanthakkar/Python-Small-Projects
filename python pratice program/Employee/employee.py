from tkinter import*
class EmployeeSystem:
    def __init__(self,root):
        self.root=root
        self.root.title("Employee payroll management system | Develop roshan thakkkar")
        self.root.geometry("1350x700+0+0") 
        self.root.config(bg="white")  
        title=Label(self.root,text="Employee payroll management system",font=("times new roman",30,"bold"),bg="#262626",fg="white",anchor="w",padx=10).place(x=0,y=0,relwidth=1)
        
        # Employee basic detail in frame 1
        Frame1=Frame(self.root,bd=3,relief=RIDGE,bg='white')
        Frame1.place(x=10,y=70,width=750,heigh=620)
        
        title2=Label(Frame1,text="Employee Details",font=("times new roman",20),bg="lightgray",fg="black",anchor="w",padx=10).place(x=0,y=0,relwidth=1)
        
        lbl_code=Label(Frame1,text="Employee code",font=("times new roman",20),bg="white",fg="black").place(x=10,y=70)
        txt_Code=Entry(Frame1,font=("times new roman",15),bg="lightyellow",fg="black").place(x=220,y=74,width=200)  
        btn_Search=Button(Frame1,text="Search",font=("times new roman",20),bg="gray",fg="black").place(x=440,y=72,height=30)
        
        #======Row1=====#
        lbl_Designation=Label(Frame1,text="Designation",font=("times new roman",20),bg="white",fg="black").place(x=10,y=120)
        txt_Designation=Entry(Frame1,font=("times new roman",15),bg="lightyellow",fg="black").place(x=170,y=125,width=200)  
        lbl_DOB=Label(Frame1,text="D.O.B",font=("times new roman",20),bg="white",fg="black").place(x=390,y=120)
        txt_DOB=Entry(Frame1,font=("times new roman",15),bg="lightyellow",fg="black").place(x=520,y=125)

        #======Row2=====#
        lbl_Name=Label(Frame1,text="Name",font=("times new roman",20),bg="white",fg="black").place(x=10,y=170)
        txt_Name=Entry(Frame1,font=("times new roman",15),bg="lightyellow",fg="black").place(x=170,y=175,width=200)  
        lbl_DOj=Label(Frame1,text="D.O.J",font=("times new roman",20),bg="white",fg="black").place(x=390,y=170)
        txt_DOj=Entry(Frame1,font=("times new roman",15),bg="lightyellow",fg="black").place(x=520,y=175)
        
        #======Row3=====#
        lbl_Age=Label(Frame1,text="Age",font=("times new roman",20),bg="white",fg="black").place(x=10,y=220)
        txt_Age=Entry(Frame1,font=("times new roman",15),bg="lightyellow",fg="black").place(x=170,y=225,width=200)  
        lbl_Experince=Label(Frame1,text="Expernice",font=("times new roman",20),bg="white",fg="black").place(x=390,y=220)
        txt_Experince=Entry(Frame1,font=("times new roman",15),bg="lightyellow",fg="black").place(x=520,y=225)
        
        #======Row4=====#
        lbl_Gender=Label(Frame1,text="Gender",font=("times new roman",20),bg="white",fg="black").place(x=10,y=270)
        txt_Gender=Entry(Frame1,font=("times new roman",15),bg="lightyellow",fg="black").place(x=170,y=275,width=200)  
        lbl_Proof=Label(Frame1,text="Proof-ID",font=("times new roman",20),bg="white",fg="black").place(x=390,y=270)
        txt_Proof=Entry(Frame1,font=("times new roman",15),bg="lightyellow",fg="black").place(x=520,y=275)
        
        #======Row5=====#
        lbl_Email=Label(Frame1,text="E-mail",font=("times new roman",20),bg="white",fg="black").place(x=10,y=320)
        txt_Email=Entry(Frame1,font=("times new roman",15),bg="lightyellow",fg="black").place(x=170,y=325,width =200)  
        lbl_Contact=Label(Frame1,text="Contact",font=("times new roman",20),bg="white",fg="black").place(x=390,y=320)
        txt_Contact=Entry(Frame1,font=("times new roman",15),bg="lightyellow",fg="black").place(x=520,y=325)
        
        #======Row6=====#
        lbl_Hired=Label(Frame1,text="Hired Location",font=("times new roman",18),bg="white",fg="black").place(x=10,y=372)
        txt_Hired=Entry(Frame1,font=("times new roman",15),bg="lightyellow",fg="black").place(x=170,y=375,width =200)  
        lbl_Status=Label(Frame1,text="Status",font=("times new roman",20),bg="white",fg="black").place(x=390,y=370)
        txt_Status=Entry(Frame1,font=("times new roman",15),bg="lightyellow",fg="black").place(x=520,y=375)
        
        #======Row7=====#
        lbl_address=Label(Frame1,text="Address",font=("times new roman",18),bg="white",fg="black").place(x=10,y=422)
        txt_address=Text(Frame1,font=("times new roman",15),bg="lightyellow",fg="black").place(x=170,y=425,width =200)  
        txt_address.place(x=170,y=425,width=550,height=150)
        
        # Employee 2nd logout detail in frmae 2
        Frame2=Frame(self.root,bd=3,relief=RIDGE,bg='white')
        Frame2.place(x=770,y=70,width=580,heigh=300)

        # Frame 3
        Frame3=Frame(self.root,bd=3,relief=RIDGE,bg='white')
        Frame3.place(x=770,y=380,width=580,heigh=310)
root=Tk()
obj=EmployeeSystem(root)
root.mainloop()