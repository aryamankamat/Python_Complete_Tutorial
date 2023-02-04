"""
Write a Python program to perform sum of two given integers.
However, if the sum is between 15 to 20, it will return 20.
"""
n1 = int(input("Enter the 1st number : "))
n2 = int(input("Enter the 2nd number : "))
s = n1 + n2
if s in range(15, 21):
    print(int(20))
else:
    print("Out of range!!!")
