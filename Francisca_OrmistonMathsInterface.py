# CSC3 2021
# Ormiston Computing Interface Class
# Francisca Nel
# Ver 5

import random
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
        Button(self.name_page,command=lambda:[self.check_name_input(self.name_page),self.selection()], text="Next",fg='#434343',bg="#78c043", border=0, height=1, width=8).grid(row=3,column=2,pady=(50,0))


####### FUNCTIONS TO BE USED #######

# Checks if the name has input. (there is no checking of integer input in the name)
    def check_name_input(self,cpage):
        if not self.student_name.get():
            print('enter a name please')
        else:
            self.get_name()
            self.next_page(cpage)

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
        self.selection_page.grid_configure(padx=(0,0),pady=(20,0))
        print('name is:',self.student.student_name) # checking if name is saved to student class

        self.qtypesbuttons = [] # qtypes = question types, i.e: addition, subtraction...
        self.diffbuttons = [] # diff = difficulty, i.e: easy, hard...

    # Button selection for question types
        self.selectionfunc(self.student.qtypes,self.qtypesbuttons,self.student.selected_questiontype,1)
    # Button selection for difficulties
        self.selectionfunc(self.student.difficulties,self.diffbuttons,self.student.selected_difficulty,2)
    # next button
        Button(self.selection_page,command=lambda:[self.check_qbutton_selected(self.selection_page),self.question1()], text="Next",fg='#434343',bg="#78c043", border=0, height=1, width=8).grid(row=3,column=4,pady=(50,0))

# Function for selection of buttons to be used with question types and difficulties
    def selectionfunc(self,to_select,buttonlist,selection,row):
    # labels 
        i = 0 # index
        c = 0 # column
        r = row # row

        for i in range(len(to_select)):
            t = to_select[i]
            buttonlist.append(Button(self.selection_page, text=t, command = lambda p=i: self.button_pressed(p,to_select,buttonlist,selection)))
            if c < 4:
                c = c + 1

            buttonlist[i].grid(column=c, row=r, padx=(8),pady=8)
            buttonlist[i].config(width=10,bg="#ff9900", fg='#434343', border=0, highlightthickness=4)

# checks if button is pressed by detecting button colour as green or orange
    def button_pressed(self,sel,to_select,buttonlist,selection):
        print(sel)
        b = buttonlist[sel]
        selq = to_select[sel]
    # If the button is clicked while green, the selection is removed from the list
        if b.cget('bg') == "#64a335" :
            b.config(bg="#ff9900")
            selection.remove(selq)   
    # If the button is clicked while orange, it is turned green and added to the list
        elif len(selection) < 1:
            b.config(bg="#64a335")
            selection.append(selq)
        print(selection)

# checks whether there was a selection for the question type and the difficulty lists
    def check_qbutton_selected(self,cpage): # cpage = current page
        if len(self.student.selected_questiontype) == 0:
            print('please select a question type')
        else:
            self.check_dbutton_selected(cpage)
    def check_dbutton_selected(self,cpage):
        if len(self.student.selected_difficulty) == 0:
            print('please select a difficulty')
        else:
            self.next_page(cpage)

####### PAGE 3 #######
    def question1(self):
        self.question1_page = Frame(root, bg='#EEEEEE')
        self.formatting(self.question1_page)
        self.qnum = 1

        #self.qtypes = ['Addition +','Subtraction -','Times x','Division ÷']
        #self.difficulties = ['Easy','Intermediate','Hard']

        self.questiontype = str(self.student.selected_questiontype[0])
        self.difficulty = str(self.student.selected_difficulty[0])

        print(self.questiontype,'\n',self.difficulty)

    # Question title
        Label(self.question1_page,text="Question {}".format(self.qnum),bg='#efefef',fg='#ff9900',font='CenturyGothic 48 bold').grid(row=1)

    # Question label
        if self.questiontype=='Addition +' and self.difficulty=='Easy':
            self.easy()
            self.addition()
            Label(self.question1_page,text="{} + {} =".format(self.n,self.n2),fg='#434343').grid(row=2,column=0)
            self.answer = Entry(self.question1_page, bg="#434343", fg='#efefef', border=0, highlightbackground = "#434343", highlightthickness=5,width=5)
            self.answer.grid(row=2,column=1)
            print(self.a)

    # Next button hidden under check button
        Button(self.question1_page, text="Next",fg='#434343',bg="#78c043", border=0, height=1, width=8).grid(row=3,column=2,pady=(50,0))
    # Check button
        self.checkbutton = Button(self.question1_page,command=lambda:[self.checkanswer()], text="Check",fg='#434343',bg="#78c043", border=0, height=1, width=8)
        self.checkbutton.grid(row=3,column=2,pady=(50,0))

# difficulties and question types
    def addition(self):
        self.a = int(self.n + self.n2)

    def easy(self):
        self.n = random.randint(1,5)
        self.n2 = random.randint(1,5)

# check whether answer was correct, incorrect, or invalid
    def checkanswer(self):
        self.ans = int(self.answer.get())
        while True:
            try:
                int(self.ans)
                break
            except ValueError:
                print('Please enter a number')
        if int(self.ans) == self.a:
            print('correct!')
            Label(self.question1_page,text="Correct!",fg='#434343').grid(row=3,column=0)
            self.remove_check()
        if int(self.ans) != self.a:
            print('incorrect, the answer is',self.a)
            Label(self.question1_page,text="Incorrect, the answer is {}".format(self.a),fg='#434343').grid(row=3,column=0)
            self.remove_check()
            
# removes 'check' button to reveal the 'next' button that takes to the next page
    def remove_check(self):
        self.checkbutton.grid_remove()


Interface()
root.mainloop() 