# moduless imported
from tkinter import *
from PIL import ImageTk,Image
from tkinter import ttk # for combo box
from tkinter import messagebox,filedialog
import mysql.connector as mysql
#from plyer import notification
#import  pandas



# studet add  function defined
def addd(event):
    global rows
    name = name_entry.get()
    roll_no = roll_no_entry.get()
    email = email_entry.get()
    gender = val.get()
    contact_no = contact_no_entry.get()
    dob = dob_entry.get()
    address = address_entry.get()
    if (name == "" or roll_no == "" or email == "" or contact_no == "" or dob == "" or address == ""):
        messagebox.showerror("Insert Status", "All Flied Are Requried")
    else:
        con = mysql.connect(host="localhost", user="root", password="", database="student")
        cursor = con.cursor()
        cursor.execute(
            "insert into data3 values('" + name + "','" + roll_no + "','" + email + "','" + gender + "','" + contact_no + "','" + dob + "','" + address + "')")
        cursor.execute("commit")

        name_entry.delete(0, 'end')
        roll_no_entry.delete(0, 'end')
        email_entry.delete(0, 'end')
        val.delete(0, 'end')
        contact_no_entry.delete(0, 'end')
        dob_entry.delete(0, 'end')
        address_entry.delete(0, 'end')
        fetch()
        messagebox.showinfo("Insert Status", "Insert SucessFUlly")
        con.close()


# studennt  data fetch function defined
def fetch():
    global rows
    con = mysql.connect(host="localhost", user="root", password="", database="student")
    cursor = con.cursor()
    cursor.execute("select *from data3")
    rows = cursor.fetchall()
    if len(rows) != 0:
        tabel.delete(*tabel.get_children())
        for row in rows:
            tabel.insert('', END, values=row)
            con.commit()

    con.close()


# export data to the excel  file function defined
def export():
    file = filedialog.asksaveasfilename()
    get = tabel.get_children()
    first, second, third, four, fifth, six, seven = [], [], [], [], [], [], []
    for i in get:
        content = tabel.item(i)
        val = content['values']
        first.append(val[0]), second.append(val[1]), third.append(val[2]), four.append(val[3]), fifth.append(
            val[4]), six.append(val[5]),
        seven.append(val[6])
    dd = ['name', 'roll_no', 'email', 'gender', 'contact_no', 'dob', 'address']
    df = pandas.DataFrame(list(zip(first, second, third, four, fifth, six, seven)), columns=dd)
    paths = r'{}.csv'.format(file)
    df.to_csv(paths, index=False)
    messagebox.showinfo('Notifications', 'Student data is Saved {}'.format(paths))


# get the values in entry widgth function defined
def get_data(event):
    cur = tabel.focus()
    left = tabel.item(cur)
    row = left['values']

    name.set(row[0])
    roll_no.set(row[1])
    email.set(row[2])
    gender.set(row[3])
    contact_no.set(row[4])
    dob.set(row[5])
    address.set(row[6])


# update the student data function defined
def update():
    name = name_entry.get()
    roll_no = roll_no_entry.get()
    email = email_entry.get()
    gender = val.get()
    contact_no = contact_no_entry.get()
    dob = dob_entry.get()
    address = address_entry.get()
    if (name == "" or roll_no == "" or email == "" or contact_no == "" or dob == "" or address == ""):
        messagebox.showerror("Update Status", "All Flieds Are Requried")
    else:
        con = mysql.connect(host="localhost", user="root", password="", database="student")
        cursor = con.cursor()
        cursor.execute(
            "update data3 set name='" + name + "',email='" + email + "',gender='" + gender + "',contact_no='" + contact_no + "',dob='" + dob + "',address='" + address + "' where roll_no='" + roll_no + "'")
        cursor.execute("commit")
        name_entry.delete(0, 'end')
        roll_no_entry.delete(0, 'end')
        email_entry.delete(0, 'end')
        val.delete(0, 'end')
        contact_no_entry.delete(0, 'end')
        dob_entry.delete(0, 'end')
        address_entry.delete(0, 'end')
        fetch()
        messagebox.showinfo("Update Status", "Updated SucessFully")
        con.close()


# delte student data function defined
def deletee(event=""):
    if (roll_no_entry.get() == ""):
        messagebox.showerror("Delete", "Delete Requried")
    else:
        con = mysql.connect(host="localhost", user="root", password="", database="student")
        cursor = con.cursor()
        cursor.execute("delete from data3 where roll_no='" + roll_no_entry.get() + "'")
        cursor.execute("commit")

        name_entry.delete(0, 'end')
        roll_no_entry.delete(0, 'end')
        email_entry.delete(0, 'end')
        val.delete(0, 'end')
        contact_no_entry.delete(0, 'end')
        dob_entry.delete(0, 'end')
        address_entry.delete(0, 'end')
        fetch()
        messagebox.showinfo("Delete Status", "Delete SucessFully")
        con.close()


