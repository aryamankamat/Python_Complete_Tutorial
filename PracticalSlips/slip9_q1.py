tup = (6, -2, 1, 9, 2, 8, -2, 9, -4, 1, 8, -2)
s = set()
for i in tup:
    if tup.count(i) > 1:
        s.add(i)

lst = list(sorted(s))
print(lst)
