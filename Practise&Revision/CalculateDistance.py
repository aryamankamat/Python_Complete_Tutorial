"""
Given two points, the formula for computing the distance is 0.5**(x 2 - x 1 )**2 + (y2 - y1)**2
You can use a ** 0.5 to compute. The program prompts the user to enter the coordinates of the first point and the
second point 
"""
#Enter the 1st point with two float values.
x1,y1 = eval(input("Enter x1 and y1 for point1 : "))
#Enter the 2nd point with two float values.
x2, y2 = eval(input("Enter x2 and y2 for point2 : "))

#distance = ((x1 - x2) * (x1 - x2) + (y1 - y2) * (y1 - y2)) ** 0.5
distance = (((x1 - x2) **2) + ((y1 - y2) ** 2)) ** 0.5
print("The distance between two points is = ",distance)
