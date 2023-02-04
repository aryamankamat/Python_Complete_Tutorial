from tkinter import *


def show():
    s = entry.get()
    # ans = s.replace(' ', '*').swapcase()
    for i in s:
        if i.isdigit():
            s = s.replace(i, '@')
    ans = s.replace(' ', '*').swapcase()
    entry1.insert(0, ans)


root = Tk()
root.title()
root.geometry("500x500+400+200")

lab = Label(root, text="Enter a Sentence : ", font="verdana 20 bold")
entry = Entry(root, font="verdana 12", width=50)
btn = Button(root, text="Click Me!", font="Forte 15", command=show)
entry1 = Entry(root, font="verdana 15 bold", bg="black", fg="white", width=50)

lab.pack()
entry.pack()
btn.pack()
entry1.pack()

root.mainloop()
