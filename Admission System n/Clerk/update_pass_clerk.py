from tkinter import *
import database
from tkinter import messagebox

class Main:
    def __init__(self):
        self.tk = Tk()
        self.tk.title("Update Password")

        height = self.tk.winfo_screenheight()
        width = self.tk.winfo_screenwidth()

        y = (height-600)//2-20
        x = (width-800)//2
        self.tk.geometry('800x600+{}+{}'.format(str(x),str(y)))
    
        self.frame = Frame(self.tk,height = 600,width = 800)
        self.can = Canvas(self.frame,height = 600,width = 800,bg="#161B21")
        self.can.pack()
        
        self.oldpassword = StringVar(self.tk)
        self.newpassword = StringVar(self.tk)

        self.img = PhotoImage(file="./images/office_21.png")
        self.can.create_image(0,0,image = self.img, anchor = NW)
        
        self.can.create_text(400,100,text = "UPDATE PASSWORD",fill = "#080A52", font = ('Comic Sans MS',28,"bold"))
        self.can.create_text(195,230,text = "Old Password",fill = "#080A52", font = ('Comic Sans MS',24,"bold"))
        self.can.create_text(200,270,text = "New Password",fill = "#080A52", font = ('Comic Sans MS',24,"bold"))

        self.ent_oldpassword = Entry(self.frame, textvariable = self.oldpassword ,font=('',22),fg="#080A52",bg="#F2E3BA")
        self.ent_olpassword.place(x=340,y=210)

        self.ent_newpassword = Entry(self.frame, textvariable = self.newpassword ,show = "*",font=('',22),fg="#080A52",bg="#F2E3BA")
        self.ent_newpassword.place(x=340,y=250)

        self.btn = Button(self.frame,text = "UPDATE",font=('Comic Sans MS',22,"bold"), fg="#080A52",bg = "#F2E3BA",
                          command = update_password)
        self.btn.place(x=340,y=330)

        self.frame.place(x=0,y=0)

        self.tk.resizable(height = False , width = False)
        self.tk.mainloop()

    def update_password(self):
        tupl = (self.name.get(),)

        if( self.oldpassword.get() != "" and
            self.newpassword.get() != ""):

            obj = database.database()
            obj.add_dept(tupl)

            messagebox.showinfo("Success","Password has been updated")

            

        else:
            messagebox.showinfo("Error","Please fill all the fields")

d = Main()
