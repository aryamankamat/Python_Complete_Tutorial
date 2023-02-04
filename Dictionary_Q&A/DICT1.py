"""
1. Write a Python script to add a key to a dictionary.
**Sample Dictionary :** {0: 10, 1: 20}
**Expected Result :** {0: 10, 1: 20, 2: 30}
"""
d = {0: 10, 1: 20}
print("Original Dictionary...", d, sep='\n')

d2 = {2: 30}
d.update(d2)
print("updated dictionary is displayed below...", d, sep='\n')
