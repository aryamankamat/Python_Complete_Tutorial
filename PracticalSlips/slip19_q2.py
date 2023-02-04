from tkinter import *

def show():
    # u = uservalue.get()
    # p = passvalue.get()
    print(f"The user name is = {uservalue.get()}")
    print(f"The password is = {passvalue.get()}")


root = Tk()
root.title("Displaying Username and Password")
root.geometry("500x500+400+200")

uservalue = StringVar()
passvalue = StringVar()

lab1 = Label(root, text="Enter Username : ", font="verdana 15")
entry1 = Entry(root, font="verdana 15", textvariable=uservalue)

lab2 = Label(root, text="Enter Password : ", font="verdana 15")
entry2 = Entry(root, font="verdana 15", textvariable=passvalue)

btn = Button(root, text="Display", font="Forte 12", fg="pink", command=show)

lab1.grid(row=0)
entry1.grid(row=0, column=1)
lab2.grid(row=1)
entry2.grid(row=1, column=1)

btn.grid(row=2)

root.mainloop()