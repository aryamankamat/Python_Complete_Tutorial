class Demo(object):

    def getString(self):
        self.s = input("Enter a string = ")

    def printString(self):
        print("Original String is = ", self.s)
        print("Updated String is = ", self.s.upper())


d1 = Demo()
d1.getString()
d1.printString()
