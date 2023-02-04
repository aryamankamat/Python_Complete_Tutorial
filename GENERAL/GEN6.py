"""
Write a Python program to calculate the 
sum and average of n integer numbers (input from the user). Input 0 to finish.
"""
# method1
"""
n = int(input("Enter last limit : "))
s = 0
cnt = 0
for i in range(0, n+1):
    s = s + i
    cnt = cnt + 1

if (cnt == 0):
    print("Input some number.")
ag = s / (cnt-1)
print("The sum is = ", s, "and average is = ", ag)
"""

# method2
n = int(input("Enter last limit : "))
s = 0

for i in range(0, n+1):
    s = s + i

if (n == 0):
    print("Input some number.")
ag = s / (n)
print("The sum is = ", s, "and average is = ", ag)
