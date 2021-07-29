# CSC3 2021
# Ormiston Computing Interface Class
# Francisca Nel
# Ver 2

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
        self.formatting(self.name_page)
       
    # OSC logo displayed using PhotoImage. 
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
        self.nextbutton = Button(self.name_page,command=lambda:[self.get_name,self.next_page(self.name_page),self.selection()], text="Next",fg='#434343',bg="#78c043", border=0, height=1, width=8).pack(side=RIGHT,pady=(40,0))


####### FUNCTIONS TO BE USED #######

# Formats each page with the same font and packs it
    def formatting(self,page):
        page.option_add('*Font', 'CenturyGothic 24 bold')
        page.pack()

# Next page function- forgets the current page
    def next_page(self,cpage):
        cpage.pack_forget()

# Function that collects the student's name
    def get_name(self): 
        sn = self.student_name.get()
        self.student = Student(sn)

####### PAGE 2 #######

    def selection(self):
        self.selection_page = Frame(root, bg='#EEEEEE')
        self.formatting(self.selection_page)

        Label(self.name_page,text="Ormiston Maths",bg='#efefef',fg='#ff9900',font='CenturyGothic 48 bold').pack()
        

Interface()
root.mainloop()