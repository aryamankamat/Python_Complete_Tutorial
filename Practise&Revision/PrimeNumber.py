"""
A prime number is a whole number greater than 1 whose only factors are 1 and itself. A factor is a whole number that can be divided evenly into another number. 
The first few prime numbers are 2, 3, 5, 7, 11, 13, 17, 19, 23 and 29.
"""

# Method 1
"""
n = int(input("Enter a number : "))

for i in range(2, n):
    if n % i == 0:
        print("It is not a prime number.")
        break
else:
    print("It is prime number!!!")
"""


# Method 2
"""
def prime(Sn, end):
    list = []

    for i in range(Sn, end+1):
        if i > 1:
            for j in range(2, i):
                if i % j == 0:
                    break
            else:
                list.append(i)

    return list


Sn = int(input("Enter the Starting number : "))
En = int(input("Enter the Ending number : "))
lst = prime(Sn, En)
if len(lst) == 0:
    print("There is no prime number in this range.")
else:
    print("The prime number in this range is : \n", lst)
"""


# Method 3
"""
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
"""
