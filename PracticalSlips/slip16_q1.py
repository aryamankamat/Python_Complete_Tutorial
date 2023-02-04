from tkinter import *


def Change():
    s1 = entry.get()
    ans = s1.upper()
    labCng.config(text=ans)
    return


root = Tk()
root.title("Slip 16 Question 1.")
root.geometry("500x500+400+200")

lab = Label(root, text="Enter a String : ", font="verdana 15 bold")
entry = Entry(root, font="verdana 12")
btn = Button(root, text="Change", font="Forte 12", command=Change)
labCng = Label(root, font="Forte 15 bold", fg="pink", text="")

lab.grid(row=0)
entry.grid(row=0, column=1)
btn.grid(row=1)
labCng.grid(row=1, column=1)

root.mainloop()
