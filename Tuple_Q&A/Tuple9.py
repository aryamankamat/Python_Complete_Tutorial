"""
Write a Python program to check whether an element exists within
a tuple.
"""
tup = 2, 4, 5, 6, 2, 3, 7

n = int(input("Enter a number to check it's existance : "))
if n in tup:
    print("The element present in the tuple.")
else:
    print("The element is not present in the tuple.")
