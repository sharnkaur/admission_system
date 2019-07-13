
from tkinter import *
import database
from tkinter.ttk import Treeview
from tkinter import ttk
'''
import mysql.connector
mydb=mysql.connector.connect(
    user="root",
    passwd="",
    host="localhost",
    database="first_database")

cursor=mydb.cursor()
cursor.execute("select * from second")
result=cursor.fetchall()
print(result)
'''

class MainWindow:
    def __init__(self):
        
        self.tk=Tk()
        height = self.tk.winfo_screenheight()
        width = self.tk.winfo_screenwidth()
        
        y = (height - 600)//2-20
        x = (width - 600)//2
        
        self.tk.geometry('600x600+'+str(x)+'+'+str(y)+'')
        self.fr=Frame(self.tk,width='600',height='600',bg="#021C1E")
        self.label=Label(self.fr,text="Manage Department",font=('ALGERIAN',40),bg="#021C1E",fg="white")
        self.label.place(x=20,y=0)
        

        self.can=Canvas(self.fr,width=200,height=200,bg="#021C1E")
        self.can.place(x=200,y=100)
        self.img=PhotoImage(file='./images/icon11p.gif')
        self.can.create_image(0,0,image=self.img,anchor=NW)
        
    
        self.frame=Frame(self.fr,height=400,width=500,bg="#021C1E")
        self.table=Treeview(self.frame,column=('#0','#1','#2'))
        style=ttk.Style()
        style.theme_use("alt")
        ttk.Style().configure("Treeview.heading",font=('ALGERIAN',20))
        self.table.heading('#0',text="Sno.")
        self.table.column('#0',width=50)
        self.table.heading('#1',text="Name")
        self.table.column('#1',width=80)
        self.table.heading('#2',text="Edit")
        self.table.column('#2',width=80)
        self.table.heading('#3',text="Delete")
        self.table.column('#3',width=80)
        x=database.Manage()
        y=x.view_d()
        print(y)
        for i in y:
            self.table.insert('','end',text=i[0],values=(i[1],"Edit","Delete"))


        self.table.place(x=0,y=0)
        self.frame.place(x=165,y=320)
        self.tk.resizable(height=False,width=False)
        self.fr.place(x=0,y=0)
        

        self.btn=Button(self.tk,text="Edit",font=('ALGERIAN',15))
        self.btn.place(x=440,y=550)

        self.btn=Button(self.tk,text="Delete",font=('ALGERIAN',15))
        self.btn.place(x=510,y=550)
        self.tk.mainloop()
        
d=MainWindow()
