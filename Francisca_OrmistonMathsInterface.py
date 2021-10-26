# CSC3 2021
# Ormiston Computing Interface Class
# Francisca Nel
# Ver 22

from Francisca_Math_operations_class import Mathop
from Francisca_OrmistonMathsStudent import Student 
from tkinter import *
from tkinter import messagebox

root = Tk()
root.configure(bg='#EDEDED')
# This centers all of the widgets and auto-positions them by window size
root.grid_columnconfigure(0, weight=1)
root.grid_rowconfigure(0, weight=1)
root.title("Ormiston Maths")
root.geometry("880x550") # small 16:9 ratio window (55x)

class Interface:
    def __init__(self):
    ### FONTS ###
        self.title_size = 'CenturyGothic 48 bold'
        self.qsize = 'CenturyGothic 40 bold'
        self.symbl_size = 'CenturyGothic 50 bold'
        self.msg_size = 'CenturyGothic 30 bold'

    ### COLOURS ### 
# I am not using tkinter's colours because I am using custom colours
       #self.color = [ 0:darkgrey, 1:lightgrey, 2:green, 3:red, 4:orange, 5:darkgreen ]
        self.color = ['#434343', '#EDEDED', '#78c043', '#ff5252', '#ff9900', '#64a335']

######################################### PAGE 1 #########################################
####################################### Name Page ########################################


        self.name_page = Frame(root,bg=self.color[1])
        self.formatting(self.name_page)
       
    # Ormiston Primary School logo displayed using PhotoImage.
        self.img = PhotoImage(file="OPS_logo3.gif")
        self.logotitle = Label(self.name_page, image=self.img,bg=self.color[1])
        self.logotitle.photo = self.img
        self.logotitle.grid()
    # Title
        Label(self.name_page,text="Ormiston Maths",fg=self.color[4],bg=self.color[1],font=self.title_size).grid(row=1)
    # Labels
        Label(self.name_page,text="Name",fg=self.color[0],bg=self.color[1]).grid(row=2,pady=(20),padx=(0,400))
        Label(self.name_page,text="Age",fg=self.color[0],bg=self.color[1]).grid(row=3,pady=(20),padx=(0,400))
    # Text boxes
        self.student_name = Entry(self.name_page, bg=self.color[0], fg=self.color[1], border=0, 
                                  highlightbackground = self.color[0], highlightthickness=5)
        self.student_name.grid(row=2,padx=(120,0))

        self.student_age = Entry(self.name_page, bg=self.color[0], fg=self.color[1], border=0, 
                                  highlightbackground = self.color[0], highlightthickness=5)
        self.student_age.grid(row=3,padx=(120,0))
    # Buttons
        self.nextb(self.name_page,lambda:[self.check_name_age_input(self.name_page)])
        self.n.grid(row=4,column=2,pady=(20,0))

##### BUTTONS & LABELS #####
    def nextb(self,page,cmd):
        self.n = Button(page,command=cmd,text="Next",fg=self.color[0],bg=self.color[2],border=0,height=1,width=8)


# Checks if the name has input.
    def check_name_age_input(self,cpage):
        
    # Check Age
        if not self.student_age.get(): 
            messagebox.showerror(title='Error',message='Please enter your age as a number between 5 and 12')
        elif self.student_age.get().isalpha(): # isalpha() returns True when it detects letters 
            messagebox.showerror(title='Error',message='Age must be in numbers only!\nPlease enter your age as a number between 5 and 12')
        elif int(self.student_age.get()) > 12: 
            messagebox.showerror(title='Error',message='Age is too high!\nPlease enter an age between 5 and 12')
        elif int(self.student_age.get()) < 5: 
            messagebox.showerror(title='Error',message='Age is too low!\nPlease enter an age between 5 and 12')

    # Check Name
        elif not self.student_name.get(): 
            messagebox.showerror(title='Error',message='Please enter your name')
        elif len(self.student_name.get()) > 12: 
            messagebox.showerror(title='Error',message='Name must be below 12 letters')
        elif len(self.student_name.get()) < 2: 
            messagebox.showerror(title='Error',message='Name must be over 1 letter')
        elif not self.student_name.get().isalpha(): 
            messagebox.showerror(title='Error',message='Name must be in letters only!')

        else:
            sn = self.student_name.get().capitalize() # every name capitalized for consistency
            sa = self.student_age.get()
            self.student = Student(sn,sa)
            self.next_page(cpage) 
            self.selection()

