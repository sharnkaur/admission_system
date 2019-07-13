from tkinter import *
import database
from tkinter import messagebox

class Main:
    def __init__(self):
        self.tk = Tk()
        self.tk.title("Admin Login")

        height = self.tk.winfo_screenheight()
        width = self.tk.winfo_screenwidth()

        y = (height-600)//2-20
        x = (width-800)//2
        self.tk.geometry('800x600+{}+{}'.format(str(x),str(y)))
    
        self.frame = Frame(self.tk,height = 600,width = 800)
        self.can = Canvas(self.frame,height = 600,width = 800,bg="#292826")
        self.can.pack()
        self.email=StringVar(self.tk)
        self.password=StringVar(self.tk)

        self.img = PhotoImage(file="./images/desk_12.png")
        self.can.create_image(0,0,image = self.img, anchor = NW)

        self.can_1 = Canvas(self.frame, height = 160, width = 180,bg="#292826")
        self.can.pack()
        
        self.icon_img = PhotoImage(file="./images/use.png")
        self.can.create_image(310,140,image = self.icon_img, anchor = NW)
        
        self.can.create_text(400,100,text = "ADMIN LOGIN",fill = "#F9D342", font = ('Comic Sans MS',28,"bold"))
        self.can.create_text(190,340,text = "Email",fill = "#F9D342", font = ('Comic Sans MS',24,"bold"))
        self.can.create_text(220,380,text = "Password",fill = "#F9D342", font = ('Comic Sans MS',24,"bold"))

        self.ent_email = Entry(self.frame,font=('',22),fg="#292826",bg="#FCFDFE")
        self.ent_email.place(x=310,y=320)

        self.ent_password = Entry(self.frame,show = "*",font=('',22),fg="#292826",bg="#FCFDFE")
        self.ent_password.place(x=310,y=360)

        self.btn = Button(self.frame,text = "LOGIN",font=('Comic Sans MS',22,"bold"), fg="#F9D342",bg = "#FCFDFE")
        self.btn.place(x=310,y=420)

        self.frame.place(x=0,y=0)

        self.tk.resizable(height = False , width = False)
        self.tk.mainloop()

    

d = Main()
