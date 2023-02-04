"""
10. Write a Python program to accept a number from the user
and find its factorial. Do necessary validations. 
"""
n = int(input("Enter a number : "))
if (n == 0) or (n == 1):
    print("The factorial of number", n, "is = 1")
else:
    fact = 1
    for i in range(1, n+1):
        fact = fact * i
    print("The factorial of number", n, "is = ", fact)
