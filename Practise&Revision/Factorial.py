# Write a Program to calculate the factorial of two number.

# Method 1
"""
def fact(n):
    if n == 0 or n == 1:
        return 1

    f = 1
    for i in range(1, n+1):
        f = f * i

    return f


n = int(input("Enter a number : "))
result = fact(n)
print("The factorial of ", n, " is = ", result)
"""


# Method 2
"""
def fact(n):
    if (n == 0 or n == 1):
        return 1
    else:
        return n * fact(n - 1)


n = int(input("Enter a number : "))
print("The factorial of ", n, " is = ", fact(n))
"""

#method3
n = int(input("Enter a number : "))
if n == 0 or n == 1:
        print("The factorial of number",n,"is = 1")
else:
    fact = 1
    for i in range(1,n+1):
        fact = fact * i
    print("The factorial of number",n,"is = ",fact)
