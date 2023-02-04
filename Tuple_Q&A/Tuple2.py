"""
Write a Python program to create a tuple with different data
types.
"""
lst = [12, 33, 45, 67, 89, 90]
st = {44, 56, 64, 34, 22}
d = {'name': 'Aryman', 'per': 99.9}
s = "Indira"
print("Tuple from different data types is dislplayed : ")
print("Tuple using a list is displayed below...")
print(tuple(lst))
print("Tuple using a set is displayed below...")
print(tuple(st))
print("Tuple using a string is displayed below...")
print(tuple(s))
print("Tuple using a dictionary is displayed below...")
print(tuple(d))
