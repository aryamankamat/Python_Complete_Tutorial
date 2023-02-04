from tkinter import *

root = Tk()
root.title("ADDITION Program")
root.geometry("700x700+400+200")


def ADDITION():
    num1 = int(txtNum1.get())
    num2 = int(txtNum2.get())
    ans = num1 + num2
    txtResult.insert(END,ans)
    #print(num1+num2)
    

lbl1 = Label(root,text="First Number :: ",font = 'verdana 20')
lbl2 = Label(root,text="Second Number :: ",font = 'verdana 20')
lbl3= Label(root,text="RESULT :: ",font = 'verdana 20')


txtNum1 = Entry(root, font= 'verdana 20')
txtNum2 = Entry(root, font= 'verdana 20')
txtResult = Entry(root, font= 'verdana 20')

#txtNum1['show'] = '*'

btnAdd = Button(root,text="ADD",font='verdana 20', command=ADDITION)
btnExit = Button(root,text="EXIT",font='verdana 20',command=root.destroy)

lbl1.grid(row=0,column=0)               #lbl1.grid(row=0)
txtNum1.grid(row=0,column=1)

lbl2.grid(row=1)
txtNum2.grid(row=1,column=1)

lbl3.grid(row=2)
txtResult.grid(row=2,column=1)


btnAdd.grid(row=3)
btnExit.grid(row=3,column=1)



root.mainloop()