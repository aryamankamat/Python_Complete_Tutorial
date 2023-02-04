import sys

num1 = int(input('Enter First No.::'))
num2 = int(input('Enter Second No.::'))
try:
    ans = num1/num2
    print(f"{num1}/{num2} = {ans}")
#print("Hello")
except:
    print("Error caught")
    print(sys.exc_info())
    #print("Err. Desc. ::",sys.exc_info()[1])
    

