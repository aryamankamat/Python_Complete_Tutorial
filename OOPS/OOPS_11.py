class Student():

    def __init__(self):
        print("Constructor called...")
        print("ID of self = ", id(self))
        return
        
    
s1 = Student()  # Student.__init__(s1)
print("ID of s1 = ", id(s1))
#s2 = Student()
#s3 = Student()
#Student()
#Student()