class Rectangle:

    def __init__(self):
        self.length = float(input("Enter lenght of a rectangle ="))
        self.width = float(input("Enter width of a rectangle = "))

    def area(self):
        print(f"The area of rectangle is = {round((self.length * self.width), 2)}")

    def perimeter(self):
        print(f"The perimeter of rectangle is = {2 * (self.length + self.width):.2f}")


r1 = Rectangle()
r1.area()
r1.perimeter()
