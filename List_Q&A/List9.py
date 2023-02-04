"""
Write a Python program to multiplies all the items in a list.

**Sample Input:** lst = \[3, 2, -1, 5, -4\]

**Output :** Multiplication = 120
"""
lst = [3, 2, -1, 5, -4]
mul = 1
for i in lst:
    mul = mul * i
print(f"Multiplication of {lst} is = {mul}")
