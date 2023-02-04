
class Student:
    roll = 101     #By default, these are the class level attributes
    name = "ICCS"
    
s1 = Student()
# print("Available attributes for s1 =", s1.__dict__)

# print("BFORE : Available attributes for Student =", Student.__dict__)

# print("Accessible attributes for s1 =", dir(s1))

# del s1.roll
# print("Accessible attributes for s1 =", dir(s1))
# del Student.roll
# print("Accessible attributes for s1 =", dir(s1))

# print("AFTER : Available attributes for Student =", Student.__dict__)





