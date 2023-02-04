"""
Write a Python script to find a number is a prime number or not.
A number that is divisible only by itself and 1 (e.g. 2, 3, 5, 7, 11).
"""

#I-logic
"""
n = int(input("Enter a number : "))

for i in range(2,n):
    if (n % i == 0):
        print("The number is not a Prime number.")
        break
else:
    print("The number is a Prime number.")
"""

#II-logic

Sn = int(input("Enter the Starting number : "))
En = int(input("Enter the Ending number : "))
print("The Prime numbers from ", Sn, " to ", En, " are displayed below...")
for i in range(Sn, En+1):
    flag = 0
    for j in range(2, i):
        if i % j == 0:
            flag = 1
            break

    if flag == 0:
        print(i, end=" ")
