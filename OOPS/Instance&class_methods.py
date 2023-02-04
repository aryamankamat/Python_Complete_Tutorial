class Student():

    college = "ICCS"    #class level attribute

    def __init__(self,m1,m2,m3):
        self.m1 = m1
        self.m2 = m2
        self.m3 = m3

    def avg(self):
        return (self.m1+self.m2+self.m3)/3

    #There are two types of instance level methods
    #1)Accessors:- Used to fetch the existing values.
    def get_m1(self):
        return self.m1
    #2)Mutators:- Used to change the assigned values to exisiting variables.
    def set_m2(self):
        self.m2 = 100
        #print(self.m2,self.m1,self.m3)

    #class Method
    @classmethod
    def get_college(cls):
        return cls.college

    #Static Method
    @staticmethod
    def info():
        print("This is class Student, created for the demonstration of class methods and instance methods.")


s1 = Student(66,77,88)
s2 = Student(68,72,80)
# print(s1.avg())
# print(s2.avg())

# print(s1.get_m1())
# print(s1.set_m2())

# print(Student.get_college())

# Student.info()    #static Method