from tkinter import *
import database
from tkinter import messagebox

class Main:
    def __init__(self):
        self.tk = Tk()
        self.tk.title("Add Department")
        
        height = self.tk.winfo_screenheight()
        width = self.tk.winfo_screenwidth()
        
        print(height,width)
        y = (height-600)//2-20
        x = (width-600)//2
        self.tk.geometry('600x600+{}+{}'.format(str(x),str(y)))

        self.frame = Frame(self.tk,height = 600,width = 600)
        self.can = Canvas(self.frame,height = 600,width = 600,bg="#FCBC05")
        self.can.pack()

        self.name = StringVar(self.tk)

        self.img = PhotoImage(file = "./images/yellow.png")
        self.can.create_image(0,0,image = self.img, anchor = NW)

        self.can_1 = Canvas(self.can,height = 100,width = 100,bg="#FCBC05")
        self.can.pack()

        self.icon_img = PhotoImage(file = "./images/home_icon.png")
        self.can.create_image(310,140,image = self.icon_img, anchor = NW)
        
        self.can.create_text(300,60,text = "ADD DEPARTMENT",fill = "#FFFFFF", font = ('Comic Sans MS',24,"bold"))
        self.can.create_text(100,380,text = "Name",fill = "#FFFFFF", font = ('Comic Sans MS',26))

        self.ent_name = Entry(self.frame, font = ('',22),fg="#FFFFFF",bg="#FCBC05",textvariable=self.name)
        self.ent_name.place(x=200,y=370)

        self.btn = Button(self.frame,text = "SUBMIT", font = ('Comic Sans MS',22),fg="#FFFFFF",bg="#FCBC05"
                          ,command=self.add_data)
        self.btn.place(x=220,y=420)


        self.frame.place(x=0,y=0)
      
        self.tk.resizable(height = False, width = False)
        self.tk.mainloop()

    def add_data(self):
        tupl = (self.name.get(),)

        if( self.name.get() != ""):

            obj = database.database()
            obj.add_dept(tupl)

            messagebox.showinfo("Success","Department has been created")

            

        else:
            messagebox.showinfo("Error","Please fill all the fields")

              

d = Main()

    
