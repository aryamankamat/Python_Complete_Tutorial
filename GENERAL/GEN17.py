"""
Write a Python program to create the multiplication table (from 1
to 10) of a number.

Expected Output:
Input a number: 8
8 x 1 = 8
8 x 2 = 16
8 x 3 = 24
.
.
.
8 x 10 = 80
"""
n = int(input("Enter a number : "))
for i in range(1, 11):
    print(f"{n} X {i} = {n*i}")
