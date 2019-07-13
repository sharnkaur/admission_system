from tkinter import *
class Main:
    def __init__(self):
        self.win=Tk()
        self.win.geometry('600x600')
        height = self.win.winfo_screenheight()
        width = self.win.winfo_screenwidth()
    
        y = (height - 600)//2-20
        x = (width - 900)//2
    
        self.win.geometry('900x600+'+str(x)+'+'+str(y)+'')
        self.can=Canvas(self.win,width=900,height=600)
        self.can.place(x=0,y=0)
        self.img=PhotoImage(file='./images/image7p.gif')
        self.can.create_image(0,0,image=self.img,anchor=NW)


        self.menu=Menu(self.can)
        self.sub=Menu(self.menu)
        self.sub.add_cascade(label="Add Student",font=('ALGERIAN',15))
        self.sub.add_cascade(label="Manage Student",font=('ALGERIAN',15))
        self.menu.add_cascade(label="Admission",menu=self.sub)
        
        self.sub=Menu(self.menu)
        self.sub.add_cascade(label="Update password",font=('ALGERIAN',15))
        self.sub.add_cascade(label="LogOut",font=('ALGERIAN',15))
        self.menu.add_cascade(label="Account",menu=self.sub)

        self.win.config(menu=self.menu)
        self.win.resizable(height=False,width=False)
        self.win.mainloop()

    def change(self):
    
        self.main_frame.destroy()
        x=secondframe.secondframe(self.win)

    def do(self):
        self.main_frame.destroy()
        x=firstframee.firstframe(self.win)

d=Main()
        
