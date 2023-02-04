d = {4: 22, 8: 90, 3: 21, 5: 69, 2: 45, 6: 80}

print("Original Dictionary...")
print(d)
print()
print("Dictionary sorted in Ascending order...")
asc_dict = dict(sorted(d.items()))
print(asc_dict)
print()
print("Dictionary sorted in Descending order...")
des_dict = dict(sorted(d.items(),reverse=True))
print(des_dict)
