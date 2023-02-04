from tkinter import *


def Change():
    # lab['font'] = ("Cooper Black", 30, "bold")
    lab['font'] = ("Forte", 30, "bold")


root = Tk()
root.title("Label Changing Progrma")
root.geometry("500x500+400+200")

lab = Label(root, text="Hello Python", font="vardana 20", relief="sunken")
btn = Button(root, text="change", font="vardana 12 bold", fg="red", command=Change)

lab.pack()
btn.pack()
root.mainloop()
