class MyException(Exception):
    def __init__(self):
        self.msg = "Incorrect Input"
        return


def main():
    try:
        num = int(input("Enter a number = "))
        if num > 0:
            print("Correct Input")
        else:
            raise MyException()

    except MyException as e:
        print("Error = ", e.msg)

    finally:
        print("Inside Finally Block")


if __name__ == '__main__':
    main()
