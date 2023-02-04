import tkinter
# from tkinter import *

root = tkinter.Tk() #Constructor
# root = Tk() #Constructor
root.title("Testing frame of Tkinter.")
root.geometry("600x600")
# root.minsize(300,300) #minimum size of window
# root.maxsize(900,900) #maximum size of window
lab1 = tkinter.Label(text="Hello Python",bg="yellow",fg="white",font="vardana 20 bold",borderwidth=5,relief="sunken")
lab1.pack()
root.mainloop()