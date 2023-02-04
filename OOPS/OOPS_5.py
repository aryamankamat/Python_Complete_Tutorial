#WAY-2: Setting the attributes to the object/class from outside the class and accessing them from within the class 

class Student():
    college = 'ICCS'
    def show(self):
        #print(self.roll, self.name, self.college)
        print(self.roll, self.name, Student.college)

s1 = Student()
s2 = Student()
print("BEFORE :", s1.__dict__)
print("BEFORE :", s2.__dict__)
s1.roll = 101
s1.name = 'ABC'
s2.roll = 105
s2.name = 'XYZ'
print("AFTER :", s1.__dict__)
print("AFTER :", s2.__dict__)

print("SUMMARY")
print("Roll Name College")
print("===========")
s1.show()
s2.show()
