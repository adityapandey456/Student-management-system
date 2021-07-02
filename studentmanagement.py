from tkinter import *
from tkinter import Toplevel,messagebox,filedialog
from tkinter.ttk import Treeview
from tkinter import ttk
import pandas
import pymysql
import time
root = Tk()
root.title('Student Management System')
root.config(bg='gold2')
root.geometry('1174x700+200+50')
root.iconbitmap('mana.ico')
root.resizable(False,False)
############################################################################################################  Frames
##---------------------------------------------------------------------------- dataentry frame

DataEntryFrame = Frame(root,bg='gold2',relief=GROOVE,borderwidth=5)
DataEntryFrame.place(x=10,y=80,width=500,height=600)
frontlabel = Label(DataEntryFrame,text='--------------Welcome--------------',width=30,font=('arial',22,'italic bold'),bg='gold2')
frontlabel.pack(side=TOP,expand=True)
addbtn = Button(DataEntryFrame,text='1. Add Student',width=25,font=('chiller',20,'bold'),bd=6,bg='skyblue3',activebackground='blue',relief=RIDGE,
                activeforeground='white',command=addstudent)
addbtn.pack(side=TOP,expand=True)

searchbtn = Button(DataEntryFrame,text='2. Search Student',width=25,font=('chiller',20,'bold'),bd=6,bg='skyblue3',activebackground='blue',relief=RIDGE,
                activeforeground='white',command=searchstudent)
searchbtn.pack(side=TOP,expand=True)

deletebtn = Button(DataEntryFrame,text='3. Delete Student',width=25,font=('chiller',20,'bold'),bd=6,bg='skyblue3',activebackground='blue',relief=RIDGE,
                activeforeground='white',command=deletestudent)
deletebtn.pack(side=TOP,expand=True)

updatebtn = Button(DataEntryFrame,text='4. Update Student',width=25,font=('chiller',20,'bold'),bd=6,bg='skyblue3',activebackground='blue',relief=RIDGE,
                activeforeground='white',command=updatestudent)
updatebtn.pack(side=TOP,expand=True)

showallbtn = Button(DataEntryFrame,text='5. Show All',width=25,font=('chiller',20,'bold'),bd=6,bg='skyblue3',activebackground='blue',relief=RIDGE,
                activeforeground='white',command=showstudent)
showallbtn.pack(side=TOP,expand=True)

exportbtn = Button(DataEntryFrame,text='6. Export data',width=25,font=('chiller',20,'bold'),bd=6,bg='skyblue3',activebackground='blue',relief=RIDGE,
                activeforeground='white',command=exportstudent)
exportbtn.pack(side=TOP,expand=True)

exitbtn = Button(DataEntryFrame,text='7.  Exit',width=25,font=('chiller',20,'bold'),bd=6,bg='skyblue3',activebackground='blue',relief=RIDGE,
                activeforeground='white',command=exitstudent)
exitbtn.pack(side=TOP,expand=True)

##-----------------------------------------------------------Show data frame
ShowDataFrame = Frame(root,bg='gold2',relief=GROOVE,borderwidth=5)
ShowDataFrame.place(x=550,y=80,width=620,height=600)

##-------------------------------------------------  Showdataframe
style = ttk.Style()
style.configure('Treeview.Heading',font=('chiller',20,'bold'),foreground='blue')
style.configure('Treeview',font=('times',15,'bold'),background='cyan',foreground='black')
scroll_x = Scrollbar(ShowDataFrame,orient=HORIZONTAL)
scroll_y = Scrollbar(ShowDataFrame,orient=VERTICAL)
studenmttable = Treeview(ShowDataFrame,columns=('Id','Name','Mobile No','Email','Address','Gender','D.O.B','Added Date','Added Time'),
                         yscrollcommand=scroll_y.set,xscrollcommand=scroll_x.set)
scroll_x.pack(side=BOTTOM,fill=X)
scroll_y.pack(side=RIGHT,fill=Y)
scroll_x.config(command=studenmttable.xview)
scroll_y.config(command=studenmttable.yview)
studenmttable.heading('Id',text='Id')
studenmttable.heading('Name',text='Name')
studenmttable.heading('Mobile No',text='Mobile No')
studenmttable.heading('Email',text='Email')
studenmttable.heading('Address',text='Address')
studenmttable.heading('Gender',text='Gender')
studenmttable.heading('D.O.B',text='D.O.B')
studenmttable.heading('Added Date',text='Added Date')
studenmttable.heading('Added Time',text='Added Time')
studenmttable['show'] = 'headings'
studenmttable.column('Id',width=100)
studenmttable.column('Name',width=200)
studenmttable.column('Mobile No',width=200)
studenmttable.column('Email',width=300)
studenmttable.column('Address',width=200)
studenmttable.column('Gender',width=100)
studenmttable.column('D.O.B',width=150)
studenmttable.column('Added Date',width=150)
studenmttable.column('Added Time',width=150)
studenmttable.pack(fill=BOTH,expand=1)

################################################################################################################  Slider
ss = 'Welcome To Student Management System'
count = 0
text = ''
##################################
SliderLabel = Label(root,text=ss,font=('chiller',30,'italic bold'),relief=RIDGE,borderwidth=4,width=35,bg='cyan')
SliderLabel.place(x=260,y=0)
IntroLabelTick()
IntroLabelColorTick()
############################################################################################################### clock
clock = Label(root,font=('times',14,'bold'),relief=RIDGE,borderwidth=4,bg='lawn green')
clock.place(x=0,y=0)
tick()
################################################################################################################## ConnectDatabaseButton
connectbutton = Button(root,text='Connect To Database',width=23,font=('chiller',19,'italic bold'),relief=RIDGE,borderwidth=4,bg='green2',
                       activebackground='blue',activeforeground='white',command=Connectdb)
connectbutton.place(x=930,y=0)
root.mainloop()