# Exercise 2 - Faulty Calculator
# 45 * 3 = 555, 56+9 = 77, 56/6 = 4
# Design a calculator which will correctly solve all the problems except
# the following ones:
# 45 * 3 = 555, 56+9 = 77, 56/6 = 4
# Your program should take operator  and the two numbers as input from the user
# and then return the result


n1 = int(input("Enter the first number : "))
n2 = int(input("Enter the second number : "))
print("MENU \n" +
      "1. '+' \n" +
      "2. '*' \n" +
      "3. '/' \n" +
      "4. '-' \n")
ch = input("Select your choice: ")

if n1 == 45 and n2 == 3 and ch == '*':
    print("555")
elif n1 == 56 and n2 == 9 and ch == '+':
    print("77")
elif n1 == 56 and n2 == 6 and ch == '/':
    print("4")
elif ch == '*':
    n4 = n1*n2
    print(n4)
elif ch == '+':
    plus = n1+n2
    print(plus)
elif ch == '/':
    Dev = n1/n2
    print(Dev)
elif ch == '-':
    Dev = n1-n2
    print(Dev)
elif ch == '%':
    percent = n1 % n2
    print(percent)
else:
    print("Error! Please check your input")
