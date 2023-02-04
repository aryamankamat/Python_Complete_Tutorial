# An Armstrong number of three digits is an integer such that the sum of the cubes of its digits is equal to the number itself.
# For example, 371 is an Armstrong number since 3**3 + 7**3 + 1**3 = 371.

"""
n = int(input("Enter a number : "))
temp = n
length = len(str(n))
sum = 0
# print(length)

while (temp > 0):
    rem = temp % 10
    sum = sum + rem ** length
    temp = temp // 10

if (sum == n):
    print("The Entered number is an Armstrong")
else:
    print("The entered number is not an Armstrong number")
"""
