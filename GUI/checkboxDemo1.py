from tkinter import *


def show():
    hobbies = ""
    if chkState1.get() == 1:
        hobbies = hobbies + chkHockey['text']
    if chkState2.get() == True:
        hobbies = hobbies + "Cricket "
    if chkState3.get():
        hobbies = hobbies + "Chess "

    lblSel.config(text=hobbies, font='verdana 15')

    return


root = Tk()
root.title('PROGRAM')
root.geometry('400x400')
chkState1 = IntVar()
chkState2 = IntVar()
chkState3 = IntVar()

chkHockey = Checkbutton(root, text='Hockey', font='Verdana 15',
                        command=show, var=chkState1)
chkCri = Checkbutton(root, text='Cricket', font='Verdana 15',
                     command=show, variable=chkState2)
chkChess = Checkbutton(root, text='Chess', font='Verdana 15',
                       command=show, variable=chkState3)
lblMsg = Label(root, text="SELECT CHOICES :")
lblSel = Label(root, text="")

lblMsg.grid(row=0, column=0)
chkHockey.grid(row=0, column=1)
chkCri.grid(row=0, column=2)
chkChess.grid(row=0, column=3)
lblSel.grid(row=1, column=0)

root.mainloop()
