# METHOD 1
# n = int(input("Enter the limit : "))
"""
8. Write a python program to sum of the first n positive integers.
"""
# pos = 0
# for i in range(0, n+1):
#     if (i > 0):
#         pos = pos + i
#print("The sum of first", n, "positive numbers is = ", pos)

# METHOD 2
n = int(input("Enter the limit : "))
total = n * (n+1) // 2
print("The sum of first", n, "positive numbers is = ", total)
