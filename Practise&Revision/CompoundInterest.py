# Write a program to calculate the compound interest.

def compoundInterest(p, r, t):

    amt = p * pow((1 + r/100), t)
    CI = amt - p
    print("The compound Interest is = ", CI)


p = int(input("Enter the principle value : "))
r = int(input("Enter the rate of interest : "))
t = int(input("Enter the time period : "))
compoundInterest(p, r, t)
