lst = [1, 2, 3, 4, 2, 55, 6, 4, 10]
lst2 = []

for i in lst:
    if i not in lst2:
        lst2.append(i)

print("Original list = ", lst)
print("The Non duplicate elements are displayed below...")
print(lst2)
