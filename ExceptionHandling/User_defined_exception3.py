class InvalidNumberError(Exception):
    def __init__(self):
        self.msg = "Number is NOT Perfect"


def main():
    try:
        n = int(input("Enter a number "))
        sum1 = 0

        for i in range(1, n):
            if n % i == 0:
                sum1 = sum1 + i

        if sum1 == n:
            print("The number is a perfect number.")
        else:
            raise InvalidNumberError()

    except InvalidNumberError as i:
        print(i.msg)


if __name__ == '__main__':
    main()
