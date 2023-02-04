''' A Function with two required positional parameter'''
# def show(roll,name,*marks):
#     print("Roll :", roll)
#     print("Name :", name)
#     #print("Marks :", marks)
#     for mk in marks:
#         print("subject:", mk)
#
# #show(101,'ABC')
# show(101,'ABC',67,45,83)

#Positonal arguments
"""
def showData(roll,name,per):
    print("ROLL NAME PERCENTAGE")
    print(roll,name,per)

showData(101,"ABC",99.9)
"""

''' A Function with any no. of positional parameters '''
def show(*args):
    print("Function called...")
    print("Type of args = ", type(args))
    # print("Elements = ", args)
    print("Elements : ", end=" ")
    for e in args:
        print(e, end=", ")


# show()
show(1,"ABC",3.7)
