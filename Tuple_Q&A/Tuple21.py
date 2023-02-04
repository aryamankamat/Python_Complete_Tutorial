"""
Write a Python program to convert a tuple of string values to a
tuple of integer values.
"""
tuple_str = (('333', '33'), ('1416', '55'))
tup_int = ()
for i in tuple_str:
    tup_int = tup_int + tuple((int(i[0]), int(i[1])))
print(tup_int)
