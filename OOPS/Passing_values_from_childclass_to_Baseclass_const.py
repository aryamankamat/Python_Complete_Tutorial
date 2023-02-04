class Human():

    def __init__(self,n,g):
        self.name = n
        self.gender = g

class Student(Human):
    college = "ICCS"

    def __init__(self,r,n,g,p):
        super().__init__(n,g)
        self.roll = r
        self.per = p

    def printData(self):
        print(self.roll,self.name,self.gender,self.per,Student.college)


s1 = Student(15,"Aryaman","Male",99.9)
# print("Availabe attribute of s1 = ", s1.__dict__)
print("Roll  Name  Gender  Percantage  College")
s1.printData()