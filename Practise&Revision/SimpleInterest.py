# Write a program to calculate the simple interest

def simpleInteres(p, r, t):
    print("The Principle amount is = ", p)
    print("The Rate of Interest is = ", r)
    print("The Time period is = ", t)

    si = (p * r * t)/100
    print("The simple interest is = ", si)


p = int(input("Enter the principle value : "))
r = int(input("Enter the rate of interest : "))
t = int(input("Enter the time period : "))
simpleInteres(p, r, t)
