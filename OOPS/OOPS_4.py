class Demo():
    def show(self):
        print("HELLO")
        print("ID of self = ", id(self))

    def display(self,name,city):
        print(name,city)
    
d1 = Demo()
d1.show()  #==> Demo.show(d1)
print("ID of d1 = ", id(d1))
d1.display('ABC','Pune') #==>Demo.display(d1,'ABC','Pune')

