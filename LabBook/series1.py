"""
 Write a Python program to sum the series:  

1 + 1/2^2 + 1/3^2 + 1/4^2 + ………. + 1/n^2 

If n = 3, then sum should be of first THREE terms only i.e. 1 + 1/2^2 + 1/3^2
"""
import math

n = int(input("Enter a number : "))
summ = 0
siri = 0
for i in range(1,n+1):
    siri = 1 / pow(i,i)
    summ = summ+siri
print("The sum of",n," numbers is = ",summ)
