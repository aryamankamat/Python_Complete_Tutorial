"""
Write a Python program to check if the given list is in Ascending Order or not.
"""

lst = [1, 4, 5, 8, 10]
flag = 0
i = 1
while (i < len(lst)):
    if (lst[i] < lst[i-1]):
        flag = 1

    i = i + 1

# if (flag == 0):
if (not flag):

    print("Yes, List is sorted.")

else:

    print("No, List is not sorted.")
