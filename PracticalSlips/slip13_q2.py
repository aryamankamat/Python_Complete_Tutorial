from tkinter import *


def show():
    n = enty.get()
    # print(n)
    num = ""
    for i in n:
        if i == '0':
            num = num + "Zero "
        elif i == '1':
            num = num + "One "
        elif i == '2':
            num = num + "Two "
        elif i == '3':
            num = num + "Three "
        elif i == '4':
            num = num + "Four "
        elif i == '5':
            num = num + "Five "
        elif i == '6':
            num = num + "Six "
        elif i == '7':
            num = num + "Seven "
        elif i == '8':
            num = num + "Eight "
        elif i == '9':
            num = num + "Nine "

    lab2.config(text=num)


root = Tk()
root.title("Display each digit of number in words.")
root.geometry("500x500+400+200")

lab = Label(root, text="Enter a Number : ", font="verdana 12 bold")
enty = Entry(root, font="verdana 12")
btn = Button(root, text="Show", font="verdana 10 bold", command=show)
lab2 = Label(root, text="", font="Forte 20 bold", fg="green")

lab.grid(row=0)
enty.grid(row=0, column=1)
btn.grid(row=1)
lab2.grid(row=3)
root.mainloop()
