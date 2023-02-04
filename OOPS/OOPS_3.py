#WAY - 1 Setting the attributes to the objects/class from outside the class and printing/accessing them from outside the class 

class Student():
    college = "ICCS"   #class Level attribute
    
s1 = Student()
s2 = Student()
print("BEFORE : Available attributes of s1 ::", s1.__dict__)
print("BEFORE : Available attributes of s2 ::", s2.__dict__)
#setting instance level attributes
s1.roll = 101
s1.name = 'ABC'

s2.roll = 106
s2.name = 'PQR'
s2.per = 7.8

print("AFTER : Available attributes of s1 ::", s1.__dict__)
print("AFTER : Available attributes of s2 ::", s2.__dict__)

print("BEFORE : Available attributes of Student ::", Student.__dict__)

#setting class level attributes
Student.city = 'Pune'
Student.state = 'MH'
Student.college = 'ICACS'

print("AFTER : Available attributes of Student ::", Student.__dict__)


print("SUMMARY")
print("Roll Name Percentage")
print("======================")
# print(s1.roll,s1.name,s1.per) #ERROR
print(s1.roll,s1.name)
print(s2.roll,s2.name, s2.per)


