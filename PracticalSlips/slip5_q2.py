""" Write a Python program to convert a tuple of string values to a tuple of integer values.
Original tuple values: (('333', '33'), ('1416', '55'))
New tuple values: ((333, 33), (1416, 55))
"""
tup = (('333', '33'), ('1416', '55'))

res = tuple((int(i[0]), int(i[1])) for i in tup)

print("Original Tuple values are...")
print(tup)
print("New Tuple values are...")
print(res)
