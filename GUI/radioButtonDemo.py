from tkinter import *


def show():
    gen = gender.get()
    # print(f"VAlue = {gen}")
    if gen == 1:
        print("You are ", radioMale['text'])
    elif gen == 2:
        print("You are ", radioFemale['text'])
    elif gen == 3:
        print("You are Transgender.....")
    return


root = Tk()
root.title('PROGRAM')
root.geometry('500x500')

gender = IntVar()

radioMale = Radiobutton(root, text="MALE", font='Verdana 12',
                        var=gender, value=1)
radioFemale = Radiobutton(root, text="FEMALE", font='Verdana 12',
                          var=gender, value=2)
radioOther = Radiobutton(root, text="OTHERS", font='Verdana 12',
                         var=gender, value=3)
lblMsg = Label(root, text="SELECT GENDER :", font='Verdana 12')

btnShow = Button(root, text='CLICK', font='verdana 12', command=show)

lblMsg.grid(row=0, column=0)
radioMale.grid(row=0, column=1)
radioFemale.grid(row=0, column=2)
radioOther.grid(row=0, column=3)
btnShow.grid(row=1, column=0)

root.mainloop()
