# CSC3 2021
# Ormiston Computing Math operations class
# Francisca Nel
# Ver 1

import random

# question types and difficulty specifications
class Mathop:
    def __init__(self,qt,d):
        self.questiontypeforq = qt
        self.difficulty = d

    def addition(self):
        if self.difficulty == 'Easy':
            self.n = random.randint(1,3)
            self.n2 = random.randint(0,3)
        elif self.difficulty == 'Intermediate':
            self.n = random.randint(0,10)
            self.n2 = random.randint(1,5)
        elif self.difficulty == 'Hard':
            self.n = random.randint(5,15)
            self.n2 = random.randint(1,15)
        self.a = int(self.n + self.n2)

    def multiplication(self):
        if self.difficulty == 'Easy':
            self.n = random.randint(0,5)
            self.n2 = random.randint(1,2)
        elif self.difficulty == 'Intermediate':
            self.n = random.randint(0,5)
            self.n2 = random.randint(1,5)
        elif self.difficulty == 'Hard':
            self.n = random.randint(0,12)
            self.n2 = random.randint(1,12)
        self.a = int(self.n * self.n2)

    def division(self):
        if self.difficulty == 'Easy':
            self.n = random.randint(1,3)
            self.n2 = self.n*(random.randint(1,3)) 
        elif self.difficulty == 'Intermediate':
            self.n = random.randint(1,5)
            self.n2 = self.n*(random.randint(1,5))
        elif self.difficulty == 'Hard':
            self.n = random.randint(1,5)
            self.n2 = self.n*(random.randint(1,10))
        self.a = int(self.n2/self.n)
    
    def subtraction(self):
            if self.difficulty == 'Easy':
                self.n2 = random.randint(1,5)
                self.n = random.randint(self.n2,5)
            elif self.difficulty == 'Intermediate':
                self.n2 = random.randint(1,5)
                self.n = random.randint(self.n2,10)
            elif self.difficulty == 'Hard':
                self.n2 = random.randint(1,10)
                self.n = random.randint(self.n2,15)
            self.a = int(self.n - self.n2)
        