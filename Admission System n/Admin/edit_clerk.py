from tkinter import *
import database
import manageclerk
class Main:
    def __init__(self,id_):
        self.id = id_

        obj = database.Manage()
        clerk = obj.getclerkbyid(id_)
        print(clerk)
        
        self.tk = Toplevel()
        self.tk.title("Edit Clerk")
        
        height = self.tk.winfo_screenheight()
        width = self.tk.winfo_screenwidth()
        
        print(height,width)
        y = (height-600)//2-30
        x = (width-800)//2
        self.tk.geometry('800x600+{}+{}'.format(str(x),str(y)))

        self.frame = Frame(self.tk,height = 600,width = 800)
        self.can = Canvas(self.frame,height = 600,width = 800,bg="#293250")
        self.can.pack()
        

        self.img = PhotoImage(file = "./images/book_1.png")
        self.can.create_image(0,0,image = self.img, anchor = NW)
        
        self.can.create_text(400,80,text = "EDIT CLERK",fill = "#F4A950", font = ('Comic Sans MS',28,"bold"))
        self.can.create_text(175,170,text = "Name",fill = "#F4A950", font = ('Comic Sans MS',24,"bold"))
        self.can.create_text(185,220,text = "Gender",fill = "#F4A950", font = ('Comic Sans MS',24,"bold"))

        self.can.create_text(170,270,text = "Email",fill = "#F4A950", font = ('Comic Sans MS',24,"bold"))
        self.can.create_text(200,320,text = "Password",fill = "#F4A950", font = ('Comic Sans MS',24,"bold"))

        self.can.create_text(190,370,text = "Contact",fill = "#F4A950", font = ('Comic Sans MS',24,"bold"))
        self.can.create_text(190,420,text = "Address",fill = "#F4A950", font = ('Comic Sans MS',24,"bold"))

        self.name = StringVar(self.tk) 
        self.gender = StringVar(self.tk)
        self.email = StringVar(self.tk)
        self.password = StringVar(self.tk)
        self.contact = StringVar(self.tk)
        self.address = StringVar(self.tk)
        
        
        self.name.set(clerk[1])
        
        self.gender.set(clerk[2])
        self.email.set(clerk[3])
        self.password.set(clerk[4])
        self.contact.set(clerk[5])
        self.address.set(clerk[6])
        
        self.ent_name = Entry(self.frame, font = ('',22),fg="#F4A950",bg="#161B21",textvariable=self.name)
        self.ent_name.place(x=330,y=150)

        self.ent_gender = Radiobutton(self.frame, value = "M",text="Male",variable=self.gender,
                                      font = ('Comic Sans MS',12),fg="#F4A950",bg="#161B21")
        self.ent_gender.place(x=330,y=200)
        self.ent_gender = Radiobutton(self.frame, value = "F",text="Female",variable=self.gender,
                                      font = ('Comic Sans MS',12),fg="#F4A950",bg="#161B21")
        self.ent_gender.place(x=410,y=200)


        self.ent_email = Entry(self.frame, font = ('',22),fg="#F4A950",bg="#161B21",textvariable=self.email)
        self.ent_email.place(x=330,y=250)

        self.ent_password = Entry(self.frame,show = "*",font = ('',22),fg="#F4A950",bg="#161B21",textvariable=self.password)
        self.ent_password.place(x=330,y=300)

        self.ent_contact = Entry(self.frame, font = ('',22),fg="#F4A950",bg="#161B21",textvariable=self.contact)
        self.ent_contact.place(x=330,y=350)

        self.ent_address = Entry(self.frame, font = ('',22),fg="#F4A950",bg="#161B21",textvariable=self.address)
        self.ent_address.place(x=330,y=400)


        self.btn = Button(self.frame,text = "UPDATE", font = ('Comic Sans MS',22,"bold"),fg="#F4A950",bg="#161B21",command=self.update)
        self.btn.place(x=330,y=460)


        self.frame.place(x=0,y=0)
      
        self.tk.resizable(height = False, width = False)
        self.tk.mainloop()

    def update(self):
        lis = [self.name.get(),
               self.gender.get(),
               self.email.get(),
               self.password.get(),
               self.contact.get(),
               self.address.get(),
               self.id]
        obj= database.Manage()
        obj.updateclerk(lis)
        self.tk.destroy()
        obj = manageclerk.MainWindow()