# Formats each page with the same font and grids it
    def formatting(self,page):
        page.option_add('*Font', 'CenturyGothic 24 bold')
        page.grid(padx=(170,0))
        page.grid_columnconfigure(0, weight=1)
        page.grid_rowconfigure(0, weight=1)

# Next page function- forgets the current page
    def next_page(self,cpage):
        cpage.grid_forget()


######################################### PAGE 2 #########################################
##################################### Selection Page #####################################


    def selection(self):
        self.f=1
        self.selection_page = Frame(root, bg=self.color[1])
        self.formatting(self.selection_page)
        self.selection_page.grid_configure(padx=(0,0),pady=(20,0))
    # checking if name and age is saved to student class
        print('name is:',self.student.student_name)
        print('age is:',self.student.student_age)

    # Button list to be printed
        self.qtypesbuttons = [] # qtypes = question types, i.e: addition, subtraction...
        self.diffbuttons = [] # diff = difficulty, i.e: easy, hard...

    # Button selection for question types
        Label(self.selection_page,fg=self.color[0], bg=self.color[1],text='Questions').grid(row=0, column=2)
        self.selectionfunc(self.student.qtypes, self.qtypesbuttons, self.student.selected_questiontype, 1)

    # Button selection for difficulties
        Label(self.selection_page,fg=self.color[0], bg=self.color[1],text='Difficulties').grid(row=2, column=2, pady=(50,0))
        self.selectionfunc(self.student.difficulties, self.diffbuttons, self.student.selected_difficulty, 3)
    
    # Next button
        self.nextb(self.selection_page, lambda:[self.check_qbutton_selected(self.selection_page),self.turnstr(),self.questions()])
        self.n.grid(row=4,column=4)
        self.n.config(text="Start")

# Function for selection of buttons to be used with question types and difficulties
    def selectionfunc(self,to_select,buttonlist,selection,row):
    # Selection Buttons 
        i = 0 # index
        c = 0 # column
        r = row 
        for i in range(len(to_select)):
            if to_select == self.student.qtypes:
                t = self.student.qtypes_smbl[i] # seperate list containing question type symbols
            else:
                t = to_select[i]
            buttonlist.append(Button(self.selection_page, text=t, command=lambda p=i:
                              self.button_pressed(p,to_select,buttonlist,selection)))
            if c < 4:
                c = c + 1
            buttonlist[i].grid(column=c, row=r, padx=(8),pady=8)
            buttonlist[i].config(width=10,height=2,bg=self.color[4], fg=self.color[0], border=0, 
                                 highlightthickness=5)

# checks if button is pressed by detecting button colour as green or orange
    def button_pressed(self, sel, to_select, buttonlist,selection):
        b = buttonlist[sel]
        selq = to_select[sel]
    # If the button is clicked while green, turned orange and removed from the list
        if b.cget('bg') == self.color[5] :
            b.config(bg= self.color[4], fg=self.color[0])
            selection.remove(selq) 
    # If the button is clicked while orange, it is turned green and added to the list
        elif len(selection) < 1:
            b.config(bg= self.color[5], fg=self.color[1])
            selection.append(selq)
        print("selection:", selection)

# checks whether there was a selection for the question type and the difficulty lists
    def check_qbutton_selected(self, cpage): # cpage = current page
        if len(self.student.selected_questiontype) == 0:
            messagebox.showerror(title='Error',message='Please select a question type')
        else:
            self.check_dbutton_selected(cpage)
    def check_dbutton_selected(self, cpage):
        if len(self.student.selected_difficulty) == 0:
            messagebox.showerror(title='Error',message='Please select a difficulty')
        else:
            self.next_page(cpage)

# Turn question type and difficulty selections from list to str
    def turnstr(self):
        self.questiontypeforq = StringVar
        self.questiontype = str(self.student.selected_questiontype[0])
        self.difficulty = str(self.student.selected_difficulty[0])

    def questiontypeforquestions(self, page):
    # Variables for the mathop class 
        qt = self.questiontypeforq
        d = self.difficulty
        self.maths = Mathop(qt, d)
    # determines type of question to be used from selection
        if self.questiontype=='Addition': self.question_used(self.maths.addition(),page,' + ')
        elif self.questiontype=='Times': self.question_used(self.maths.multiplication(),page,' x ')
        elif self.questiontype=='Division': self.question_used(self.maths.division(),page,' ÷ ')
        elif self.questiontype=='Subtraction': self.question_used(self.maths.subtraction(),page,' - ')
    # Stringing together the answers
        self.qanswers = (self.qtext + str(self.maths.a)) 
        self.student.questionlist.append(self.qanswers) 
        print(self.student.questionlist)
        print(len(self.student.questionlist))

    def question_used(self, qt, page, smbl):
        self.questiontypeforq = qt
        self.qtext = (str(self.maths.n2) + smbl + str(self.maths.n) + ' = ')
        self.question = Label(page, text=self.qtext, font=self.qsize, fg=self.color[0], bg=self.color[1])
        self.question.grid(row=2, column=0, padx=(0,180))


