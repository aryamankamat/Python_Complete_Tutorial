stack = []

while True:
    print("*****MENU*****")
    print("1.ADD elements to the stack")
    print("2.DELETE elements from the stack")
    print("3.Display elements of the stack")
    print("4.Exit")    

    ch = int(input("Select your choice = "))

    if ch == 1:
        n = int(input("Enter a number = "))
        stack.append(n)

    elif ch == 2:
        stack.pop()

    elif ch == 3:
        print("Stack is displayed below...", stack, sep='\n')

    elif ch == 4:
        exit()

    else:
        print("Invalid choice")
