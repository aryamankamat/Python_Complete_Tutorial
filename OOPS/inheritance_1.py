class base(object):
    pass

class child(base):
    pass

c = child()

print("c is object of class child :", isinstance(c,child))
print("c is object of class base :", isinstance(c,base))
print("c is object of class object :", isinstance(c,object))
print("c is object of class int :", isinstance(c,int))

print("child is subclass of base :", issubclass(child,base))
print("base is subclass of object :", issubclass(base,object))
print("child is subclass of object :", issubclass(child,object))

print("ANS :", type(c) == base) 
print("ANS :", type(c) == child) 

print(dir(base))
print(dir(object))