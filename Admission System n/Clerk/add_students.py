from tkinter import *
import database
from tkinter import messagebox

class Main:
    def __init__(self):
        self.tk = Tk()
        self.tk.title("Add Student")
        
        height = self.tk.winfo_screenheight()
        width = self.tk.winfo_screenwidth()
        
        print(height,width)
        y = (height-690)//2-35
        x = (width-1000)//2
        self.tk.geometry('1000x690+{}+{}'.format(str(x),str(y)))

        self.frame = Frame(self.tk,height = 690,width = 1000)
        self.can = Canvas(self.frame,height = 690,width = 1000,bg="#8AAAE5")
        self.can.pack()

        self.name = StringVar(self.tk)
        self.gender=StringVar(self.tk,"M")
        self.dob = StringVar(self.tk)
        self.email = StringVar(self.tk)
        self.contact = StringVar(self.tk)
        self.address = StringVar(self.tk)
        self.f_name = StringVar(self.tk)
        self.m_name = StringVar(self.tk)
        #self.dept = StringVar(self.tk)
        #self.course = StringVar(self.tk)
        self.last_qualification = StringVar(self.tk)
        self.comments = StringVar(self.tk)
        

        self.img = PhotoImage(file = "./images/students_12.png")
        self.can.create_image(0,0,image = self.img, anchor = NW)
        
        self.can.create_text(500,30,text = "ADD STUDENT",fill = "#FFFFFF", font = ('Comic Sans MS',28,"bold"))
        self.can.create_text(220,100,text = "Name",fill = "#FFFFFF", font = ('Comic Sans MS',24,"bold"))
        self.can.create_text(230,140,text = "Gender",fill = "#FFFFFF", font = ('Comic Sans MS',24,"bold"))

        self.can.create_text(210,180,text = "DOB",fill = "#FFFFFF", font = ('Comic Sans MS',24,"bold"))
        self.can.create_text(215,220,text = "Email",fill = "#FFFFFF", font = ('Comic Sans MS',24,"bold"))

        self.can.create_text(235,260,text = "Contact",fill = "#FFFFFF", font = ('Comic Sans MS',24,"bold"))
        self.can.create_text(235,300,text = "Address",fill = "#FFFFFF", font = ('Comic Sans MS',24,"bold"))

        self.can.create_text(290,340,text = "Father's Name",fill = "#FFFFFF", font = ('Comic Sans MS',24,"bold"))
        self.can.create_text(290,380,text = "Mother's Name",fill = "#FFFFFF", font = ('Comic Sans MS',24,"bold"))

        self.can.create_text(260,420,text = "Department",fill = "#FFFFFF", font = ('Comic Sans MS',24,"bold"))
        self.can.create_text(220,460,text = "Course",fill = "#FFFFFF", font = ('Comic Sans MS',24,"bold"))

        self.can.create_text(310,500,text = "Last Qualification",fill = "#FFFFFF", font = ('Comic Sans MS',24,"bold"))
        self.can.create_text(245,540,text = "Comments",fill = "#FFFFFF", font = ('Comic Sans MS',24,"bold"))

        self.ent_name = Entry(self.frame, textvariable=self.name, font = ('',22),fg="#FFFFFF",bg="#8AAAE5")
        self.ent_name.place(x=480,y=80)

        self.ent_gender = Radiobutton(self.frame, value = "M",text="Male",variable=self.gender,
                                      font = ('Comic Sans MS',12),fg="black",bg="#8AAAE5",activeforeground="red")
        self.ent_gender.place(x=480,y=120)
        self.ent_gender = Radiobutton(self.frame, value = "F",text="Female",variable=self.gender,
                                      font = ('Comic Sans MS',12),fg="black",bg="#8AAAE5")
        self.ent_gender.place(x=560,y=120)


        self.ent_dob = Entry(self.frame, textvariable=self.dob, font = ('',22),fg="#FFFFFF",bg="#8AAAE5")
        self.ent_dob.place(x=480,y=160)

        self.ent_email = Entry(self.frame, textvariable=self.email,font = ('',22),fg="#FFFFFF",bg="#8AAAE5")
        self.ent_email.place(x=480,y=200)

        self.ent_contact = Entry(self.frame, textvariable=self.contact, font = ('',22),fg="#FFFFFF",bg="#8AAAE5")
        self.ent_contact.place(x=480,y=240)

        self.ent_address = Entry(self.frame, textvariable=self.address, font = ('',22),fg="#FFFFFF",bg="#8AAAE5")
        self.ent_address.place(x=480,y=280)

        self.ent_fname = Entry(self.frame, textvariable=self.f_name, font = ('',22),fg="#FFFFFF",bg="#8AAAE5")
        self.ent_fname.place(x=480,y=320)

        self.ent_mname = Entry(self.frame, textvariable=self.m_name, font = ('',22),fg="#FFFFFF",bg="#8AAAE5")
        self.ent_mname.place(x=480,y=360)

        #self.can.create_text(480,400,fill="#FFFFFF",font=('Comic Sans MS',30))

        
        # Department Dropdown
        self.dept_option =[]
        self.dept = database.Manage()
        self.all_dept= self.dept.view_d()
        for i in self.all_dept:
            self.dept_option.append(i[1])
        
        
        self.dept = StringVar(self.tk)
        self.dept_1 = OptionMenu(self.can, self.dept, *tuple(self.dept_option))
        self.dept_1.place(x=480,y=400)
        self.dept_1.config(font=('Comic Sans MS',20),fg="#FFFFFF",bg="#8AAAE5",width=17)

        
        # Course Dropdown
        self.course_option =[]
        self.course = database.Manage()
        self.all_course= self.course.view_course()
        for i in self.all_course:
            self.course_option.append(i[2])
            
        self.course = StringVar(self.tk)
        
        self.course_1 = OptionMenu(self.can, self.course, *tuple(self.course_option))
        self.course_1.place(x=480,y=440)
        self.course_1.config(font=('Comic Sans MS',20),fg="#FFFFFF",bg="#8AAAE5",width=17)
        
        
        self.ent_last_qual = Checkbutton(self.frame,text="10th",variable=self.last_qualification,
                                      font = ('Comic Sans MS',12),fg="#FFFFFF",bg="#8AAAE5")
        self.ent_last_qual.place(x=480,y=500)
        self.ent_last_qual = Checkbutton(self.frame,text="10+2",variable=self.last_qualification,
                                      font = ('Comic Sans MS',12),fg="#FFFFFF",bg="#8AAAE5")
        self.ent_last_qual.place(x=560,y=500)
        self.ent_last_qual = Checkbutton(self.frame,text="Graduate",variable=self.last_qualification,
                                      font = ('Comic Sans MS',12),fg="#FFFFFF",bg="#8AAAE5")
        self.ent_last_qual.place(x=600,y=500)
        self.ent_last_qual = Checkbutton(self.frame,text="Post Graduate",variable=self.last_qualification,
                                      font = ('Comic Sans MS',12),fg="#FFFFFF",bg="#8AAAE5")
        self.ent_last_qual.place(x=640,y=500)
        

        self.ent_comments = Entry(self.frame, textvariable=self.comments, font = ('',22),fg="#FFFFFF",bg="#8AAAE5")
        self.ent_comments.place(x=480,y=540)

        self.btn = Button(self.frame,text = "SUBMIT", font = ('Comic Sans MS',24,"bold"),
                          fg="#FFFFFF",bg="#8AAAE5", command=self.add_data)
        self.btn.place(x=430,y=580)


        self.frame.place(x=0,y=0)
      
        self.tk.resizable(height = False, width = False)
        self.tk.mainloop()


    def add_data(self):
        tupl = [self.name.get(),
                self.gender.get(),
                self.dob.get(),
                self.email.get(),
                self.contact.get(),
                self.address.get(),
                self.f_name.get(),
                self.m_name.get(),
                self.dept.get(),
                self.course.get(),
                self.last_qualification.get(),
                self.comments.get(),]

        if( self.name.get() != "" and
            self.gender.get() != "" and
            self.dob.get() != "" and
            self.email.get() != "" and
            self.contact.get() != "" and
            self.address.get() != "" and
            self.f_name.get() != "" and
            self.m_name.get() != "" and
            self.dept.get() != "" and
            self.course.get() != "" and
            self.last_qualification.get() != "" and
            self.comments.get() != "" ):

            obj = database.database()
            obj.add_student(tupl)

            messagebox.showinfo("Success","Student data has been created")

            self.tk.destroy()
            

            

        else:
            messagebox.showinfo("Error","Please fill all the fields")

d = Main()

