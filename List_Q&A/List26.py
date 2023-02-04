"""
Write a program to implement the concept of stack using list.
"""
stack = []

while True:
    print("*****MENU*****")
    print("1.To add elements to the stack.")
    print("2.To delete elements from the stack.")
    print("3. To display the stack.")
    print("4. To exit")

    ch = int(input("Enter a choice : "))

    if (ch == 1):
        n = int(input("Enter a number : "))
        stack.append(n)

    elif (ch == 3):
        print("Stack is displayed below...", stack, sep='\n')

    elif (ch == 2):
        print(stack.pop())

    elif (ch == 4):
        exit()
    else:
        print("Invalid choice...")
        exit()
