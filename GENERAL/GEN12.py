"""
12. Write a Python program to find x raise to y.
(Assume x and y as integers and do not use exponentiation operator).
"""
# Logic 1
"""
import math

x = int(input("Enter the value of x = "))
y = int(input("Enter the value of y = "))
ans = math.pow(x, y)  # logic 1
print("The", x, "raise to", y, "is = ", ans)
"""

# Logic 2
"""
x = int(input("Enter the value of x = "))
y = int(input("Enter the value of y = "))
result = 1
while (y != 0):
    result = result * x
    y = y - 1
print("The", x, "raise to", y, "is = ", result)
"""

# Logic 3
"""
x = int(input("Enter the value of x = "))
y = int(input("Enter the value of y = "))
result = 1
for y in range(y, 0, -1):
    result = result * x
print("The", x, "raise to", y, "is = ", result)
"""
