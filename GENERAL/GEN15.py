"""
Write a Python program which will print the sum of first N natural
numbers. (Accept the value of N from the user).
"""
sum = 0
n = int(input("Enter a limit : "))
for i in range(n):
    sum = sum + i
print("Sum of n naturals numbers is = ", sum)
