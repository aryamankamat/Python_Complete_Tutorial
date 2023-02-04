class Student(object):

    def __init__(self):
        self._name = input("Enter a Name = ")
        self.marks = float(input("Enter Student marks = "))

    def display(self):
        print(self._name, self.marks)

    def setValues(self):
        self._name = "Python"
        self.marks = 3.11


s1 = Student()
print("Original values are displayed below...")
print("Name  Marks")
s1.display()
print()
s1.setValues()
print("Updated values are displayed below...")
print("Name  Marks")
s1.display()
