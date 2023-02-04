''' This program displays the number of keywords present in python'''
""" This program displays the number of keywords present in python"""

#import keyword

#print("The list of keywords is : ")
# print(keyword.kwlist)

''' To check the location of a variable, we can use id()'''
#num = 10
# print(id(num))
# 3233934737936

''' Both the variable have the same location id/reference '''
#a = 10
# print(id(a))
#b = a
# print(id(b))


''' Data types in Python '''

# Numeric
'''
a = 10
print(type(a))
b = 5.2
print(type(b))
c = 2+4j
print(type(c))
d = True
print(type(d))
e = int(d)
#print(type(e))
print(e)
f = False
g = int(f)
#print(type(g))
print(g)
'''

# Sequence
'''
lst = [1,2,3,4,5]
print(type(lst))
tup = (1,23,4,5,6)
print(type(tup))
st = {1,23,344,5,6}
print(type(st))
rg = range(6)
print(list(rg))
print(type(rg))
'''

# String
"""
str = "Aryaman"
print(type(str))
char = 'A'
print(type(char))
"""

# Mapping(dictionary)
'''
dct = {'Name':'Aryaman','age':25,'BD':'01.03.2001'}
print(dct)
print(type(dct))
'''

# Binary
'''
bi = bytes(10)
print(bi)
print(type(bi))
biary = bytearray(10)
print(biary)
print(type(biary))
x = memoryview(bytes(10))
print(x)
print(type(x))
'''

# None
'''
x = None
print(type(x))
'''


# Type Casting
# int()
'''
a = "12112"
b = int(a)
print(type(b))
c = 23.44
d = float(c)
print(type(d))
'''
# float()
'''
a = "122212"
b = float(a)
print(type(b),"The value is = ",b)
c = 54
d = float(c)
print(type(c),"The vlaue is = ",d)
'''
# str()
'''
a = 45
b = 33.55
c = str(a)
d = str(b)
print(type(c),"the value is = ",c)
print(type(d),"the value is = ",d)
'''


# Number System
'''
num = 45
print("The number in octal form = ",oct(num))
print("The number in binary form = ",bin(num))
print("The number in hexadecimal form = ",hex(num))
'''

#Operators in Python
# 1.Arithmatic operator
'''
a = 10
b = 20
add = a + b
print("The addition is = ",add)
sub = a - b
print("The subtraction is = ",sub)
mult = a * b
print("The multiplication is = ",mult)
div = a / b
print("The division is = ",div)
mod = a % b
print("The reminder is = ",mod)
expo = a ** 2
print("The power is = ",expo)
floor = a // b
print("The integer devision is = ",floor)
'''
# Assignment operator
'''
a = 10
b = 20
c = 30
d = 40
e = 50
f = 60
g = 70
#print("Initial a is = ",a)
a += 2
print("Addition assignment = ",a)
b -= 2
print("Subraction assignment = ",b)
c *= 2
print("Multiplication assignment = ",c)
d /= 2
print("division assignment = ",d)
e %= 2
print("Remender assignment = ",e)
f //= 2
print("Floor assignment = ",f)
g **= 2
print("exponent assignment = ",g)
'''
# Relational/comparision operator
'''
ans = 10 == 10
print(ans)
ans = 10 > 20
print(ans)
ans = 10 < 20
print(ans)
ans = 34 != 40
print(ans)
'''
# Logical Operator
'''
ans = 10 > 2 and 11 > 2
print(ans)
ans = 22 > 100 and 12 > 3
print(ans)
ans = 22 > 100 and 12 > 3
print(ans)
ans = 0 or "Hi"
print(ans)
ans = 0.0 and "Hi"
print(ans)
'''
# Bitwise operator
'''
print("The once complement of 12 is = ",~12)
print("The once complement of 42 is =",~42)
print("The bitwise and operation of 12&13 is = ",12&13)
print("The bitwise and operation of 41&54 is = ",41&54)
12 | 13
13
41 | 54
63
bin(25)
'0b11001'
bin(30)
'0b11110'
0b11000
24
25 & 30
24
0b0001
1
0b00111
7
25^30
7
bin(10)
'0b1010'
0b101000
40
10 << 2
40
0b1100100000
800
25 << 5
800
0b0010
2
0b00000
0
25 >> 5
0
bin(20)
'0b10100'
'''

#while loop
"""
i = 1
while(i <= 5):
    print("Hello",end="")
    j = 1
    while(j <= 4):
        print("Python",end="")
        j = j+1
        
    i = i+1
    print()
"""
"""
i = 1
while(i <= 5):
    print("Hello")
    i = i+1
else:
    print("This is not part of the program")
"""
#for loop
"""
for i in range(10,0,-1):
    print(i)
"""

#Accept multiple values on one line.
#metod1
"""
print("Enter the number below...")
n1,n2 = int(input()),int(input())
print("The values are = ",n1,"and",n2)
"""
#method2
fname,mname,lname = input("Enter your full name : ").split()
print("User name = ",fname,mname,lname)
print(fname)
print(mname)
print(lname)
