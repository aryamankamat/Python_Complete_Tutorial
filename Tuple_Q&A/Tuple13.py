"""
Write a Python program to find the index of an item of a tuple.
"""
t = tuple("Indira")
idx = t.index('d')
print(idx)
idx1 = t.index('i', 3)
print(idx1)
idx1 = t.index('a', 3, 6)
print(idx1)
