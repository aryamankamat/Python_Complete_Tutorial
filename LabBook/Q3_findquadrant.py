"""
3.Write python script to accept the x and y coordinate of a point and find the quadrant in which the point lies.

Quadrant 1: x is negative and y is positive
Quadrant 2: Both x and y are positive
Quadrant 3: Both x and y are negative
Quadrant 4: x is positive and y is negative
"""

x = int(input("Enter the x co-ordinate : "))
y = int(input("ENter the y-cordinate : "))
if(x<0) and (y>0):
    print("Belongs to 1st quadrant...")
elif(x>0) and (y>0):
    print("Belongs to 2nd quadrant...")
elif(x<0) and (y<0):
    print("Belongs to 3rd quadrant...")
else:
    print("Belongs to 4th quadrant...")
