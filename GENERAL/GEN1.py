"""
Write a Python program to find those numbers which are divisible by 7 and 
multiple of 5,between 1 and 1000 (both included).
"""
for i in range(1, 1001):
    if (i % 7 == 0) and (i % 5 == 0):
        print(i)
