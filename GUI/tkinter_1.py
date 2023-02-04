
import tkinter

root = tkinter.Tk()
root.title("First Program")
root.geometry("400x400+600+200")

'''
lblMsg = tkinter.Label(root,text="Hello World",
              font = "Verdana 20 bold", relief='sunken')
'''
lblMsg = tkinter.Label(root,text="Hello World",
              font = ('Times New Roman',20,'italic'))


#lblMsg['fg'] = 'BLUE'
#lblMsg['bg'] = 'YELLOW'
# lblMsg['text'] = 'ICCS'
# lblMsg['cursor'] = 'pirate'

lblMsg.pack()

root.mainloop()