from tkinter import *


def AddLang():
    code = txtLang.get()
    lst.insert(END, code)
    txtLang.delete(0, END)
    txtLang.focus()
    return


def DelLang():
    lst.delete(2)


def PrintLang():
    fav = "Your Favorites : "
    indices = lst.curselection()
    print(indices)
    # print("Value at index 2 = ",lst.get(2))
    print("Your favorite Languages:")
    for index in indices:
        fav = fav + lst.get(index) + "   "
        # print(lst.get(index))

    lblFav.config(text=fav, fg='blue')


root = Tk()
root.title('PROGRAM')
root.geometry('500x500')

lst = Listbox(root, font='verdana 15', selectmode='multiple')
lst.insert(0, 'C')
lst.insert(1, 'Cpp')
lst.insert(2, 'Java')
lst.insert(3, 'Python')

lbl1 = Label(root, text='Select Languages', font='verdana 15')
lbl2 = Label(root, text='Insert Language', font='verdana 15')
txtLang = Entry(root, font='verdana 15')
btnInsert = Button(root, text='INSERT', font='verdana 15', command=AddLang)
btnPrint = Button(root, text='PRINT', font='verdana 15', command=PrintLang)
btnDel = Button(root, text='DELETE', font='verdana 15', command=DelLang)
btnExit = Button(root, text='EXIT', font='verdana 15', command=root.destroy)
lblFav = Label(root, text='', font='verdana 15')

lbl1.grid(row=0)
lst.grid(row=0, column=1)
lbl2.grid(row=1, column=0)
txtLang.grid(row=1, column=1)
btnInsert.grid(row=2, column=0)
btnPrint.grid(row=2, column=1)
btnDel.grid(row=3)
btnExit.grid(row=3, column=1)
lblFav.grid(row=4)

root.mainloop()
