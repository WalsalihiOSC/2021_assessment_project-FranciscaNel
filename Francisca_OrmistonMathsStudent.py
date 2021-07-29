# CSC3 2021
# Ormiston Computing Student Class
# Francisca Nel
# Ver 1

class Student:
    def __init__(self,sn):
    # defining (possible) variables for the student instance
        self.student_name = sn
    # Lists for storing questiontype/difficulty temporarily to check if selection < 1
        self.selected_questiontype = [] 
        self.selected_difficulty = []
    # Lists to store all attempted question types and difficulties from a user.
        self.selected_questiontypes = [] 
        self.selected_difficulties = []
    # Lists to store incorrect answers and correct answers for the scores
        self.incorrect_answers = []
        self.correct_answers = []
        self.scores = []
    # Lists for question types and difficulties
        self.qtypes = ['Addition +','Times x','Division ÷','Subtraction -']
        self.difficulties = ['Easy','Intermediate','Hard']
