class Circle():

    def __init__(self):
        print("Constructor called...")
        self.radius = float(input("Enter the radius of a circle = "))
        self.area = None

    def CalcArea(self):
        self.area = 3.14 * (self.radius ** 2)
        print("Area of circle is = {}".format(round(self.area,2)))


c1 = Circle()
c1.CalcArea()