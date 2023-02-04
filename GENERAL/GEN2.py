"""
Write a Python program to count the number of 
even and odd numbers from a series of numbers.
"""
strt = int(input("Enter the start number : "))
ed = int(input("Enter the end number : "))
evenCount = 0
oddCount = 0

for i in range(strt, ed+1):
    if (i % 2 == 0):
        evenCount += 1
    else:
        oddCount += 1

print("The number of even numbers are = ", evenCount)
print("The number of odd numbers are = ", oddCount)