######################################## PAGE 3-13 #######################################
#################################### 10 Question Pages ###################################


    def questions(self):
        self.page = Frame(root, bg=self.color[1])
        self.formatting(self.page)
        self.page.config(padx=(0))

    # Question title
        Label(self.page,text="Question {}".format(self.f), bg=self.color[1], fg=self.color[4], 
              font= self.title_size).grid(row=1,pady=(0,50))
    
    # Answer text box
        self.answer = Entry(self.page,font=self.qsize, bg=self.color[4], fg=self.color[0], border=0, 
                            highlightbackground=self.color[4], highlightthickness=5,width=5)
        self.answer.grid(row=2,padx=(250,0))
    
    # Next button hidden under check button
        self.nextb(self.page,lambda:[self.question_number(),self.next_page(self.page),self.questions()])
        self.n.grid(row=4,column=1,pady=(80,0))

    # Check button
        self.checkb = Button(self.page, command=lambda:[self.checkanswer(self.page)], text="Check",
                             fg=self.color[0],bg=self.color[2], border=0, height=1, width=8)
        self.checkb.grid(row=4,column=1,pady=(80,0))

    # determines type of question to be used in the rest of the 10 questions (responsible for printing questions)
        self.questiontypeforquestions(self.page)

    # Every time 'Next' is pressed, question function is called until f=10 frames 
        if self.f == 11:
            self.next_page(self.page)
            self.results()

# Function for adding to f after 'next' button is pressed
    def question_number(self):
        self.f=self.f+1

# removes 'check' button to reveal the 'next' button that takes to the next page
    def remove_check(self):
        self.checkb.grid_remove()

# check whether answer was correct, incorrect, or invalid
    def checkanswer(self,page):
        checknum = True

    # Check input, return error if string
        try:
            self.ans = int(self.answer.get())
        except ValueError:
            messagebox.showerror(title='Error',message='Please enter a number in the box')
            checknum = False

    # Check input if correct/incorrect to answer
        if checknum == True:
            if int(self.ans) == self.maths.a: # Correct
                Label(page,text="Correct!",fg=self.color[2],bg=self.color[1],font=self.msg_size).grid(row=3,pady=(10,0))
                self.answer.configure(bg=self.color[2]) # Turn answer entry box green
            # Add to correct answer list to calculate score
                self.student.correct_answers.append(self.ans) 
            # Tick symbol added
                Label(self.page,text='✔',fg=self.color[2],font=self.symbl_size,bg=self.color[1]).grid(row=2,column=1) 
                self.remove_check()

            if int(self.ans) != self.maths.a: # Incorrect
                Label(page,text="Incorrect, the answer is {}".format(self.maths.a),fg=self.color[3],bg=self.color[1],
                      font=self.msg_size).grid(row=3,pady=(10,0))
                self.answer.configure(bg=self.color[3]) # Turn answer entry box red
            # Cross symbol added
                Label(self.page,text='✘',fg=self.color[3],bg=self.color[1],font=self.symbl_size).grid(row=2,column=1) 
                self.remove_check()

######################################## PAGE 14 #######################################
##################################### Results Page #####################################

    def results(self):
        self.results_page = Frame(root, bg=self.color[1])
        self.formatting(self.results_page)
        self.results_page.grid_configure(padx=(0))
        self.student.score = len(self.student.correct_answers)

    # Question title
        Label(self.results_page,text="Results\n{} on {} Difficulty".format(self.questiontype,
              self.difficulty),fg=self.color[4], bg=self.color[1], font='CenturyGothic 35 bold').grid(row=1)

    # Results subheader- Header message changes depending on the score!
        if self.student.score > 4:
            Label(self.results_page,text="Good job {}, you got {}/10 answers correct".format
                 (self.student.student_name,self.student.score),fg=self.color[0],bg=self.color[1]).grid(row=2,pady=(0,50))
        elif self.student.score < 5:
            Label(self.results_page,text="Practice makes perfect {},\nyou got {}/10 answers correct"
                 .format(self.student.student_name,self.student.score),fg=self.color[0],bg=self.color[1]).grid(row=2)

    # Next button
        self.nextb(self.results_page,lambda:[self.student.store(),self.next_page(self.results_page),self.leaderboard()])
        self.n.grid(row=3,sticky=E,pady=(10,0))
    # Answers button
        self.ansb = Button(self.results_page, text='Answers✔', bg=self.color[2], fg=self.color[0], border=0, highlightthickness=5,
        command=lambda:[self.next_page(self.results_page),self.answers()])
        self.ansb.grid(row=0,sticky=W)

