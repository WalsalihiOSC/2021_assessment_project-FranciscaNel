# CSC3 2021
# Ormiston Computing Interface Class
# Francisca Nel
# Ver 1

from Francisca_OrmistonMathsStudent import Student
from tkinter import *

root = Tk()
root.configure(bg='#EEEEEE')
root.title("Ormiston Maths")
root.geometry("880x495") # small 16:9 ratio window (55x)

####### PAGE 1 #######

class Interface:
    def __init__(self):
        self.name_page = Frame(root, bg='#EEEEEE')
        self.name_page.option_add('*Font', 'CenturyGothic 24 bold')
        self.name_page.pack()

    # OSC logo
        self.img = PhotoImage(file="OJC_logo3.gif")
        self.logotitle = Label(self.name_page, image=self.img, bg='#EEEEEE')
        self.logotitle.photo = self.img
        self.logotitle.pack(side=TOP)

    # Labels
        Label(self.name_page,text="Ormiston Maths",bg='#efefef',fg='#ff9900',font='CenturyGothic 48 bold').pack()
        Label(self.name_page,text="Name",bg='#efefef',fg='#434343').pack(side=LEFT,pady=(0,60),padx=(20,20)) 
    # Text boxes
        self.student_name=Entry(self.name_page, bg="#434343", fg='#efefef', border=0, highlightbackground = "#434343", highlightthickness=5).pack(pady=(20,0))
    # Buttons
        self.nextbutton = Button(self.name_page,command=lambda:[self.next_page(self.logotitle),self.selection()], text="Next",fg='#434343',bg="#78c043", border=0, height=1, width=8).pack(side=RIGHT,pady=(40,0))

    # Next page function 
    def next_page(self,cpage):
        cpage.pack_forget()

####### PAGE 2 #######

    def selection(self):
        self.selection_page = Frame(root, bg='#EEEEEE')
        self.selection_page.option_add('*Font', 'CenturyGothic 24 bold')
        self.selection_page.pack()

Interface()
root.mainloop()