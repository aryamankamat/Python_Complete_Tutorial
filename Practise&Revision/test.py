import this
# My first program
"""
print("Hello World!");
print("Hey Python, How are you!!!")

"""

# print function

# end="value"
"""
print("Hey Hi", end="")
print("How are you?")
"""

# sep="seprator"
"""
print("Hey hi Pyhon.", "How are you doing?", sep="***")
"""

# Escape sequence characters
"""
print("\' Hey Hi")
print("\" Hey Hi")
print("\\ Hey Hi")
print("Hey Hi \n Hi!!! \t How are you?")
"""

#Varibales in Python
"""
a = 4
# print(a)
b = 33.3
# print(a)
c = "Python"
# print(c)
# to identify the type of value a variable is storing we can use type() function.
# print(type(c))
#ans = a + b
# print(ans)
d = "Hello"
# When two strings are added, they are concatinated
#ans = c + d
# print(ans)
# ans = a + c  #ERROR
# print(ans)   #ERROR
e = "10"
f = "20"
# ans = e + f #concatination will be performed
# print(ans)

"""


#Typecasting in Python
"""
#ans = int(e) + a
# print(ans)
#ans = int(e) + int(f)
# print(ans)

# if we want to print a string multiple times
#print(5 * c)

"""

# String Operations
"""
str = "I am Python"
# print(str[2])
# print(str[0:4])
# print(len(str))
# print(str[0:4:2])
# print(str[:4])
# print(str[0:])

# print(str[-6:])
# print(str[-6:-3])
# print(str[::-1])  # reversing the string

# string methods
# print(str.isalnum())
# print(str.isalpha())
# print(str.endswith("Python"))
# print(str.count("P"))
# print(str.capitalize())
# print(str.find("am"))
# print(str.lower())
# print(str.upper())
#print(str.replace("am", "AM"))
# print(str.split())
#ch = str.split()
# print(ch[0])
# print(ch[1])
# print(ch[2])

str = "I am Python   "
str = str.rstrip()
print(str, "@")
str = "    I am Python"
str = str.lstrip()
print(str)

message = "One of Python's strengths is its diverse community."
print(message)
"""

# Lists
"""
var = ["Aryaman", 2001, 1, 3, "Kamat", 5.2]
# positive
# print(var)
# print(var[0])
# print(var[1])
# print(var[2])
# print(var[3])
# print(var[4])
# print(var[5])
# Negetive indexing
# print(var[-1])
# print(var[-2])
# print(var[-3])
# print(var[-4])
# print(var[-5])
# print(var[-6])
# slicing
# print(var[0:5])
# print(var[:5])
# print(var[:])
# extended slicing
# print(var[::1])
# print(var[::2])
# print(var[::3])
# print(var[::-1])
# print(var[::-2])
# print(var[::-3])
# methods
# print(len(var))
# print(max(var))
# print(min(var))
# var.append(10)
# print(var)
# var.insert(1, 33)
# print(var)
"""

# TUPLES
"""
# var = ("Aryaman", "Kamat", 1, 3, 2001)
# print(var)
# t = (1,)
# print(t)
var = ["Aryaman", 2001, 1, 3, "Kamat", 5.2]
t = tuple(var)
print(t)
"""

# Dictionaries
"""
# d = {"brand": "Ford", "model": "Mustang", "year": 1964}
# print(d)
# print(d["brand"])
# print(d["model"])
# print(d["year"])
# d = {"brand": "Ford", "model": "Mustang", "year": 1964,
    #  "Food": {"nveg": "chicken", "veg": "Paneer"}}
# print(d)
# print(d["Food"])
# print(d["Food"]["veg"])
# print(d["Food"]["nveg"])
# d["Fruit"] = "Apple"
# print(d)
# del d["Food"]
# print(d)
"""

# Set
"""
s = {1, 2, 3, 4, 5}
print(type(s))
"""

