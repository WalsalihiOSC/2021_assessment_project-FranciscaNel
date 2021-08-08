# CSC3 2021
# Ormiston Computing Interface Class
# Francisca Nel
# Ver 12

from Francisca_Math_operations_class import Mathop
from Francisca_OrmistonMathsStudent import Student 
from tkinter import *

root = Tk()
root.configure(bg='#EEEEEE')
root.grid_columnconfigure(0, weight=1)
root.grid_rowconfigure(0, weight=1)
root.title("Ormiston Maths")
root.geometry("880x495") # small 16:9 ratio window (55x)

class Interface:
    def __init__(self):

######################################################################

######### PAGE 1 ########
####### Name Page #######

        self.name_page = Frame(root, bg='#EEEEEE')
        self.formatting(self.name_page)
       
    # Ormiston Primary School logo displayed using PhotoImage.
        self.img = PhotoImage(file="OPS_logo3.gif")
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

# Checks if the name has input. (there is no checking of integer input in the name)
    def check_name_input(self,cpage):
        if not self.student_name.get():
            print('enter a name please')
        else:
            self.get_name()
            self.next_page(cpage)

# Formats each page with the same font and grids it
    def formatting(self,page):
        page.option_add('*Font', 'CenturyGothic 24 bold')
        page.grid(padx=(170,0))
        page.grid_columnconfigure(0, weight=1)
        page.grid_rowconfigure(0, weight=1)

# Next page function- forgets the current page
    def next_page(self,cpage):
        cpage.grid_forget()

# Function that collects the student's name
    def get_name(self): 
        sn = self.student_name.get()
        self.student = Student(sn)

######################################################################

##########  PAGE 2  #########
####### Selection Page ######

    def selection(self):
        self.f=1
        self.selection_page = Frame(root, bg='#EEEEEE')
        self.formatting(self.selection_page)
        self.selection_page.grid_configure(padx=(0,0),pady=(20,0))
        print('name is:',self.student.student_name) # checking if name is saved to student class
        self.qtypesbuttons = [] # qtypes = question types, i.e: addition, subtraction...
        self.diffbuttons = [] # diff = difficulty, i.e: easy, hard...

    # Button selection for question types
        self.selectionfunc(self.student.qtypes,self.qtypesbuttons,self.student.selected_questiontype,1,self.student.selected_questiontypes)
        Label(self.selection_page,fg='#434343',text='Questions').grid(row=0,column=2)
    # Button selection for difficulties
        Label(self.selection_page,fg='#434343',text='Difficulties').grid(row=2,column=2,pady=(50,0))
        self.selectionfunc(self.student.difficulties,self.diffbuttons,self.student.selected_difficulty,3,self.student.selected_difficulties)
    # next button
        Button(self.selection_page,command=lambda:[self.check_qbutton_selected(self.selection_page),self.questions()], text="Next",fg='#434343',bg="#78c043", border=0, height=1, width=8).grid(row=4,column=4,pady=(50,0))

# Function for selection of buttons to be used with question types and difficulties
    def selectionfunc(self,to_select,buttonlist,selection,row,classlist):
    # Selection Buttons 
        i = 0 # index
        c = 0 # column
        r = row 

        for i in range(len(to_select)):
            t = to_select[i]
            buttonlist.append(Button(self.selection_page, text=t, command = lambda p=i: self.button_pressed(p,to_select,buttonlist,selection,classlist)))
            if c < 4:
                c = c + 1

            buttonlist[i].grid(column=c, row=r, padx=(8),pady=8)
            buttonlist[i].config(width=10,height=1,bg="#ff9900", fg='#434343', border=0, highlightthickness=5)

# checks if button is pressed by detecting button colour as green or orange
    def button_pressed(self,sel,to_select,buttonlist,selection,classlist):
        print(sel)
        b = buttonlist[sel]
        selq = to_select[sel]
    # If the button is clicked while green, the selection is removed from the list
        if b.cget('bg') == "#64a335" :
            b.config(bg="#ff9900")
            selection.remove(selq) 
            classlist.remove(selq)  
    # If the button is clicked while orange, it is turned green and added to the list
        elif len(selection) < 1:
            b.config(bg="#64a335")
            selection.append(selq)
            classlist.append(selq)
        print("classlist:",selq)
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

    def questiontypeforquestions(self,page):
        self.questiontypeforq = StringVar
        self.questiontype = str(self.student.selected_questiontype[0])
        self.difficulty = str(self.student.selected_difficulty[0])
    # Variables for the mathop class 
        qt = self.questiontypeforq
        d = self.difficulty
        self.maths = Mathop(qt,d)
        print(self.questiontype,'\n',self.difficulty)
    # determines type of question to be used from selection
        if self.questiontype=='Addition +':
            self.questiontypeforq = self.maths.addition()
            Label(page,text="{} + {} =".format(self.maths.n,self.maths.n2),fg='#434343').grid(row=2,column=0)
        elif self.questiontype=='Times x':
            self.questiontypeforq = self.maths.multiplication()
            Label(page,text="{} x {} =".format(self.maths.n,self.maths.n2),fg='#434343').grid(row=2,column=0)
        elif self.questiontype=='Division ÷':
            self.questiontypeforq = self.maths.division()
            Label(page,text="{} ÷ {} =".format(self.maths.n2,self.maths.n),fg='#434343').grid(row=2,column=0)
        elif self.questiontype=='Subtraction -':
            self.questiontypeforq = self.maths.subtraction()
            Label(page,text="{} - {} =".format(self.maths.n,self.maths.n2),fg='#434343').grid(row=2,column=0)

