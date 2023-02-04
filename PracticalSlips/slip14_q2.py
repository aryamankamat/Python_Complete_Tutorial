from tkinter import *


def AddItem():
    itm = enty.get()
    lstbox.insert(ACTIVE, itm)
    enty.focus()
    return


def DelItem():
    lstbox.delete(ACTIVE)
    return


def PrintItem():
    sel = "Your Selected Items : "
    itm = lstbox.curselection()
    # print(itm)
    for i in itm:
        sel = sel + lstbox.get(i) + "  "

    lblFav.config(text=sel, fg="yellow")
    return


root = Tk()
root.title("Add elements to a Listbox")
root.geometry("500x500+400+200")

# 1st Label
lab1 = Label(root, text="Select elements : ", font="verdana 15")

# ListBox
lstbox = Listbox(root, font="verdana 12", selectmode="multiple")
lstbox.insert(0, "Bag")
lstbox.insert(1, "Shoes")

# 1st Labe2
lab2 = Label(root, text="Insert a Item : ")

# Entry for Label2
enty = Entry(root, font="verdana 12")

# Display Label
lblFav = Label(root, text='', font='verdana 15')

# Buttons
btn1 = Button(root, text="ADD", font="verdana 12", command=AddItem)
btn2 = Button(root, text="PRINT", font="verdana 12", command=PrintItem)
btn3 = Button(root, text="DELETE", font="verdana 12", command=DelItem)

# Positions
lab1.grid(row=0)

lstbox.grid(row=0, column=1)

lab2.grid(row=1)
enty.grid(row=1, column=1)

btn1.grid(row=2, column=2)
btn2.grid(row=2, column=3)
btn3.grid(row=2, column=4)

lblFav.grid(row=3)

root.mainloop()
