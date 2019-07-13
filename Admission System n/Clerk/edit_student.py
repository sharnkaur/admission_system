from tkinter import *

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
        self.gender=StringVar(self.tk)

        self.img = PhotoImage(file = "./images/students_12.png")
        self.can.create_image(0,0,image = self.img, anchor = NW)
        
        self.can.create_text(500,30,text = "EDIT STUDENT",fill = "#FFFFFF", font = ('Comic Sans MS',28,"bold"))
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

        self.ent_name = Entry(self.frame, font = ('',22),fg="#FFFFFF",bg="#8AAAE5")
        self.ent_name.place(x=480,y=80)

        self.ent_gender = Radiobutton(self.frame, value = "M",text="Male",variable=self.gender,
                                      font = ('Comic Sans MS',12),fg="#FFFFFF",bg="#8AAAE5")
        self.ent_gender.place(x=480,y=120)
        self.ent_gender = Radiobutton(self.frame, value = "F",text="Female",variable=self.gender,
                                      font = ('Comic Sans MS',12),fg="#FFFFFF",bg="#8AAAE5")
        self.ent_gender.place(x=560,y=120)


        self.ent_dob = Entry(self.frame, font = ('',22),fg="#FFFFFF",bg="#8AAAE5")
        self.ent_dob.place(x=480,y=160)

        self.ent_email = Entry(self.frame,show = "*",font = ('',22),fg="#FFFFFF",bg="#8AAAE5")
        self.ent_email.place(x=480,y=200)

        self.ent_contact = Entry(self.frame, font = ('',22),fg="#FFFFFF",bg="#8AAAE5")
        self.ent_contact.place(x=480,y=240)

        self.ent_address = Entry(self.frame, font = ('',22),fg="#FFFFFF",bg="#8AAAE5")
        self.ent_address.place(x=480,y=280)

        self.ent_fname = Entry(self.frame, font = ('',22),fg="#FFFFFF",bg="#8AAAE5")
        self.ent_fname.place(x=480,y=320)

        self.ent_mname = Entry(self.frame, font = ('',22),fg="#FFFFFF",bg="#8AAAE5")
        self.ent_mname.place(x=480,y=360)

        self.ent_dept = Entry(self.frame, font = ('',22),fg="#FFFFFF",bg="#8AAAE5")
        self.ent_dept.place(x=480,y=400)

        self.ent_course = Entry(self.frame, font = ('',22),fg="#FFFFFF",bg="#8AAAE5")
        self.ent_course.place(x=480,y=440)

        self.ent_last_qual = Entry(self.frame, font = ('',22),fg="#FFFFFF",bg="#8AAAE5")
        self.ent_last_qual.place(x=480,y=480)

        self.ent_comments = Entry(self.frame, font = ('',22),fg="#FFFFFF",bg="#8AAAE5")
        self.ent_comments.place(x=480,y=520)

        self.btn = Button(self.frame,text = "UPDATE", font = ('Comic Sans MS',24,"bold"),fg="#FFFFFF",bg="#8AAAE5")
        self.btn.place(x=430,y=580)


        self.frame.place(x=0,y=0)
      
        self.tk.resizable(height = False, width = False)
        self.tk.mainloop()

d = Main()