# clear data to the entry widght function defined
def clearr():
    con = mysql.connect(host="localhost", user="root", password="", database="student")
    cursor = con.cursor()
    name_entry.delete(0, 'end')
    roll_no_entry.delete(0, 'end')
    email_entry.delete(0, 'end')
    val.delete(0, 'end')
    contact_no_entry.delete(0, 'end')
    dob_entry.delete(0, 'end')
    address_entry.delete(0, 'end')
    con.close()


# search student data function defined
def search_data():
    con = mysql.connect(host="localhost", user="root", password="", database="student")
    cursor = con.cursor()
    cursor.execute("select * from data3 where " + str(search_by.get()) + " LIKE '%" + str(search_text.get()) + "%'")
    rows = cursor.fetchall()
    if len(rows) != 0:
        tabel.delete(*tabel.get_children())
        for row in rows:
            tabel.insert('', END, values=row)
            con.commit()
    con.close()

root=Tk()
root.title("Student Management System")
#p1=PhotoImage(file="student.png")
#root.iconphoto(False,p1)
root.geometry("500x400")
root.geometry("1386x768")
root.config(background="darkgrey")

f1=Frame(root,bg="darkorange",borderwidth=10,relief=SUNKEN)      #frame function is used to
f1.pack(side=TOP,fill="x")
var1=Label(f1,text="STUDENT MANAGEMENT SYSTEM",fg="black",bg="orange",font=('Georgia','28','bold'))
var1.pack()

# all variables
'''notification.notify(
    title='Welcome To Student Mangement System',
    message='TSD',
    app_icon='student.ico',

    timeout=2,  #  time out  for (2) seconds
)'''

f2=Frame(root,bg="crimson",borderwidth=8,relief=SUNKEN)
f2.place(x=30,y=100,width=600,height=660)
f3=Frame(root,bg="crimson",borderwidth=8,relief=SUNKEN)
f3.place(x=650,y=100,width=850,height=660)
var2=Label(f2,text="Manage Student",fg="white",bg="crimson",font=('TimesNewRoman','20','bold'),justify="center")
var2.place(y=5,x=190)
image=Image.open("lg.jpg")
image = image.resize((90, 90), Image.ANTIALIAS)
photo=ImageTk.PhotoImage(image)
new=Label(f2,image=photo)
new.place(x=240,y=50)





name=Label(f2,text="Name ",fg="white",bg="crimson", font=('TimesNewRoman','20','bold'))
name.place(x=100,y=185)


name=StringVar()
name_entry=Entry(f2,borderwidth=4,font=('shruti','16','bold'),textvariable = name)
name_entry.place(x=270 ,y=185,width=250,height=35)

roll_no =Label(f2,text="Roll_No",fg="white",bg="crimson", font=('TimesNewRoman','20','bold'))
roll_no.place(x=100,y=230)

roll_no=StringVar()
roll_no_entry=Entry(f2,borderwidth=4,font=('shruti','16','bold'),textvariable = roll_no)
roll_no_entry.place(x=270 ,y=235,width=250,height=35)

email =Label(f2,text="Email Id ",fg="white",bg="crimson", font=('TimesNewRoman','20','bold'))
email.place(x=100,y=285)

email=StringVar()
email_entry=Entry(f2,borderwidth=4,font=('shruti','16','bold'),textvariable =email)
email_entry.place(x=270 ,y=290,width=250,height=35)


gender=Label(f2,text="Gender ",fg="white",bg="crimson",font=('TimesNewRoman','20','bold'))
gender.place(x=100,y=340)
gender=StringVar()
val=ttk.Combobox(f2,textvariable=gender,font=('shruti','16','bold'))
val['values']=('Male','Female','Other')
val.place(x=270 ,y=345,width=250,height=35)
'''entry_4=Entry(f2,borderwidth=4,font=('shruti','16','bold'))
entry_4.place(x=270 ,y=345,width=250,height=35)'''

contact_no =Label(f2,text="Contact_No",fg="white",bg="crimson",font=('TimesNewRoman','20','bold'))
contact_no.place(x=100,y=395)

contact_no=StringVar()
contact_no_entry=Entry(f2,borderwidth=4,font=('shruti','16','bold'),textvariable = contact_no)
contact_no_entry.place(x=270 ,y=400,width=250,height=35)

