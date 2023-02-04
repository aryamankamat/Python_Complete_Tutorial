"""
Write a Python program to sort a dictionary by key.
"""
d = {4: 22, 8: 90, 3: 21, 5: 69, 2: 45, 6: 80}
"""
for k in sorted(d):
    print(k, d[k])
"""

new_ans = dict(sorted(d.items()))
print(new_ans)
