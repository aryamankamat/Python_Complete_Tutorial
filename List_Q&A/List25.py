"""
Write a program to implement the concept of queue using list.
"""
queue = []


while (True):
    print("*****MENU*****")
    print("1.To add elements to the Queue.")
    print("2.To delete elements from the Queue.")
    print("3. To display the Queue.")
    print("4. To exit")
    ch = int(input("Enter a choice : "))

    if (ch == 1):
        n = int(input("Enter a number : "))
        queue.append(n)

    elif (ch == 3):
        print(queue)

    elif (ch == 2):
        print(queue.pop())

    elif (ch == 4):
        exit()
