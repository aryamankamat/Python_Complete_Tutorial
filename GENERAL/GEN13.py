"""
Write a Python program to accept a number from the user and prints sum of its digits.
"""
n = input("Enter a number : ")
sum = 0
for i in n:
    sum = sum + int(i)

print(f"sum of {n} is = {sum}")
