import math

"""
Write a python program to create a class Circle and Compute the Area and the
circumferences of the circle. (use parameterized constructor) 
"""


class Circle:

    def __init__(self, r):
        self.r = r
        return

    def Area_of_circle(self):
        area = (math.pi * (self.r ** 2))
        print(f"The area of circle for radius {self.r} is = {area:.2f}")
        return

    def Circum_of_circle(self):
        circum = 2 * (math.pi * self.r)
        print(f"The Circumference of circle for radius {self.r} is = {circum:.2f}")
        return


c1 = Circle(12.22)
c1.Area_of_circle()
c1.Circum_of_circle()
print()
c2 = Circle(14.33)
c2.Area_of_circle()
c2.Circum_of_circle()
