import sys

print("START")
try:
    x=10
    y=2
    ans = x/y
    print("Answer = ", ans)

except ZeroDivisionError as e:
    print("Error : ", e)

else: 
    print("Inside the else block")

finally:
    print("Inside the finally block")

print("END")