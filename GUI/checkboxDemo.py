from tkinter import *


def show():
    print("Method called...")
    status = chkState1.get()
    print("STATUS :", status)
    return


root = Tk()
root.title('PROGRAM')
root.geometry('400x400')
# chkState1 = BooleanVar()
# chkState1 = IntVar()
# chkState1 = DoubleVar()
chkState1 = StringVar()
chkHockey = Checkbutton(root, text='Hockey', font='Verdana 15',
                        command=show, variable=chkState1,
                        onvalue="Hello", offvalue="Sayonara")

# chkHockey = Checkbutton(root,text='Hockey', font='Verdana 15',
#                        command= show, variable=chkState1,
#                        onvalue=99, offvalue=1111)
chkHockey.pack()
root.mainloop()
