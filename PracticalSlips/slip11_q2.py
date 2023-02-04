from tkinter import *
import random
import string


def Generate():
    res = ''.join(random.choices(string.ascii_uppercase + string.ascii_lowercase, k=8))
    # entry.insert(0, str(res))
    lab2.config(text=str(res))


root = Tk()
root.title("Generate Random password")
root.geometry("500x500+400+200")

lab1 = Label(root,text=".....Random Password Generator.....",font="Forte 20",bg="black",fg="white")

# entry = Entry(root, font="verdana 12", fg="red")
lab2 = Label(root, text="", font="verdana 12", fg="red")

btn = Button(root, text="generate", font="Forte 12",command=Generate)

lab1.pack()
# entry.pack()
lab2.pack()
btn.pack()

root.mainloop()
