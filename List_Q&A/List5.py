"""
5\. Write a Python program to remove duplicates from a list.(Using SET
and without using SET)
"""
a = [10, 20, 30, 20, 10, 50, 60, 40, 80, 50, 40]

"""
ds = set()
lst = []
for i in a:
    if i not in ds:
        ds.add(i)

print(list(ds))
"""

"""
print("The original string is = ", a)
res = set(a)
print("The updated list is = ", list(res))
"""
lst = []
for i in a:
    if i not in lst:
        lst.append(i)
print(lst)
