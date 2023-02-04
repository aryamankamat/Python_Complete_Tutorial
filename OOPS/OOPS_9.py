class Student():
    __college = "ICCS"
    
    def setData(self):
        self.__roll = 101
        self.name = 'ABC'

s1 = Student()
s1.setData()
print("NAME = ", s1.name)
# print("ROLL = ", s1.__roll) #ERROR
print("ROLL = ", s1._Student__roll)
print("Attributes = ", s1.__dict__)
# print("College ::",s1.__college) #ERROR
print(Student.__dict__)
