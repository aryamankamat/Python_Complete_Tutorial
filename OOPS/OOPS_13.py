class Student():

    def __init__(self):
        self.__roll = None
        self.__name = None
        self.__city = None
        return
        
    
s1 = Student()
s2 = Student()
s3 = Student()
print("Attributes s1 = ", s1.__dict__)
print("Attributes s2 = ", s2.__dict__)
print("Attributes s3 = ", s3.__dict__)


