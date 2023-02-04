"""
Write a Python program to slice a tuple.
"""
s = "Indira college of commerce and science"
tup = tuple(s)
# print(tup)
new_tup = tup[7:]
tstr = ''.join(new_tup)
print("Sliced tuple is displayed below...", tstr, sep='\n')