########################################################################################
###################################### Answers Page ####################################

    def answers(self):
        self.answers_page = Frame(root, bg=self.color[1])
        self.formatting(self.answers_page)
        self.answers_page.config(padx=0)
    # Title
        Label(self.answers_page,text="Answers",fg=self.color[4], bg=self.color[1],
              font=self.qsize).grid(row=0,column=2)
        i = 0
        r = 0
        c = 0
        p = 0
        for i in range(10):
            t = self.student.questionlist[i]
            r = r + 1
            l = Label(self.answers_page, text=t, fg=self.color[5], bg=self.color[1], font=self.msg_size)
            l.grid(row=r, column=c+1, padx=p)
            if r == 5:
                c = 3
                r = 0
            if c == 3: p = (0,150)

    # Back button
        Button(self.answers_page, text=' Back ', bg=self.color[4], fg=self.color[0], border=0, highlightthickness=5,
               command=lambda:[self.next_page(self.answers_page),self.results()]).grid(sticky=SE,column=2,padx=(0,50))

######################################## PAGE 15 #######################################
#################################### Leaderboard Page ##################################

    def leaderboard(self):
        self.leaderboard_page = Frame(root, bg=self.color[1])
        self.formatting(self.leaderboard_page)
        self.leaderboard_page.grid_configure(padx=(0))
    # Title
        Label(self.leaderboard_page,text="Leaderboard",fg=self.color[4], bg=self.color[1],
              font=self.qsize).grid(row=0,column=1)
        Label(self.leaderboard_page,text="{} on {} difficulty".format(self.questiontype, 
              self.difficulty),fg=self.color[0], bg=self.color[1],font=self.msg_size).grid(row=1,column=1)

    # New frame for leaderboard to prevent irregular spacing of the entry widgets
        self.leaderboard_frame = Frame(root,bg=self.color[1]) 
        self.formatting(self.leaderboard_frame)
        self.leaderboard_frame.grid_configure(padx=(0))
        self.user_row = 0 
        for r in range(2,8): # iteration for rows (6)
            for c in range(3): # iteration for columns(3) 
                e = Entry(self.leaderboard_frame, justify='center', font='CenturyGothic 18 bold', 
                               width=12, border=0, highlightbackground="#d9d9d9", highlightthickness=5)
                e.grid(row=r, column=c+1, pady=2, padx=2)
                e.insert(END, self.student.leaderboard_data[r][c]) 

            # getting each entry's input. 
                getted = e.get()
            # if it detects current user's name, their row is saved to variable
                if getted == self.student.student_name:
                    self.user_row = int(e.grid_info()['row'])
            # set leaderboard entries to read-only
                e.config(state=DISABLED, disabledbackground='#d9d9d9', disabledforeground=self.color[0])
            # Colouring the header dark grey
                if r == 2: 
                    e.config(disabledbackground=self.color[0], highlightbackground=self.color[0], disabledforeground=self.color[1])
            # colouring current user's rows green (all rows with same name)
                if r == self.user_row:
                        e.config(disabledbackground=self.color[5], highlightbackground=self.color[5], disabledforeground=self.color[1])

    # restart button
        self.restartb = Button(self.leaderboard_frame, text="Restart", fg=self.color[0], bg=self.color[2], border=0, height=1, width=8, command= lambda:[
                               self.student.reset_var(),self.next_page(self.leaderboard_page), self.next_page(self.leaderboard_frame), self.selection()])
        self.restartb.grid(row=8,column=0,sticky=E, pady=(30,10))
    # logout button
        self.logoutb = Button(self.leaderboard_frame, text="Log out", fg=self.color[0], bg=self.color[4], border=0, height=1, width=8, 
                              command= lambda:[self.student.reset_var(), self.student.reset_user(), self.next_page(self.leaderboard_page),
                                               self.next_page(self.leaderboard_frame), self.__init__()])
        self.logoutb.grid(row=8,column=4,sticky=W, pady=(30,10))

Interface()
root.mainloop() 