class Student():
    __college = "ICCS"
    
    def setData(self):
        self.__roll = 101
        self.name = 'ABC'

    def putData(self):
        print(self.__roll,self.name,Student.__college)

s1 = Student()
s1.setData()
s1.putData()