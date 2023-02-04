from abc import ABC, abstractmethod
import math


class Shape(ABC):

    @abstractmethod
    def area(self):
        pass

    @abstractmethod
    def volume(self):
        pass


class Square(Shape):

    def __init__(self):
        self.s = float(input("Enter the side of a square = "))

    def area(self):
        print(f"The area of square is = {(self.s ** 2):.2f}")

    def volume(self):
        print(f"The volume of square is = {(self.s ** 3):.2f}")


class Circle(Shape):

    def __init__(self):
        self.r = float(input("Enter the radius of a circle = "))

    def area(self):
        print(f"The area of Circle is = {(math.pi * (self.r ** 2)):.2f}")

    def volume(self):
        print(f"The volume of Circle is = {((4 / 3 * (math.pi * self.r)) ** 3):.2f}")


print("Square details is displayed below...")
s1 = Square()
s1.area()
s1.volume()
print()
print("Circle details is displayed below...")
c1 = Circle()
c1.area()
c1.volume()
