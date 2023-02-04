# Checking for prime Number.

def Check_prime(n):
    flag = 0
    if n > 1:
        for i in range(2, n):
            # print(i)
            if n % i == 0:
                print(n, "is not a prime number.")
                break
            else:
                flag = 1
    else:
        print("The number is not a prime number.")

    if flag > 0:
        print(n, "is a prime number.")


# Calculating factorial of given number.

def Check_factorial(n):
    fact = 1

    if n < 0:
        print("Factorial does not exist for negative number.")
    elif n == 0:
        print("The factorial of 0 is 1")
    else:
        for i in range(1, (n + 1)):
            fact *= i
        print("The factorial of", n, "is = ", fact)


if __name__ == '__main__':
    n = int(input("Enter a number = "))
    Check_prime(n)
    Check_factorial(n)
