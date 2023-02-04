from tkinter import *
from tkinter import messagebox


def show():
    m = messagebox.showwarning("Alert", "Hello User!!!")
    return


root = Tk()
root.title("Generating an Alert.")
root.geometry("500x500+400+300")

btn = Button(root, text="Click Me!", font="Forte 15 bold", command=show)

btn.pack()


root.mainloop()