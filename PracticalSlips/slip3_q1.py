x = (1, 2, 3, 4)
y = (3, 5, 2, 1)
z = (2, 2, 3, 1)

print("Original tuple values are displayed below... ")
print(x)
print(y)
print(z)

lst = zip(x, y, z)
result = tuple(map(sum, lst))
print("Sum of individual elements are displayed below...")
print(result)
