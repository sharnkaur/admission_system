from tkinter import *
import database
import managecourse
class Main:
    def __init__(self,id_):
        self.id = id_

        obj = database.Manage()
        course = obj.getcoursebyid(id_)
        print(course)

        
    
        self.tk=Toplevel()
        self.tk.title("Edit Course")
        height = self.tk.winfo_screenheight()
        width = self.tk.winfo_screenwidth()
        
        y = (height - 500)//2-20
        x = (width - 800)//2
        
        self.tk.geometry('800x500+'+str(x)+'+'+str(y)+'')
        
        self.can=Canvas(self.tk,width=800,height=500)
        self.can.place(x=0,y=0)
        self.img=PhotoImage(file='./images/image11pppp.gif')
        self.can.create_image(0,0,image=self.img,anchor=NW)
        
        self.can.create_text(400,30,text="Edit Courses",fill="#FA6775",font=('ALGERIAN',30))
        self.can.create_text(180,100,text="Department",fill="#FA6775",font=('ALGERIAN',30))

         
        # Dept Dropdown
        self.dept_option =[]
        self.dept = database.Manage()
        self.all_dept= self.dept.view_d()
        for i in self.all_dept:
            self.dept_option.append(i[1])
        
        
        self.dept = StringVar(self.tk)
        self.dept_1 = OptionMenu(self.can, self.dept, *tuple(self.dept_option))
        self.dept_1.place(x=320,y=70)
        self.dept_1.config(font=('Comic Sans MS',20),fg="#FFFFFF",bg="#8AAAE5",width=17,textvariable=self.dept)
        
        self.course = StringVar(self.tk)
        self.can.create_text(140,175,text="Courses",fill="#FA6775",font=('ALGERIAN',30))
        self.course=Entry(self.can,font=('ALGERIAN',20),textvariable=self.course)
        self.course.place(x=320,y=155)
        

        self.btn=Button(self.can,text="SUBMIT QUERY",font=("ALGERIAN",20),fg="#FA6775",command=self.update)
        self.btn.place(x=290,y=270)
        self.dept.set(course[1])
        self.course.set(course[2])

        self.tk.resizable(height=False,width=False)
        self.tk.mainloop()
             
    def update(self):
        lis = [self.dept.get(),
               self.course.get(),
               
               self.id]
        obj= database.Manage()
        obj.updatecourse(lis)
        self.tk.destroy()
        obj = managecourse.MainWindow()



