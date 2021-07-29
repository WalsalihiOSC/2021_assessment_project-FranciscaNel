# CSC3 2021
# Ormiston Computing Student Class
# Francisca Nel
# Ver 1

class Student:
    def __init__(self,sn):

    # defining (possible) variables for the student instance
        self.student_name = sn
        #self.student_score = ss
        #self.student_attempts = sa
        self.selected_questiontype = [] 
        self.selected_difficulty = []
        #self.questiontypes = qt

        self.qtypes = ['Addition +','Subtraction -','Times x','Division ÷']
        self.difficulties = ['Easy','Intermediate','Hard']

    # These variables would be for recording the personal leaderboard
        #self.student_attempts = len(self.scores_list)
        #self.scores_list = []

