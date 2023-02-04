# def show(**kwargs):
#     print("Function is called...")
#     print("Type of kwargs = ", type(kwargs))
#     print("The Elements are = ",kwargs)
#     print()
#     for k,v in kwargs.items():
#         print(f"{k} = {v}")
#
# show(roll = 101,name="ABC",per=99.9,city = "Pune")

#With two compulory arguments

def show(roll, name, **kwargs):
    print("Function is called...")
    print("Roll = ",roll)
    print("Name = ", name)
    print("Type of kwargs = ", type(kwargs))
    print("The Elements are = ",kwargs)
    print()
    for k,v in kwargs.items():
        print(f"{k} = {v}")

# show(roll=101,name="Aryaman")
show(roll = 101,name="ABC",phy = 88,chem=89,maths = 90)
