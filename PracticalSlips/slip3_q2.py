class Calc:
    def __init__(self, x, y):
        self.a = x
        self.b = y

    def add(self):
        return self.a + self.b

    def sub(self):
        return self.a - self.b

    def mul(self):
        return self.a * self.b

    def div(self):
        return self.a / self.b


a = int(input("Enter first number = "))
b = int(input("Enter second number = "))

c1 = Calc(a, b)
ch = 0
while True:
    print("0. Exit")
    print("1. Add")
    print("2. Subtraction")
    print("3. Multiplication")
    print("4. Division")
    ch = int(input("Enter your choice: "))

    if ch == 1:
        print("\n Addition is = ", c1.add(), "\n")

    elif ch == 2:
        print("\n Subtraction is = ", c1.sub(), "\n")

    elif ch == 3:
        print("\n Multiplication is = ", c1.mul(), "\n")

    elif ch == 4:
        print("\n Division is = ", c1.div(), "\n")

    elif ch == 0:
        print("\n Terminated \n")
        exit()
