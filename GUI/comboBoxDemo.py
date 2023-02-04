from tkinter import * 
from tkinter.ttk import Combobox

def show():
    myCity = comboCity.get()
    lblCity.config(text='My City is : ' + myCity,fg='blue' )
    return

root = Tk()
root.title('Combobox Demo')
root.geometry('500x500+300+200')

city = ('--Select City--','Pune','Thane','PCMC','Mumbai')

comboCity = Combobox(root,font='verdana 15', values=city,
                     state = 'readonly')

lbl1 = Label(root,text='Select City :', font='verdana 15')

btnShow = Button(root,text='Click Me!', font='verdana 15',
                 command = show)

lblCity = Label(root, font='verdana 15')
lbl1.grid(row=0,column=0)
comboCity.grid(row=0,column=1)
btnShow.grid(row=1,column=0)
lblCity.grid(row=1,column=1)

comboCity.current(0)

root.mainloop()