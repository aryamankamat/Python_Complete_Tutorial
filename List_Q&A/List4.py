"""
4. Write a Python program to count the number of strings where the
string length is 2 or more and the first and last character are same
from a given list of strings.
"""
lst = ['abc', 'xyz', 'aba', '1221']
cnt = 0
for i in lst:
    if ((len(i) > 1) and (i[0] == i[-1])):
        cnt = cnt + 1
print("The number of strings which satisfy the conditions are = ", cnt)
