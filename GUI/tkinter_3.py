from tkinter import *

root = Tk()
root.title("First Program")
root.geometry("400x400+600+200")


def show():
    print("Hello World")
    return 

lblMsg = Label(root,text="Hello World", font = ('Times New Roman',20,'italic'))

btnClick = Button(root,text="Click Me!", font='verdana 20',command=show)


btnExit = Button(root,text="EXIT", font='verdana 20',command=root.destroy)

lblMsg.pack()
btnClick.pack()
btnExit.pack()

root.mainloop()