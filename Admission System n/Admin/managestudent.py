from tkinter import *
import database
from tkinter.ttk import Treeview
from tkinter import ttk


class MainWindow:
    def __init__(self):
        
        self.tk=Tk()
        height = self.tk.winfo_screenheight()
        width = self.tk.winfo_screenwidth()
        
        y = (height - 600)//2
        x = (width - 600)//2
        
        self.tk.geometry('600x600+'+str(x)+'+'+str(y)+'')
        self.fr=Frame(self.tk,width='600',height='600',bg="#063852")
        self.label=Label(self.fr,text="Manage Admissions",font=('ALGERIAN',40),bg="#063852",fg="white")
        self.label.place(x=20,y=0)
        
        self.can=Canvas(self.fr,width=600,height=200)
        self.can.place(x=0,y=80)
        self.img=PhotoImage(file='./images/image10p.gif')
        self.can.create_image(0,0,image=self.img,anchor=NW)
          
        self.grid=Frame(self.fr,height=768,width=600,bg="#063852")
        self.table=Treeview(self.grid,column=('#0','#1','#2','#3','#4'))
        style=ttk.Style()
        style.theme_use("alt")
        ttk.Style().configure("Treeview.heading",font=('ALGERIAN',20))
        self.table.heading('#0',text="id")
        self.table.column('#0',width=40)
        self.table.heading('#1',text="Name")
        self.table.column('#1',width=70)
        self.table.heading('#2',text="Contact")
        self.table.column('#2',width=70)
        self.table.heading('#3',text="Course")
        self.table.column('#3',width=70)
        self.table.heading('#4',text="Email")
        self.table.column('#4',width=70)
        self.table.heading('#5',text="Details")
        self.table.column('#5',width=70)
        x=database.Manage()
        y=x.view_s()
        print(y)
        for i in y:
            self.table.insert('','end',text=i[0],values=(i[1],i[2],i[3],i[4]))
        
       
        self.table.place(x=0,y=0)
        
        self.fr.place(x=0,y=0)
        self.grid.place(x=90,y=320)
        self.btn=Button(self.tk,text="Full Details",font=('ALGERIAN',15))
        self.btn.place(x=440,y=550)
        self.tk.resizable(height=False,width=False)
        self.tk.mainloop()
        
      
        

d=MainWindow()
