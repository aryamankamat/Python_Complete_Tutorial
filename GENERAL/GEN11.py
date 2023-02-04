"""
11. Write a Python program to accept two numbers from the user and swap them. 
"""
n1 = int(input("Enter the 1st number : "))
n2 = int(input("Enter the 2nd number : "))
print("The values Before swapping are : n1 =", n1, "and n2 = ", n2)

# n1, n2 = n2, n1   #logic 1
"""
n1 = n1 + n2
n2 = n1 - n2    #logic 2
n1 = n1 - n2
"""
"""
n1 = n1 ^ n2
n2 = n1 ^ n2    # logic 3
n1 = n1 ^ n2
"""
"""
temp = n1
n1 = n2         #logic 4
n2 = temp
"""
print("The values After swapping are : n1 =", n1, "and n2 = ", n2)
