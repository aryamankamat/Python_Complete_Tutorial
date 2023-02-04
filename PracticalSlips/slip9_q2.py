from tkinter import *


def CheckNum():
    ch = num.get()
    # print(ch)
    if ch == 1:
        n = int(txtNum1.get())
        # print(n)
        flag = 0
        for i in range(2, n):
            if (n % i) == 0:
                flag = True
                break
        if flag:
            print("The number is not a prime number.")
        else:
            print("The number is a prime number.")

    elif ch == 2:
        n = int(txtNum1.get())
        # print(n)
        sum1 = 0
        rem = 0
        num1 = n
        # print(num1)
        while n != 0:
            rem = n % 10
            sum1 = sum1 + (rem ** 3)
            n = n // 10
        if num1 == sum1:
            print("The number is a Armstrong number.")
        else:
            print("The number is not Armstrong number.")


    elif ch == 3:
        n = int(txtNum1.get())
        # print(n)
        sum2 = 0
        for i in range(1, n):
            if n % i == 0:
                sum2 = sum2 + i
        if sum2 == n:
            print("The number is a Perfect Number.")
        else:
            print("The number is not a Perfect number.")


root = Tk()
root.title("Checkig a number is prime or Armstrong or perfect")
root.geometry("500x500+300+200")

# variable class
num = IntVar()

lab1 = Label(root, text="Enter a number : ", font="vardana 12 bold")
txtNum1 = Entry(root, font="verdana 15 bold")

lab2 = Label(root, text="Select your choice : ", font="vardana 12 bold")

radio1 = Radiobutton(root, text="Prime", font="vardana 15 bold", var=num, value=1)
radio2 = Radiobutton(root, text="Armstrong", font="vardana 15 bold", var=num, value=2)
radio3 = Radiobutton(root, text="Perfect", font="vardana 15 bold", var=num, value=3)

btnCheck = Button(root, text="Check", font="vardana 12", command=CheckNum)

lab1.grid(row=0)
txtNum1.grid(row=0, column=1)

lab2.grid(row=1, column=0)

radio1.grid(row=1, column=2)
radio2.grid(row=1, column=3)
radio3.grid(row=1, column=4)

btnCheck.grid(row=2, column=0)

root.mainloop()
