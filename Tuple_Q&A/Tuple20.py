"""
Write a Python program to accept two lists and merge the two
lists into list of tuple.
"""
lst1 = [1, 2, 3]
lst2 = ['a', 'b', 'c']
tup = []
for i in range(0, len(lst1)):
    tup.append((lst1[i], lst2[i]))
print(tup)
