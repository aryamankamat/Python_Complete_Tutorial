"""
Write a Python function that takes two lists and returns **True**
if they have at least one common member.(Using SET and without using
SET)
"""
lst1 = [1, 2, 3, 4, 5]
lst2 = [5, 6, 7, 8, 9]

flag = 0

for i in lst1:
    for j in lst2:
        if (i == j):
            flag = 1

if (flag == 1):
    print("True")
else:
    print("False")
