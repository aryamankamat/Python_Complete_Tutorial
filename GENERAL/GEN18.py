"""
Write a program to accept a binary number and convert it into
decimal number.
"""
n = list(input("Enter a binary number : "))
val = 0

for i in range(len(n)):
    digit = n.pop()
    if digit == '1':
        val = val + pow(2, i)
print(f"Decimal value is = {val}")
