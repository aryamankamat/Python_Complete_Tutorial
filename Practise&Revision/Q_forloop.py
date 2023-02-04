"""
Write a program to create a list and print the values which are number and greater then 6
"""

list = [12, 1, 44, 21, 2, 3, 4, 54, 5, "Apple", "Hey", 33, 54.4]
for var in list:
    if str(var).isnumeric() and var > 6:
        print(var)
