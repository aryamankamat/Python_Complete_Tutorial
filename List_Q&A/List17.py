"""
Write a Python program to find common items from two lists.(Using
SET and without using SET)

**EXAMPLE :**

**Assume below mentioned two lists :**

> a = [1, 2, 3, 5]
>
> b = [1, 2]

**OUTPUT : Common_items** = [1,2]
"""
a = [1, 2, 3, 5]
b = [1, 2]
lst = []
for i in a:
    for j in b:
        if (i == j):
            lst.append(i)
print(lst)
