
import math

def Area_of_circle(r):
    '''This function is accepting a radius to calculate the area of a circle.'''
    area = math.pi * (r ** 2)
    return area

r = float(input("Enter the radius of circle = "))
area  = Area_of_circle(r)
print(f"The Area of circle is = {round(area,2)}")
print("The Area of circle is = {:.2f}".format(area))