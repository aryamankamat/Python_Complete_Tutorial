class MyException(Exception):
    def __init__(self):
        self.msg = "It is user Defined exception"
        return

def main():
    try:
        print("Inside try block...")
        raise MyException()
    except MyException as e:
        print("Error desc = ",e.msg)

    finally:
        print("Execute finally anyway...")

if __name__ == "__main__":
    main()
