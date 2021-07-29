# CSC3 2021
# Ormiston Computing Interface Class
# Francisca Nel
# Ver 3

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
        self.student_name = Entry(self.name_page, bg="#434343", fg='#efefef', border=0, highlightbackground = "#434343", highlightthickness=5)
        self.student_name.pack(pady=(20,0))
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

    # labels - There is a much more efficient way of doing this, but the buttons will be line-by-line for now.
    # Because I am using pack, I have to make a seperate frame for a different row...

        Label(self.selection_page,text="Ormiston Maths",bg='#efefef',fg='#ff9900',font='CenturyGothic 48 bold').pack(pady=10) # Title
    # Question Type Selection
        Label(self.selection_page,text="Question Type",bg='#efefef',fg='#434343').pack()
        Button(self.selection_page, text="Addition +",fg='#434343',bg="#ff9900", border=0, height=2, width=9).pack(side=LEFT,padx=15)
        Button(self.selection_page, text="Subtraction −",fg='#434343',bg="#ff9900", border=0, height=2, width=11).pack(side=LEFT)
        Button(self.selection_page, text="Times X",fg='#434343',bg="#ff9900", border=0, height=2, width=9).pack(side=LEFT,padx=15)
        Button(self.selection_page, text="Division ÷",fg='#434343',bg="#ff9900", border=0, height=2, width=9).pack(side=LEFT)
    # Difficulty Level Selection
        self.buttons2 = Frame(root,bg='#EEEEEE')
        self.formatting(self.buttons2)
        Label(self.buttons2,text="Difficulty Level",bg='#efefef',fg='#434343').pack(side=TOP,pady=(15,0))
        Button(self.buttons2, text="Easy",fg='#434343',bg="#ff9900", border=0, height=2, width=9).pack(side=LEFT,padx=15)
        Button(self.buttons2, text="Intermediate",fg='#434343',bg="#ff9900", border=0, height=2, width=11).pack(side=LEFT)
        Button(self.buttons2, text="Hard",fg='#434343',bg="#ff9900", border=0, height=2, width=9).pack(side=LEFT,padx=15)
        
        self.nextbutton = Button(self.buttons2, text="Next",fg='#434343',bg="#78c043", border=0, height=1, width=8).pack(side=BOTTOM,pady=(40,0))
 
Interface()
root.mainloop() 