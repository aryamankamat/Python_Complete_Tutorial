"""
Write a Python program to get the difference between the two lists.
(Using SET and without using SET)

EXAMPLE :

Assume below mentioned two lists :
> a = [1, 2, 3, 5]
> b = [1, 2]
OUTPUT :
> lst_diff = [3, 5]
"""

# Using set
list1 = [1, 3, 5, 7, 9]
list2 = [1, 2, 4, 6, 7, 8]
d_list1 = list(set(list1) - set(list2))
d_list2 = list(set(list2) - set(list1))
diff = d_list1 + d_list2
print(diff)
