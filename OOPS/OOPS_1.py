class Student:
    '''This is sample class for the demonstration'''
    pass 
    
s1 = Student()

print("Type of s1 = ", type(s1))
print("Is s1 instance of the Student?", isinstance(s1,Student))
print("Is s1 instance of the object?", isinstance(s1,object))
    
print("Available attributes of s1 = ", s1.__dict__)

print("Accessible attributes of s1 = \n",dir(s1))

print("Available attributes of object = \n ", object.__dict__)

print("Available attributes of Student = \n ", Student.__dict__)





