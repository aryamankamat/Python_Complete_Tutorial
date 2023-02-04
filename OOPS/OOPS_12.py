class Student():

    def __init__(self,r,n,c):
        print("Constructor called...")
        self.roll = r
        self.name = n
        self.city = c
        return
        
    
s1 = Student(101,'Sindhu','Vizag')
print("Attributes = ", s1.__dict__)
# Student.__init__(s1,101,'Sindhu','Vizag') 
