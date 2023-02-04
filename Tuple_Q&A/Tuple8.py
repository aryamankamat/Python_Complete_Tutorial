"""
Write a Python program to find the repeated items of a tuple.
"""
tup = 2, 4, 5, 6, 2, 3, 4, 4, 7
print("Original tuple elements are displayed below...", tup, sep='\n')
n = int(input("Enter a number to count it's occurance : "))
cnt = tup.count(n)
print("Element", n, "occurace", cnt, "times.")
