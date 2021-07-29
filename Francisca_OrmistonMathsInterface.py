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

class Interface:
    def __init__(self):

####### PAGE 1 #######

        self.name_page = Frame(root, bg='#EEEEEE')
        self.formatting(self.name_page)
       
    # OSC logo displayed using PhotoImage.
        self.img = PhotoImage(file="OJC_logo3.gif")
        self.logotitle = Label(self.name_page, image=self.img, bg='#EEEEEE')
        self.logotitle.photo = self.img
        self.logotitle.grid()
    # Title
        Label(self.name_page,text="Ormiston Maths",bg='#efefef',fg='#ff9900',font='CenturyGothic 48 bold').grid(row=1)
    # Labels
        Label(self.name_page,text="Name",bg='#efefef',fg='#434343').grid(row=2,pady=(20),padx=(0,400))
    # Text boxes
        self.student_name = Entry(self.name_page, bg="#434343", fg='#efefef', border=0, highlightbackground = "#434343", highlightthickness=5)
        self.student_name.grid(row=2,padx=(120,0))
    # Buttons
        self.nextbutton = Button(self.name_page,command=lambda:[self.get_name,self.next_page(self.name_page),self.next_page(self.logotitle),self.selection()], text="Next",fg='#434343',bg="#78c043", border=0, height=1, width=8).grid(row=3,column=2,pady=(50,0))


####### FUNCTIONS TO BE USED #######

# Formats each page with the same font and packs it
    def formatting(self,page):
        page.option_add('*Font', 'CenturyGothic 24 bold')
        page.grid(row=0,column=0,padx=(170,0))

# Next page function- forgets the current page
    def next_page(self,cpage):
        cpage.grid_forget()

# Function that collects the student's name
    def get_name(self): 
        sn = self.student_name.get()
        self.student = Student(sn)

####### PAGE 2 #######

    def selection(self):
        self.selection_page = Frame(root, bg='#EEEEEE')
        self.formatting(self.selection_page)
        self.selection_page.grid_columnconfigure((0, 1, 2), weight=1)
        self.selection_page.grid_configure(padx=(50,0),pady=(20,0))

    # labels - There is a more efficient way of doing this, but the buttons will be line-by-line for now.

        Label(self.selection_page,text="Ormiston Maths",bg='#efefef',fg='#ff9900',font='CenturyGothic 48 bold').grid() # Title
    # Question Type Selection.pack
        Label(self.selection_page,text="Question Type",bg='#efefef',fg='#434343').grid(row=1)
        Button(self.selection_page, text="Addition +",fg='#434343',bg="#ff9900", border=0, height=2, width=9).grid(row=2,column=0,sticky=W)
        Button(self.selection_page, text="Subtraction −",fg='#434343',bg="#ff9900", border=0, height=2, width=11).grid(row=2,column=0,padx=(188,0),sticky=W)
        Button(self.selection_page, text="Times X",fg='#434343',bg="#ff9900", border=0, height=2, width=9).grid(row=2,column=0,padx=(414,0),sticky=W)
        Button(self.selection_page, text="Division ÷",fg='#434343',bg="#ff9900", border=0, height=2, width=9).grid(row=2,column=0,padx=(602,0),sticky=W)
    # Difficulty Level Selection
        Label(self.selection_page,text="Difficulty Level",bg='#efefef',fg='#434343').grid(row=6)
        Button(self.selection_page, text="Easy",fg='#434343',bg="#ff9900", border=0, height=2, width=9).grid(row=7,column=0,padx=(90,0),sticky=W)
        Button(self.selection_page, text="Intermediate",fg='#434343',bg="#ff9900", border=0, height=2, width=11).grid(row=7,column=0,padx=(280,0),sticky=W)
        Button(self.selection_page, text="Hard",fg='#434343',bg="#ff9900", border=0, height=2, width=9).grid(row=7,column=0,padx=(508,0),sticky=W)
        
        self.nextbutton = Button(self.selection_page, text="Next",fg='#434343',bg="#78c043", border=0, height=1, width=8).grid(row=10,pady=(20,0),sticky=E)
 
Interface()
root.mainloop() 