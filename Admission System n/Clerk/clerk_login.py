from tkinter import *

class Main:
    def __init__(self):
        self.tk = Tk()
        self.tk.title("Clerk Login")

        height = self.tk.winfo_screenheight()
        width = self.tk.winfo_screenwidth()

        y = (height-600)//2-20
        x = (width-800)//2
        self.tk.geometry('800x600+{}+{}'.format(str(x),str(y)))
    
        self.frame = Frame(self.tk,height = 600,width = 800)
        self.can = Canvas(self.frame,height = 600,width = 800,bg="#161B21")
        self.can.pack()

        self.img = PhotoImage(file="./images/office_21.png")
        self.can.create_image(0,0,image = self.img, anchor = NW)
        
        self.can.create_text(400,100,text = "USER LOGIN",fill = "#080A52", font = ('Comic Sans MS',28,"bold"))
        self.can.create_text(200,230,text = "Email",fill = "#080A52", font = ('Comic Sans MS',24,"bold"))
        self.can.create_text(230,270,text = "Password",fill = "#080A52", font = ('Comic Sans MS',24,"bold"))

        self.ent_email = Entry(self.frame,font=('',22),fg="#080A52",bg="#F2E3BA")
        self.ent_email.place(x=340,y=210)

        self.ent_password = Entry(self.frame,show = "*",font=('',22),fg="#080A52",bg="#F2E3BA")
        self.ent_password.place(x=340,y=250)

        self.btn = Button(self.frame,text = "LOGIN",font=('Comic Sans MS',22,"bold"), fg="#080A52",bg = "#F2E3BA")
        self.btn.place(x=340,y=330)

        self.frame.place(x=0,y=0)

        self.tk.resizable(height = False , width = False)
        self.tk.mainloop()

d = Main()
