from tkinter import *
import database
from tkinter import messagebox

class Main:
    def __init__(self):
        self.tk = Tk()
        self.tk.title("Add Clerk")
        
        height = self.tk.winfo_screenheight()
        width = self.tk.winfo_screenwidth()
        
        print(height,width)
        y = (height-600)//2-20
        x = (width-800)//2
        self.tk.geometry('800x600+{}+{}'.format(str(x),str(y)))

        self.frame = Frame(self.tk,height = 600,width = 800)
        self.can = Canvas(self.frame,height = 600,width = 800)
        self.can.pack()

        self.name = StringVar(self.tk)
        self.gender = StringVar(self.tk,"M")
        self.email = StringVar(self.tk)
        self.password = StringVar(self.tk)
        self.contact = StringVar(self.tk)
        self.address = StringVar(self.tk)
               

        self.img = PhotoImage(file = "./images/clerk_123.png")
        self.can.create_image(0,0,image = self.img, anchor = NW)
        
        self.can.create_text(400,80,text = "ADD CLERK",fill = "#CFEED1", font = ('Comic Sans MS',28,"bold"))
        self.can.create_text(180,170,text = "Name",fill = "#CFEED1", font = ('Comic Sans MS',24,"bold"))
        self.can.create_text(190,220,text = "Gender",fill = "#CFEED1", font = ('Comic Sans MS',24,"bold"))

        self.can.create_text(180,270,text = "Email",fill = "#CFEED1", font = ('Comic Sans MS',24,"bold"))
        self.can.create_text(210,320,text = "Password",fill = "#CFEED1", font = ('Comic Sans MS',24,"bold"))

        self.can.create_text(195,370,text = "Contact",fill = "#CFEED1", font = ('Comic Sans MS',24,"bold"))
        self.can.create_text(195,415,text = "Address",fill = "#CFEED1", font = ('Comic Sans MS',24,"bold"))

        self.ent_name = Entry(self.frame, textvariable=self.name, font = ('',24),fg="#CFEED1",bg="#048D79")
        self.ent_name.place(x=300,y=150)

        
        self.ent_gender = Radiobutton(self.frame, value = "M",text="Male",
                                      variable=self.gender, font = ('Comic Sans MS',14,"bold"),fg="#CFEED1",bg="#048D79")
        self.ent_gender.place(x=300,y=200)
        self.ent_gender = Radiobutton(self.frame, value = "F",text="Female",
                                      variable=self.gender, font = ('Comic Sans MS',14,"bold"),fg="#CFEED1",bg="#048D79")
        self.ent_gender.place(x=380,y=200)

        self.ent_email = Entry(self.frame, font = ('',24),textvariable=self.email, fg="#CFEED1",bg="#048D79")
        self.ent_email.place(x=300,y=250)

        self.ent_password = Entry(self.frame,show = "*",textvariable=self.password,
                                            font = ('',24),fg="#CFEED1",bg="#048D79")
        self.ent_password.place(x=300,y=300)

        self.ent_contact = Entry(self.frame, textvariable=self.contact,
                                              font = ('',24),fg="#CFEED1",bg="#048D79")
        self.ent_contact.place(x=300,y=350)

        self.ent_address = Entry(self.frame, textvariable=self.address, font = ('',24),fg="#CFEED1",bg="#048D79")
        self.ent_address.place(x=300,y=400)


        self.btn = Button(self.frame,text = "SUBMIT", font = ('Comic Sans MS',24,"bold"),fg="#CFEED1",
                                    bg="#048D79", command=self.add_data)
        self.btn.place(x=320,y=460)


        self.frame.place(x=0,y=0)
      
        self.tk.resizable(height = False, width = False)
        self.tk.mainloop()

    def add_data(self):
        tupl = (self.name.get(),
                self.gender.get(),
                self.email.get(),
                self.password.get(),
                self.contact.get(),
                self.address.get(),)
        
        if( self.name.get() != "" and
            self.gender.get() != "" and
            self.email.get() != "" and
            self.password.get() != "" and
            self.contact.get() != "" and
            self.address.get() != "" ):
            
            obj = database.database()
            obj.add_clerk(tupl)
            messagebox.showinfo("Success","Clerk data has been created")

            self.tk.destroy()

        else:
            messagebox.showinfo("Error","Please fill all the fields")
                

d = Main()
