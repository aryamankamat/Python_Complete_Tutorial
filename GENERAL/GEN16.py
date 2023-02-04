"""
Write a Python program which will print the sum of even numbers
between 21 to 45.
"""
sum = 0
print("List of even numbers is displayed below...")
for i in range(21, 45, 2):
    sum = sum + i
    print(i)
print("Sum of all even numbers is = ", sum)
