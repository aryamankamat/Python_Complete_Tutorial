from tkinter import *

def PrintCourse():
    course = "Your courses : "
    crs = lst.curselection()
    for i in crs:
        course = course + lst.get(i) + "  "
    lab2.config(text=course)



root = Tk()
root.title("Computer Science Courses")
root.geometry("500x500+400+200")

lab1 = Label(root, text="Select Course : ", font="verdana 15")

lst = Listbox(root,font="verdana 12", selectmode="multiple")
lst.insert(0, "BBACA")
lst.insert(1, "BCS")
lst.insert(2, "BSC-CS")
lst.insert(3, "BCA-Science")

btn = Button(root, text='PRINT', font='verdana 15', command=PrintCourse)

lab2 = Label(root, text="", font="Forte 15 bold", fg="white", bg="black")

lab1.grid(row=0)
lst.grid(row=0, column=1)
btn.grid(row=1)
lab2.grid(row=1,column=1)


root.mainloop()