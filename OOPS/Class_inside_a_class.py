#Inner Class
#In order to execute the inner class we have to create the object of it inside the outter class or outside of outter class using outter class name and inner class constructor.

class Student():#Outter class

    def __init__(self,name,r):
        self.name = name
        self.roll = r
        self.l = self.Laptop() #Object of Inner class

    def show(self):
        print(self.name,self.roll)
        self.l.show() #calling the inner class method

    class Laptop():#inner class

        def __init__(self):
            self.brand = "HP"
            self.cpu = "i5"
            self.ram = 16

        def show(self):
            print(self.brand, self.cpu,self.ram)



s1 = Student("ABC",101)
s2 = Student("XYZ",102)
print("SUMMARY")
print("NAME ROLL")
s1.show()

#In order to access the inner class attributes
# print(s1.l.brand)

#In case we want to create another object of class Laptop
# lap1 = s1.l #For every Student class object you will get different Laptop object
# lap2 = s2.l
# print(id(lap1))
# print(id(lap2))

# lap1 = Student.Laptop() #Object of Inner class
# lap1.show()

