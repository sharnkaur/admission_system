from tkinter import *

import database
from tkinter.ttk import Treeview
from tkinter import ttk

class MainWindow:
    def __init__(self):

        
        self.tk=Toplevel()
        height = self.tk.winfo_screenheight()
        width = self.tk.winfo_screenwidth()
        
        y = (height - 600)//2
        x = (width - 700)//2
        
        self.tk.geometry('700x600+'+str(x)+'+'+str(y)+'')

        
      
        
        self.fr=Frame(self.tk,width='700',height='600',bg="#363237")
        self.label=Label(self.tk,text="Manage Clerk",font=('ALGERIAN',40),bg="#363237",fg='white')
        self.label.place(x=130,y=0)
        
        self.can=Canvas(self.tk,width=195,height=200,bg="#363237")
        self.can.place(x=250,y=90)
        self.img=PhotoImage(file='./images/icon12p.gif')
        self.can.create_image(0,0,image=self.img,anchor=NW)
        
        self.frame=Frame(self.tk,height=600,width=500,bg="#363237")
        self.table=Treeview(self.frame,column=('#0','#1','#2','#3','#4','#5','#6'))
        style=ttk.Style()
        style.theme_use("alt")
        ttk.Style().configure("Treeview.heading",font=('ALGERIAN',20))
        self.table.heading('#0',text="Sno.")
        self.table.column('#0',width=30)
        self.table.heading('#1',text="Name")
        self.table.column('#1',width=60)
        self.table.heading('#2',text="Gender")
        self.table.column('#2',width=60)
        self.table.heading('#3',text="Email_id")
        self.table.column('#3',width=110)
        self.table.heading('#4',text="Contact")
        self.table.column('#4',width=60)
        self.table.heading('#5',text="Address")
        self.table.column('#5',width=90)
        self.table.heading('#6',text="Edit")
        self.table.column('#6',width=40)
        self.table.heading('#7',text="Delete")
        self.table.column('#7',width=60)
        x=database.Manage()
        y=x.view_a()
        print(y)
        for i in y:
            self.table.insert('','end',text=i[0],values=(i[1],i[2],i[3],i[4],i[5],"Edit","Delete"))
        self.table.place(x=0,y=0)
        self.frame.place(x=100,y=310)
        self.tk.resizable(height=False,width=False)
        self.fr.place(x=0,y=0)

        self.btn=Button(self.tk,text="Edit",font=('ALGERIAN',15))
        self.btn.place(x=450,y=550)

        self.btn=Button(self.tk,text="Delete",font=('ALGERIAN',15))
        self.btn.place(x=520,y=550)
        self.table.bind("<Double-Button-1>",self.trigger)

        self.tk.mainloop()

    def trigger(self,e):
        print(e)
        d = self.table.focus()
        x = (self.table.item(d))
        col = self.table.identify_column(e.x)
        if col=="#6":
            self.tk.destroy()
            import edit_clerk
            a=edit_clerk.Main(x["text"])
            
            
        #elif col == "#7":
            
        
       
  

if __name__=="__main__":
    
    d=MainWindow()