# if-else
"""
a = 18
if a >= 18:
    print("Eligible to vote")
else:
    print("Not eligible to vote")
"""
"""
a = 18
if a > 18:
    print("Eligible to vote")
elif a == 18:
    print("The person is of age 18")
else:
    print("Not eligible to vote")
"""
"""
list = [1, 2, 3, 4, 5]
if 8 in list:
    print("yes it is in the list")
else:
    print("No, it is not there in the list")
"""
"""
list = [1, 2, 3, 4, 5]
# print(5 not in list)
if 5 not in list:
    print("yes it is not present in the list")
else:
    print("No, it is present in the list")
"""

# Switch
"""
a = int(input("Enter your choice : "))
match a:
    case 18:
        print("We can think about you!!!")
    case 19:
        print("You can drive only mopaid")
    case 20:
        print("You can drive all types of vehicles!!!")
    case default:
        print("Don't drive, drive cycle!!!")
"""

# for loop
"""
# list = [1, 2, 3, 4, 5]
# for l in list:
#     print(l)

list = [["fruit", "Apple"], ["Food", "roti"], ["snacks", "samosa"]]
# for var in list:
# print(var)


# print("\ncatagory  item")
# print("---------------")
# for catagory, item in list:
# print(catagory, item)

dict = dict(list)
# print(dict)
# for var in dict.items():
# print(var)

# print("\ncatagory  item")
# print("---------------")
# for catagory, item in dict.items():
#     print(catagory, item)
"""


# while loop
"""
i = 0
while (i < 10):
    print(i)
    i += 1
"""

# break statement
"""
i = 0
while (i < 10):
    if i == 5:
        break
    print(i)
    i += 1
"""

# continue statement
"""
i = 0
while (i < 10):
    i += 1
    if i == 5:
        print("Skip to next iteration.")
        continue
    print(i)
"""

# pass statement

"""
l = [1, 23, 4]
for i in l:
    pass
"""

# Operators
"""
# Arithmetic Operators
# print("5 + 6 is ", 5+6)
# print("5 - 6 is ", 5-6)
# print("5 * 6 is ", 5*6)
# print("5 / 6 is ", 5/6)
# print("5 ** 3 is ", 5**3)
# print("5 % 5 is ", 5%5)
# print("15 // 6 is ", 15//6)

# Assignment Operators
# print("Assignment Operators")
# x = 5
# print(x)
# x %=7 # x = x%7
# print(x)

# Comparison Operators
# i = 5
# print(i==5)
# print(i<5)
# print(i>5)
# print(i<=5)
# print(i>=5)


# Logical Operators
# a = True
# b = False

# Identity Operators
# print(5 is not 5)
# print(5 is not 7)

# Membership Operators
# list = [3, 3, 2, 2, 39, 33, 35, 32]
# print(32 in list)
# print(324 in list)
# print(324 not in list)

# Bitwise Operators
# 0 - 00
# 1 - 01
# 2 - 10
# 3 - 11

# print(0 & 2)
# print(0 | 3)
"""

# Short Hand if-else
"""
a = int(input("Enter 1st number : "))
b = int(input("Enter 2nd number : "))
# if a > b:
#     print("a is greater than b")
print("a is greater than b") if a > b else print("b is greater than a")
"""


#Functions in Python
"""
# def add():
#     a = 10
#     b = 20
#     ans = a + b
#     print(ans)

# add()

# def add(a, b):
#     ans = a + b
#     print(ans)

# add(10, 20)

# def add(a, b):
#     ans = a + b
#     return ans
# result = add(10, 20)
# print(result)
"""

# DocString
# def add():
#     """This is a Function which does addition of two integer numbers"""
#     a = 10
#     b = 20
#     ans = a + b
#     print(ans)

# print(add.__doc__)


"""
#The Zen of Python
import this
"""

# format() functions
"""
age = 21
name = "Anil"
print('{0} was {1} year old when he wrote this book'. format(name, age))
"""