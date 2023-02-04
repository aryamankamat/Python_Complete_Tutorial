# Method Overriding
# super() is a proxy object which refers to the immediate base class


class Base():
    x = 10

    def show(self):
        print("Base::show")
        return


class Derived(Base):
    y = 100
    x = "Hello World"

    def display(self):
        print("Derived::display")
        print("x = ", Derived.x)
        # print("x = ", Base.x) #refes to the parent class value x
        print("x = ", super().x)  # refes to the parent class value x
        return

    def show(self):  # overrides the Base::show() method
        print("Derived::show")
        # Base.show(self)
        super().show()  # ==>Base.show(super())
        return


obj1 = Derived()
# print("Available attributes of obj1 = ", obj1.__dict__)
# print("Accessible attributes of obj1 = ", dir(obj1))

# obj1.display() #==> Derived.display(obj1)
obj1.show()