######################################################################

######## PAGE 3-13 ########
###### Question Pages #####

    def questions(self):
        self.page = Frame(root, bg='#EEEEEE')
        self.formatting(self.page)
    # Question title
        Label(self.page,text="Question {}".format(self.f),bg='#efefef',fg='#ff9900',font='CenturyGothic 48 bold').grid(row=1,padx=(50,0))
    # Answer text box
        self.answer = Entry(self.page, bg="#434343", fg='#efefef', border=0, highlightbackground = "#434343", highlightthickness=5,width=5)
        self.answer.grid(row=2,column=1)
    # Next button hidden under check button
    # Every time 'Next' is pressed, question function is called until f=10 frames 
        Button(self.page, text="Next",command=lambda:[self.question_number(),self.next_page(self.page),self.questions()],fg='#434343',bg="#78c043", border=0, height=1, width=8).grid(row=3,column=2,pady=(50,0))
    # Check button
        self.checkbutton = Button(self.page,command=lambda:[self.checkanswer(self.page)], text="Check",fg='#434343',bg="#78c043", border=0, height=1, width=8)
        self.checkbutton.grid(row=3,column=2,pady=(50,0))
    # determines type of question to be used in the rest of the 10 questions
        self.questiontypeforquestions(self.page)
        if self.f == 11:
            self.next_page(self.page)
            self.results()

# Function for adding to f after 'next' button is pressed
    def question_number(self):
        self.f=self.f+1

# removes 'check' button to reveal the 'next' button that takes to the next page
    def remove_check(self):
        self.checkbutton.grid_remove()
            
# check whether answer was correct, incorrect, or invalid
    def checkanswer(self,page):
        self.ans = int(self.answer.get())
        while True:
            try:
                int(self.ans)
                break
            except ValueError:
                print('Please enter a number')
        if int(self.ans) == self.maths.a:
            print('correct!')
            Label(page,text="Correct!",fg='#78c043').grid(row=3,column=0)
            self.student.correct_answers.append(self.ans)
            print(self.student.correct_answers)
            self.remove_check()

        if int(self.ans) != self.maths.a:
            print('incorrect, the answer is',self.maths.a)
            Label(page,text="Incorrect, the answer is {}".format(self.maths.a),fg='#ff5252').grid(row=3,column=0)
            self.remove_check()


######################################################################

######### PAGE 13 #########
####### Results Page ######

    def results(self):
        self.results_page = Frame(root, bg='#EEEEEE')
        self.formatting(self.results_page)
        self.results_page.grid_configure(padx=(0))

        self.score = len(self.student.correct_answers)
        self.student.scores.append(self.score)

    # Question title
        Label(self.results_page,text="Results\n{} on {} Difficulty".format(self.questiontype,self.difficulty),bg='#efefef',fg='#ff9900',font='CenturyGothic 35 bold').grid(row=1)
    # Results subheader
        if self.score > 4:
            Label(self.results_page,text="Good job {}, you got {}/10 answers correct".format(self.student.student_name,self.score),bg='#efefef',fg='#434343').grid(row=2,pady=(0,50))
        elif self.score < 5:
            Label(self.results_page,text="Practice makes perfect {},\nyou got {}/10 answers correct".format(self.student.student_name,self.score),bg='#efefef',fg='#434343').grid(row=2)
    # restart/logout buttons
        Button(self.results_page, text="Restart",command= lambda:[self.store(),self.reset_var(),self.next_page(self.results_page),self.selection()],fg='#434343',bg="#78c043", border=0, height=1, width=8).grid(row=3,sticky=E)
        Button(self.results_page, text="Log out",command= lambda:[self.store(),self.reset_var(),self.reset_user(),self.next_page(self.results_page),self.__init__()],fg='#434343',bg="#ff9900", border=0, height=1, width=8).grid(row=3,sticky=W)

# Resetting all variables for restart
    def reset_var(self):
        self.student.scores = []
        self.student.selected_questiontype = []
        self.student.selected_difficulty = []
        self.student.correct_answers = []
        self.score = None
# Resetting user name for logging out
    def reset_user(self):
        self.student.student_name = None

# Function for storing info to file
    def store(self):
        pass
                          
######################################################################

Interface()
root.mainloop() 