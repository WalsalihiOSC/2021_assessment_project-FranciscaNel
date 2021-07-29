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
        self.questiontypes = [] 
        #self.questiontypes = qt

        self.qtypes = ['Addition +','Subtraction -','Times x','Division ÷']

    # These variables would be for recording the personal leaderboard
        #self.student_attempts = len(self.scores_list)
        #self.scores_list = []