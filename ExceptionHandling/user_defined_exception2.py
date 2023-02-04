class NameNotProperException(Exception):

    def __init__(self):
        self.msg = "Invalid Name"
        return

def main():

    try:
        n = input("Enter a name = ")
        if n.isalpha():
            print("Welcome ",n)
        else:
            raise NameNotProperException()

    except NameNotProperException as e:
        print("Error desc = ",e.msg)

    finally:
        print("Execute anyway...")

if __name__ == '__main__':
    main()