dob=Label(f2,text="D-O-B",fg="white",bg="crimson", font=('TimesNewRoman','20','bold'))
dob.place(x=100,y=450)

dob=StringVar()
dob_entry=Entry(f2,borderwidth=4,font=('shruti','16','bold'),textvariable = dob)
dob_entry.place(x=270 ,y=455,width=250,height=35)

address =Label(f2,text="Address ",fg="white",bg="crimson", font=('TimesNewRoman','20','bold'))
address.place(x=100,y=515)

address=StringVar()
address_entry=Entry(f2,borderwidth=4,font=('shruti','16','bold'),textvariable = address)
address_entry.place(x=270 ,y=510,width=250,height=75)

add=Button(f2,text="Add",font=('TimesNewRoman','14','bold'),borderwidth=5,fg="black",bg="red",command="add")
add.place(x=100,y=600,width=70)


update=Button(f2,text="Update",font=('TimesNewRoman','14','bold'),borderwidth=5,fg="black",bg="red",command="Update")
update.place(x=200,y=600,width=75)


delete=Button(f2,text="Delete",font=('TimesNewRoman','14','bold'),borderwidth=5,fg="black",bg="red",command="deletee")
delete.place(x=300,y=600,width=70)
#delete.bind('<Delete>',deletee)


clear=Button(f2,text="Clear",font=('TimesNewRoman', '14','bold'),borderwidth=5,fg="black",bg="red",command="clearr")
clear.place(x=400,y=600,width=70)

text=Label(f3,text="Search By",font=('TimesNewRoman','24','bold'),bg="crimson",fg="white")
text.place(x=10,y=12)

search_by=StringVar()
val1=ttk.Combobox(f3,font=('shruti','14','bold'),textvariable= search_by)
val1['values']=('name','roll_no','email')
val1.place(x=190 ,y=19,width=140,height=30)

search_text=StringVar()
stxt=Entry(f3,font=('shruti','16','bold'),textvariable=search_text)
stxt.place(x=370,y=19,width=150,height=35)

search=Button(f3,text="Search",font=('TimesNewRoman','14','bold'),borderwidth=5,bg="white",fg="black",command="search_data")
search.place(x=550,y=20,width=120,height=35)


show=Button(f3,text="Show All",font=('TimesNewRoman','14','bold'),borderwidth=5,bg="white",fg="black",command="fetch")
show.place(x=700,y=20,width=120,height=35)


# table frame for grid
f4=Frame(f3,bg="white",borderwidth=5,relief=SUNKEN)
f4.place(y=70,width=840,height=580)

scroll_x=x=Scrollbar(f4,orient=HORIZONTAL)
scroll_y=y=Scrollbar(f4,orient=VERTICAL)

tabel=ttk.Treeview(f4,columns=("Name","Roll_No","Email","Gender","Contact_No","D-O-B","Address"),xscrollcommand=scroll_x.set,yscrollcommand=scroll_y.set)
scroll_x.pack(side=BOTTOM,fill=X)
scroll_y.pack(side=RIGHT,fill=Y)

scroll_x.config(command=tabel.xview)
scroll_y.config(command=tabel.yview)

# tael heading part
tabel.heading("Name",text="Name")
tabel.heading("Roll_No",text="Roll_No")
tabel.heading("Email",text="Email")
tabel.heading("Gender",text="Gender")
tabel.heading("Contact_No",text="Contact_No")
tabel.heading("D-O-B",text="D-O-B")
tabel.heading("Address",text="Address")
tabel['show']='headings'

tabel.column("Name",width=190)
tabel.column("Roll_No",width=190)
tabel.column("Email",width=190)
tabel.column("Gender",width=190)
tabel.column("Contact_No",width=190)
tabel.column("D-O-B",width=190)
tabel.column("Address",width=190)
tabel.pack(fill=BOTH,expand=1)


# buttons part

export=Button(root,text="Export_Data",borderwidth=3,fg="white",bg="crimson",font=('TimesNewRoman','12','bold'),command="export")
export.place(x=1390,y=763)


var4=Label(root,text="Developed By Thakkar Roahan Mahendrakumar",fg="black",bg="darkgrey",bd=5,font=('TimesNewRoman','9','bold'))
var4.place(x=28,y=760)

var5=Label(root,text="The_Rt_Creation_Company",fg="black",bg="darkgrey",font=('TimesNewRoman','8','bold'))
var5.place(x=28,y=778)

root.bind("<Escape>", "exit")
root.bind('<Delete>',"deletee")



root.mainloop()