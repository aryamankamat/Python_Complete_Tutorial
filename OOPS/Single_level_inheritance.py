#Public data Members
"""
class Human():

    def __init__(self):
        self.name = input("Enter your name = ")
        self.gender = input("Enter your Gender = ")

class Student(Human):
    college = "ICCS"

    def __init__(self):
        super().__init__()
        self.roll = int(input("Enter your roll number = "))
        self.per = float(input("Enter your percentage = "))

    def printData(self):
        print(self.roll,self.name,self.gender,self.per,Student.college)


s1 = Student()
# print("Availabe attribute of s1 = ", s1.__dict__)
print("Roll  Name  Gender  Percentage  College")
s1.printData()

"""

#Private Data Members
class Human():

    def __init__(self):
        self.__name = input("Enter your name = ")
        self.__gender = input("Enter your Gender = ")

    def get_name(self):
        return self.__name

    def get_gender(self):
        return self.__gender

class Student(Human):
    __college = "ICCS"

    def __init__(self):
        super().__init__()
        self.__roll = int(input("Enter your roll number = "))
        self.__per = float(input("Enter your percentage = "))

    def printData(self):
        print(self.__roll, self.get_name(), self.get_gender(), self.__per, Student.__college)


s1 = Student()
# print("Availabe attribute of s1 = ", s1.__dict__)
print("Roll  Name  Gender  Percantage  College")
s1.printData()