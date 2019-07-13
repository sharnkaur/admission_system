from tkinter import *
import database
from tkinter import messagebox

class Main:
    def __init__(self):
        self.tk=Tk()
        height = self.tk.winfo_screenheight()
        width = self.tk.winfo_screenwidth()
        
        y = (height - 500)//2-20
        x = (width - 800)//2
        
        self.tk.geometry('800x500+'+str(x)+'+'+str(y)+'')
        
        
        self.fr = Frame(self.tk,width='800',height='500',bg="black")

        self.course = StringVar(self.tk)
        

    
        self.label=Label(self.fr,text="Add Courses",font=('ALGERIAN',30),bg="black",fg="red")
        self.label.place(x=10,y=0)
        
        self.can=Canvas(self.fr,width=800,height=500)
        self.can.place(x=0,y=50)

        self.img=PhotoImage(file='./images/image9p.gif')
        self.can.create_image(0,0,image=self.img,anchor=NW)
        
        
        self.can.create_text(180,90,text="Department",fill="red",font=('ALGERIAN',30))


        # Dept Dropdown
        self.dept_option =[]
        self.dept = database.Manage()
        self.all_dept= self.dept.view_d()
        for i in self.all_dept:
            self.dept_option.append(i[1])
        
        
        self.dept = StringVar(self.tk)
        self.dept_1 = OptionMenu(self.can, self.dept, *tuple(self.dept_option))
        self.dept_1.place(x=320,y=70)
        self.dept_1.config(font=('Comic Sans MS',20),fg="#FFFFFF",bg="#8AAAE5",width=17)
        
                

        self.can.create_text(140,170,text="Courses",fill="red",font=('ALGERIAN',30))

        self.course=Entry(self.can,textvariable = self.course,font=('ALGERIAN',20))
        self.course.place(x=320,y=150)

        self.btn=Button(self.can,text="SUBMIT QUERY",font=("ALGERIAN",20),fg="red",command=self.add_course)
        self.btn.place(x=290,y=250)

        self.fr.place(x=0,y=0)
        self.tk.resizable(height=False,width=False)
        
        self.tk.mainloop()

    def add_course(self):
        
        
        tupl =[self.dept.get(),self.course.get(),]
        
        if (self.dept.get()!="" and
            self.course.get()!=""):
            
            obj = database.database()
            obj.add_course(tupl)
            

            messagebox.showinfo("Success","Course data has been created")

            self.tk.destroy()
            

        else:
            messagebox.showinfo("Error","Please fill all the fields")
            
       
d=Main()
