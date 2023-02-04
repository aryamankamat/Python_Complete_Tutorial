"""
(Compute the volume of a cylinder) Write a program that reads in the radius and
length of a cylinder and computes the area and volume using the following formulas:
area = radius * radius * π
volume = area * length
"""
import math
r = float(input("Enter the radius of a cylinder : "))
l = float(input("Enter the lenght of a cylinder : "))

area = (r * r * math.pi)
print("The are of Cylinder is = %.4f " % area)
volume = area * l
print("The volume of cylinder is = %.2f " % volume)
