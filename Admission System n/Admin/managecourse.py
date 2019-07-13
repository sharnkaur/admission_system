from tkinter import *
from tkinter.ttk import Treeview
from tkinter import ttk
import database


class MainWindow:
    def __init__(self):
        
        self.tk=Toplevel()
        height = self.tk.winfo_screenheight()
        width = self.tk.winfo_screenwidth()
        
        y = (height - 600)//2-20
        x = (width - 600)//2
        
        self.tk.geometry('600x600+'+str(x)+'+'+str(y)+'')
        self.fr=Frame(self.tk,width='600',height='600',bg="#336B87")
        
        self.label=Label(self.fr,text="Manage Course",font=('ALGERIAN',40),bg="#336B87")
        self.label.place(x=110,y=0)


        self.can=Canvas(self.fr,width='300',height='200',bg="#336B87")
        self.can.place(x=160,y=80)
        self.img=PhotoImage(file='./images/image33p.gif')
        self.can.create_image(0,0,image=self.img,anchor=NW)
    
        self.table=Treeview(self.fr,column=('#0','#1','#2','#3'))
        style=ttk.Style()
        style.theme_use("alt")
        ttk.Style().configure("Treeview.heading",font=('ALGERIAN',20,"bold"))
        self.table.heading('#0',text="Sno.")
        self.table.column('#0',width=70)
        self.table.heading('#1',text="Department")
        self.table.column('#1',width=120)
        self.table.heading('#2',text="Course")
        self.table.column('#2',width=120)
        self.table.heading('#3',text="Edit")
        self.table.column('#3',width=70)
        self.table.heading('#4',text="Delete")
        self.table.column('#4',width=70)
        
        x=database.Manage()
        y=x.view_course()
        print(y)
        for i in y:
            self.table.insert('','end',text=i[0],values=(i[2],i[4],"Edit","Delete"))
        

        self.table.place(x=70,y=320)
       
        self.tk.resizable(height=False,width=False)
        
       
        self.btn=Button(self.tk,text="Edit",font=('ALGERIAN',15))
        self.btn.place(x=440,y=550)

        self.btn=Button(self.tk,text="Delete",font=('ALGERIAN',15))
        self.btn.place(x=510,y=550)
        self.fr.place(x=0,y=0)
        self.table.bind("<Double-Button-1>",self.trigger)
        self.tk.mainloop()

    def trigger(self,e):
        
        
        print(e)
        d = self.table.focus()
        x = (self.table.item(d))
        col = self.table.identify_column(e.x)
        if col=="#3":
            self.tk.destroy()
            import editcourse
            a=editcourse.Main(x["text"])
            
            
        #elif col == "#7":
            
        
       
  
if __name__=="__main__":
    d=MainWindow()

