queue = []

while True:
    print("\n\n")
    print("*****MENU*****")
    print("1.ADD elements to the queue")
    print("2.DELETE elements from the queue")
    print("3.Display elements of the queue")
    print("4.Exit")    

    ch = int(input("Select your choice = "))

    if ch == 1:
        n = int(input("Enter a number = "))
        queue.append(n)

    elif ch == 2:
        queue.pop()

    elif ch == 3:
        print("Queue is displayed below...", queue, sep='\n')

    elif ch == 4:
        exit()

    else:
        print("Invalid choice")
