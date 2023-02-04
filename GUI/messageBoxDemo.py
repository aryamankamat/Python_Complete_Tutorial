from tkinter import *
from tkinter.ttk import Combobox
from tkinter import messagebox


def show():
    response = messagebox.askokcancel('Test', 'Want to continue?')
    if response == True:
        print("You will be redirected to another window")
    else:
        print("You aborted the application")
    return


root = Tk()
root.title('Combobox Demo')
root.geometry('500x500+300+200')

btnShow = Button(root, text='Click Me!', font='verdana 15',
                 command=show)

btnShow.grid(row=0, column=0)

root.mainloop()
