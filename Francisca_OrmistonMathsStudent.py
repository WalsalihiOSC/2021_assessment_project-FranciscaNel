# CSC3 2021
# Ormiston Computing Student Class
# Francisca Nel
# Ver 10

class Student:
    def __init__(self,sn):
        self.student_name = sn
    # storing questiontype/difficulty  
        self.selected_questiontype = [] 
        self.selected_difficulty = []
        self.questionlist = [] # Used later for printing all answers
    # store incorrect answers and correct answers for the scores
        self.correct_answers = []
        self.score = 0
    # question types and difficulties
        self.qtypes_smbl = ['Addition\n➕','Times\n✖','Division\n➗','Subtraction\n▬']
        self.qtypes = ['Addition','Times','Division','Subtraction']
        self.difficulties = ['Easy','Intermediate','Hard']
        
    # 12! text! files! for each question type and difficulty 
        self.file_paths = [
        "Text_Files\Addition_easy.txt", "Text_Files\Addition_intermediate.txt", "Text_Files\Addition_hard.txt", 
        "Text_Files\Subtraction_easy.txt", "Text_Files\Subtraction_intermediate.txt", "Text_Files\Subtraction_hard.txt",
        "Text_Files\Times_easy.txt", "Text_Files\Times_intermediate.txt", "Text_Files\Times_hard.txt",
        "Text_Files\Division_easy.txt", "Text_Files\Division_intermediate.txt", "Text_Files\Division_hard.txt"]

# Functions for storing info to file depending on difficulty
    def store_addition(self):
            if self.selected_difficulty[0] == 'Easy': self.writef(0)
            elif self.selected_difficulty[0] == 'Intermediate': self.writef(1)
            elif self.selected_difficulty[0] == 'Hard': self.writef(2)
    def store_subtraction(self):
            if self.selected_difficulty[0] == 'Easy': self.writef(3)
            elif self.selected_difficulty[0] == 'Intermediate': self.writef(4)
            elif self.selected_difficulty[0] == 'Hard': self.writef(5)
    def store_multiplication(self):
            if self.selected_difficulty[0] == 'Easy': self.writef(6)
            elif self.selected_difficulty[0] == 'Intermediate': self.writef(7)
            elif self.selected_difficulty[0] == 'Hard': self.writef(8)
    def store_division(self):
            if self.selected_difficulty[0] == 'Easy': self.writef(9)
            elif self.selected_difficulty[0] == 'Intermediate': self.writef(10)
            elif self.selected_difficulty[0] == 'Hard': self.writef(11)

    def store(self):
        if self.selected_questiontype[0] == 'Addition': self.store_addition()
        elif self.selected_questiontype[0] == 'Times': self.store_multiplication()
        elif self.selected_questiontype[0] == 'Division': self.store_division()
        elif self.selected_questiontype[0] == 'Subtraction': self.store_subtraction()

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
        # prevent index error by filling in empty tuples until 5 elements in list
            if len(content) > 5:
                self.high_scores = content[0:5]
            else:
                self.high_scores = content
                while len(self.high_scores) < 5:
                    self.high_scores.append(('',''))       
            print(self.high_scores)
        # ... converting the high scores to seperate lists ...
            self.lscores = [i[1] for i in self.high_scores]
            self.lnames = [i[0] for i in self.high_scores]

        # The leaderboard data
            self.leaderboard_data = ["placeholder","placeholder",
                                    ("Name", "Score", "Place"),
                                    ((self.lnames[0]),self.lscores[0],"1st"),
                                    ((self.lnames[1]),self.lscores[1],"2nd"),
                                    ((self.lnames[2]),self.lscores[2],"3rd"),
                                    ((self.lnames[3]),self.lscores[3],"4th"),
                                    ((self.lnames[4]),self.lscores[4],"5th")]

# Resetting student data for restart
    def reset_var(self):
        self.selected_questiontype = []
        self.selected_difficulty = []
        self.correct_answers = []
        self.score = None

# Resetting user name for logging out
    def reset_user(self):
        self.student_name = None
