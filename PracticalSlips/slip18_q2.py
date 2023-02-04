from tkinter import *


def show():
    s = entry.get()
    ch = entry2.get()
    ans = s.count(ch)
    lab2.config(text=ans)



root = Tk()
root.title("Slip 18 Question 2")
root.geometry("500x500+400+200")

lab1 = Label(root, text="Enter a String : ", font="verdana 15")
entry = Entry(root, font="verdana 12")

lab3 = Label(root, text="Enter a Character : ", font="verdana 15")
entry2 = Entry(root, font="verdana 12")

lab2 = Label(root,text="", font="Forte 15 bold", fg="white",bg="black")

btn = Button(root, text="Count", font="Forte 12", command=show)

lab1.grid(row=0)
entry.grid(row=0,column=1)

lab3.grid(row=1)
entry2.grid(row=1,column=1)

btn.grid(row=2)
lab2.grid(row=2,column=1)

root.mainloop()