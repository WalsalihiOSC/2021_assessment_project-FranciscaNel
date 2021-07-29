# CSC3 2021
# Ormiston Computing Interface Class
# Francisca Nel
# Ver 5

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
        self.nextbutton = Button(self.name_page,command=lambda:[self.get_name(),self.next_page(self.name_page),self.next_page(self.logotitle),self.selection()], text="Next",fg='#434343',bg="#78c043", border=0, height=1, width=8).grid(row=3,column=2,pady=(50,0))


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
        self.selection_page.grid_configure(padx=(0,0),pady=(20,0))
        print('name is:',self.student.student_name) # checking if name is saved to student class

    # button iteration

        i = 0 # index
        c = 0 # column
        r = 0 # row

        self.qtypesbuttons = [] # list for buttons

        for i in range(len(self.student.qtypes)): # laying out the buttons using iteration
            t = self.student.qtypes[i]
            self.qtypesbuttons.append(Button(self.selection_page, text=t, command = lambda p=i: self.button_pressed(p)))
            if c < 4:
                c = c + 1 # for each button, the column is increased by 1

            self.qtypesbuttons[i].grid(column=c, row=r, padx=(8),pady=8)
            self.qtypesbuttons[i].config(width=10,bg="#ff9900", fg='#434343', border=0, highlightthickness=4)

# checks if button is pressed by detecting button colour as green or orange
    def button_pressed(self,sel):
        print(sel)
        b = self.qtypesbuttons[sel]
        selq = self.student.qtypes[sel]
    # If the button is clicked while green, the selection is removed from the list
        if b.cget('bg') == "#64a335" :
            b.config(bg="#ff9900")
            self.student.questiontypes.remove(selq)   
    # If the button is clicked while orange, it is turned green and added to the list
        elif len(self.student.questiontypes) < 1:
            b.config(bg="#64a335")
            self.student.questiontypes.append(selq)
        print(self.student.questiontypes)

Interface()
root.mainloop() 