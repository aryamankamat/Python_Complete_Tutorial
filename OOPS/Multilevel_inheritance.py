class Student():

    def __init__(self):
        self.roll = int(input("Enter the roll number = "))
        self.name = input("Enter the name = ")

class Exam(Student):

    def __init__(self):
        super().__init__()
        self.phy = int(input("Enter the marks of physics = "))
        self.chem = int(input("Enter the marks of chemistry = "))
        self.maths = int(input("Enter the marks of Maths = "))

class Result(Exam):

    def __init__(self):
        super().__init__()
        self.per = None
        self.grade = None

    def calResult(self):
        self.per = (self.phy + self.chem + self.maths)//3

        if self.per > 70:
            self.grade = "O"
        elif self.per >= 60 and self.per < 70:
            self.grade = "A"
        elif self.per >= 50 and self.per < 60:
            self.grade = "B"
        elif self.per >= 40 and self.per < 50:
            self.grade = "C"
        else:
            self.grade = "D"

    def printMarksheet(self):

        print(self.roll, self.name, self.phy, self.chem, self.maths, round(self.per,2), self.grade)

r1 = Result()
r1.calResult()
print("ROll Name  Physics Chemistry Maths  percentage Grade")
r1.printMarksheet()


