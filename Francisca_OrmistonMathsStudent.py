# CSC3 2021
# Ormiston Computing Student Class
# Francisca Nel
# Ver 9

class Student:
    def __init__(self,sn):
        self.student_name = sn
    # storing questiontype/difficulty  
        self.selected_questiontype = [] 
        self.selected_difficulty = []
    # store incorrect answers and correct answers for the scores
        self.correct_answers = []
        self.score = 0
    # question types and difficulties
        self.qtypes = ['Addition','Times','Division','Subtraction']
        self.difficulties = ['Easy','Intermediate','Hard']

        self.high_scores = []

                    # Addition
        self.file_paths = ["Text_Files\Addition_easy.txt", "Text_Files\Addition_intermediate.txt", "Text_Files\Addition_hard.txt", 
                    # Subtraction
                           "Text_Files\Subtraction_easy.txt", "Text_Files\Subtraction_intermediate.txt", "Text_Files\Subtraction_hard.txt",
                    # Multiplication
                           "Text_Files\Times_easy.txt", "Text_Files\Times_intermediate.txt", "Text_Files\Times_hard.txt",
                    # Division
                           "Text_Files\Division_easy.txt", "Text_Files\Division_intermediate.txt", "Text_Files\Division_hard.txt"]

# Functions for storing info to file (I should be able to simplify these later)
    def store_addition(self):
            if self.selected_difficulty[0] == 'Easy':
                self.writef(0)
            elif self.selected_difficulty[0] == 'Intermediate':
                self.writef(1)
            elif self.selected_difficulty[0] == 'Hard':
                self.writef(2)
    def store_subtraction(self):
            if self.selected_difficulty[0] == 'Easy':
                self.writef(3)
            elif self.selected_difficulty[0] == 'Intermediate':
                self.writef(4)
            elif self.selected_difficulty[0] == 'Hard':
                self.writef(5)
    def store_multiplication(self):
            if self.selected_difficulty[0] == 'Easy':
                self.writef(6)
            elif self.selected_difficulty[0] == 'Intermediate':
                self.writef(7)
            elif self.selected_difficulty[0] == 'Hard':
                self.writef(8)
    def store_division(self):
            if self.selected_difficulty[0] == 'Easy':
                self.writef(9)
            elif self.selected_difficulty[0] == 'Intermediate':
                self.writef(10)
            elif self.selected_difficulty[0] == 'Hard':
                self.writef(11)

# Function that writes to file and produces list to be used for displaying high scores
    def writef(self,i):
        with open(self.file_paths[i],"a") as f:
            f.write("{} {}\n".format(self.student_name, self.score))
            f.close()
        with open(self.file_paths[i],"r") as f:
            c = f.readlines() 
        # splits the list into a tuple for the leaderboard
            content = [tuple(line.strip().split()) for line in c] 
        # Sort the text file converted to list into 5 highest scores
            content.sort(key=lambda x : int(x[1])) # sorts from index 1 of tuple
            content.reverse()
            print(content)
        # prevent index error by filling in empty tuples until 5 elements in list
            if len(content) > 5:
                self.high_scores = content[0:5]
            else:
                self.high_scores = content
                while len(self.high_scores) < 5:
                    self.high_scores.append(('',''))       
                print(self.high_scores)

    def store(self):
        if self.selected_questiontype[0] == 'Addition': self.store_addition()
        elif self.selected_questiontype[0] == 'Times': self.store_multiplication()
        elif self.selected_questiontype[0] == 'Division': self.store_division()
        elif self.selected_questiontype[0] == 'Subtraction': self.store_subtraction()

# Resetting all variables for restart
    def reset_var(self):
        self.selected_questiontype = []
        self.selected_difficulty = []
        self.correct_answers = []
        self.score = None
# Resetting user name for logging out
    def reset_user(self):
        self.student_name = None
