"""
Write Python GUI program to accept a decimal number and convert and display it to binary, octal and hexadecimal number.
"""
import tkinter

root = tkinter.Tk()
root.title("Convert number from decimal to binary, hexadecima and octal form")
root.geometry("600x600+400+200")


def Convert():
    n = int(txtNum1.get())

    # print("....COVERTED VALUES ARE DISPLAYED BELOW....")
    # print(n,"into binary form = ",bin(n))
    # print(n,"into ocatl form = ",oct(n))
    # print(n,"into Hexadecimal form = ",hex(n))
    ans1 = bin(n)
    ans2 = oct(n)
    ans3 = hex(n)
    result1.insert(0, ans1)
    result2.insert(0, ans2)
    result3.insert(0, ans3)


# lab0 = tkinter.Label(root,text="Convertion From Decimal to Binary, Ocatal and Hexadecimal",font="vardana 20 bold")
lab1 = tkinter.Label(root, text="Enter a number : ", font="vardana 15 bold")
lab2 = tkinter.Label(root, text="Binary", font="vardana 15 bold")
lab3 = tkinter.Label(root, text="Ocatal: ", font="vardana 15 bold")
lab4 = tkinter.Label(root, text="Hexadecimal", font="vardana 15 bold")

txtNum1 = tkinter.Entry(root, font="verdana 15 bold")
result1 = tkinter.Entry(root, font="verdana 15 bold",fg="blue")
result2 = tkinter.Entry(root, font="verdana 15 bold",fg="red")
result3 = tkinter.Entry(root, font="verdana 15 bold",fg="green")

btnConvert = tkinter.Button(root, text="CONVERT", font="vardana 12 bold", command=Convert)
btnExit = tkinter.Button(root, text="EXIT", font='verdana 12 bold', command=root.destroy)
# lab0.grid(row=0,column=0)

lab1.grid(row=1, column=1)
txtNum1.grid(row=1, column=2)

lab2.grid(row=2, column=1)
result1.grid(row=2, column=2)

lab3.grid(row=3, column=1)
result2.grid(row=3, column=2)

lab4.grid(row=4, column=1)
result3.grid(row=4, column=2)

btnConvert.grid(row=5)
btnExit.grid(row=5, column=1)

root.mainloop()
