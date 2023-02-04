"""
Write a Python program to count the elements in a list until an
element is a tuple.
"""
num = [10, 20, 30, (10, 20), 40]
cnt = 0
for i in num:
    if (isinstance(i, tuple)):
        break
    cnt = cnt + 1
print(cnt)
