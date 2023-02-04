"""
#FEARURES OF PYTHON
1. python is simple to code and easy to understand.
2. Python is an interpreted programming language.
3. Python is platform independent programming language.
4. Python is portable in nature.
5. Python is free and open source.
6. Python is Embeddable in nature.
7. Python is Extensible in nature.
8. Python is dynamic in nature.
9. Python is purely an object oriented programming langauge.
10. Python has extensible libraries.
"""

# Display the keywords in python.
"""
import keyword
print("\nThe list of keywords in python are displayed below : \n")
print(keyword.kwlist)
"""
# VARIABLES IN PYTHON
"""
x = 10
y = "Hello"
z = 5.2
print("The value of x is = ", x, ", y is = ", y, ", z is = ", z)
print(type(x))
print(type(y))
print(type(z))
"""
# SIMULTANEOUS ASSIGNMENT
"""
a, b, c = 10, 20, 30
print(a, "\n", b, "\n", c)
"""
# MULTIPLE ASSIGNMENT
"""
a = b = c = 10
print("a is = ", a)
print("b is = ", b)
print("c is = ", c)
"""

# UNPACK A COLLECTION
"""
lst = [1, 23, "hi", "Hello"]
a, b, c, d = lst
print(a)
print(b)
print(c)
print(d)
tup = (22, 44, "ICCS", "Hey")
e, f, g, h = tup
print(e)
print(f)
print(g)
print(h)
"""

# PACKING VARIBALES INTO COLLECTION
"""
a = 10
b = 22
c = "HEY"
lst = []
lst = a, b, c
print(lst)
tup = ()
tup = a, b, c
print(tup)

def mySum(*args):
    return sum(args)


pac = mySum(1, 2, 3, 4, 5)
print(pac)
"""
# id()
"""
#when more than one varibale contains same data/value, 
#python will assign to them the same address/reference.
a = 10
b = 10
print(id(a))
print(id(b))
"""
#DataTypes in Python
"""
1. Text type - str
2. Numeric - int , float, complex number, boolean(0&1)
3. Sequance - list, tuple, range
4. Mapping - Dictonary
5. Set - set, frozenset
6. Boolean - bool
7. Binary - bytes, bytearrya, memoryview
8. None - nonetype
"""

# Typecasting
"""
- Typecasting simply means converting value present in one data type into another data type.
Upcasting :- converting one data type with lesser size/memory into higher size/memory.
                char < int < float < double
Downcasting :- converting one data type with higher size or memory into lesser size/memory, this leads to data loss.
"""
# Typecasting functions

# int() :- This function converts the specified value into integer format.
"""
a = "12345"
ans = int(a)
print(ans)
b = 33.55
print(int(b))
"""
# float() :- This function converts the specified value into floating point format.
"""
a = 10
print(float(a))
b = "123455"
print(float(b))
"""
# str() :- This function converts the specified value into string format.
"""
a = 44
b = str(a)
print("The value of b is = ", b, "and the type of b is = ", type(b))
c = 44.55
d = str(c)
print("The value of c is = ", c, "and the type of c is = ", type(d))
"""
# chr() :- This function return the corresponding character value for the specified ASCII value.
"""
print(chr(65))
print(chr(91))
print(chr(88))
"""
# ord() :- This function return the corresponding ASCII value for the specified character.
"""
print(ord('Z'))
print(ord('a'))
print(ord('z'))
"""
# complex() :- This function creates an complex number from one or two specified numbers.
"""
com = complex(10, 2)
print(com)
a = 33
print(complex(a))
"""
# repr() :- This function creats a printable representation of the given object, it convers the object to an expression string.
"""
lst = [1, 2, 4, 6]
ans = repr(lst)
print(ans)
print(type(ans))
a = 22
ans = repr(a)
print(ans)
print(type(ans))
"""
# eval() :- This function will evaluate the specified string expression.
"""
ans = eval("3+2")
print(ans)
ans1 = eval("22.5+33.5")
print(ans1)
"""
# round() :- This funciton will round off the fractional value.
"""
f = 3.22222
print(round(f))
ans = round(f, 4)
print(ans)
"""

#Oprators in Python

# arithmatic operator
"""
+ - addition
- - subtraction
* - Multiplication 
/ - division(float division)
// - floor division(integer devision)
% - modulus
** - exponentiation

"""
# Assignment operator
"""
They work in both arithmatic and bitwise operands
=  - assignment
+= - add and assign
-= - subtract and assign
*= - multiply and assign
/= - divide and assign
//= - integer divide and assign
%= - modulus and assign
**= - exponentiation and assign
&= - add assign
|= - or assign
^= - xor assign
>>= - right-shift assign
<<= - left-shift assign
"""
# comparison operator
"""
==
!=
>
<
>=
<=
"""
# Logical operators
"""
and
or
not 
"""
# Bitwise operator
"""
& - and
| - or
! - not
^ - xor
~ - once complement(not)
<< - right-shift
>> - left-shift
"""
# identity operators
"""
is 
is not
"""
# Membership operator
"""
in
not in
"""
#print() in python
"""
* print() function in python is used to print the statements/output on the screen.
* print() function has 5 parameters, but we can extend it to 6 parameters as per our understanding.

i) object/statements - we can print more than one values/statements
ii) sep - It specifies how to separate the values, default is " "
iii) end - It specifies what to print at the end, default is '\n' 
iv) file - An object with a write method, default is sys.stdout.
v) flush - It spcifies whether the output is flushed or not.
"""
# Way to print in python
# 1st way
"""
print("hello ICCS")
print("Maharastra")

print("Hello")
print()
print("World")

print("Rahul", 25, "Pune", sep='***')
print("Rahul", 25, "Pune", sep='\n')
"""
# 2 way
"""
name = "Shivaji"
age = 30
print("Welcome"+" ICCS")
print("Welcome " + name + ". You are "+str(age)+" year old")
* The  + is concatination operator, it can be only use with the strings
"""
# 3 way
"""
name = "Shivaji"
age = 30
print("Welcome %s" % name)
print("Hello %s . You are %d year old" % (name, age))
"""
# 4th way
"""
name = "Shivaji"
age = 30
print("Hello {0}. You are {1} year old." . format(name, age))
print(f"Hello {name}. You are {age} year old.")
print("Hello {}. You are {} year old." . format(name, age))
"""

# input() function in python
"""
The input() in python accepts an input from the user and converts it into a string format.
It does not evaluates the expression, It just returns the complete statement as a string. 
"""
"""
a = input("Enter a number : ")
print(type(a))
b = int(input("Enter a number : "))
print(type(b))
c = eval(input("Enter a number : "))
print(type(c))
print(c)
ch = input("Enter a character : ")
print(ch[0])
ch = input("Enter a character : ")[0]
print(ch)
"""
# if-else
"""
if(condition):
    statement1
    statement2
else:
    statement3
"""
# if-elif-else
"""
if(condition):
    statement1
elif(condition):
    statement
else:
    statement
"""
# while loop
"""
while(condition):
    statement
    statement

    incre/decre
"""
# while-else
"""
while(condition):
    statement
    statement

    incre/decre
else:
    statement
"""
# for loop & for-else & range()
"""
* for loop must be used only with the sequences
for [variable] in [sequence]:
    statement
else:
    statement

for [variable] in range():
    statement
else:
    statement
"""
# Accept multiple values in one line
# method 1
"""
print("Enter two numbers : (use enter key)")
n1, n2 = int(input()), int(input())
print(f"The value of n1 is = {n1} and n2 is = {n2}")
"""
# mehtod 2
"""
n1, n2, n3 = input("Enter three number of your choice : ").split()
print(f"The value of n1 is = {n1}, n2 is = {n2} and n3 is = {n3}")
print(type(n1), type(n2), type(n3))
"""

# Escape sequences
# \n \\ \t \b \a \" \' \f \ooo \xhh
"""
a = 'He said,"Hello"'
print(a)
b = 'He said,\"Hello\"'
print(b)
c = "It's quite funny"
print(c)
d = "It\'s quite funny"
print(d)
e = "D:\\aryaman\\time\\backup.txt"
print(e)
f = r"D:\aryaman\time\backup.txt"
print(f)
"""

#Strings in python
"""
* String is a sequence/collection of characters.
* Strings are immutable(non-changable) in nature.
* Strings are ordered in nature.
* A string is a collection of substrings.

* Types of strings:
    (i) Single-line strings - ' '," "
    (ii) Multi-line strings - ''' ''',""" """
"""
# ways to create a string
"""
s1 = 'Hello'
print(s1)
s2 = "Hello Aryaman"
print(s2)
s3 = '''Indira college,
wakad.
'''
print(s3)
#s4 = """
# Buddha goush housing society,
# old sangavi.
"""
print(s4)
"""

# Operations on strings
# 1)Concatination
"""
name = "Aryaman"
lname = "Kamat"
ans = name + lname
print(ans)
"""

# 2)String repetition
"""
name = "Anil"
ans = name * 5
print(ans)
"""

# 3)Using membership operator
"""
s = "indira"
ans = 'i' in s
print(ans)
ans2 = 'i' not in s
print(ans2)
"""

# 4)Indexing operations
"""
s = "indira"
print(s[2])  # positive indexing
print(s[-4])  # negative indexing
ans = s[2] = 'x' #ERROR{strings are immutable in nature}
"""

# 5)Sting slicing
"""
syntax: [start:stop:step]
        - start :- inclusive and defalut is 0
        - stop :- exclusive
        - step :- default is 1
"""
"""
s = "indira"
s1 = s[0:3]
print(s1)
s2 = s[2:5]
print(s2)
s3 = s[:4]
print(s3)
s4 = s[3:]
print(s4)
s5 = s[::]
print(s5)
s6 = s[::2]
print(s6)
s7 = s[::-1] #To print the string in reverse order.
print(s7)
"""
# 6)Iterating over a string
"""
s = "indira"
for i in s:
    print(i)
else:
    print("End of the string")


s = "indira"
for i in s:
    print(i)
    if (i == 'n'):
        break
else:
    print("End of the string")


s = "indira"
for i in s:
    if (i == 'n'):
        continue
    print(i)
else:
    print("End of the string")
"""
# String Built-in Functions

# 1)Capitalize() :- This function converts the first character of a string to uppercase.
"""
s = "I am Aryaman"
cap = s.capitalize()
print(cap)
"""
# 2) title() :- This function converts the first character of every word present in a string to uppercase.
"""
s = "I am Aryaman"
ti = s.title()
print(ti)
"""
# 3)count() :- This function will count the number of specified characters/sub-strings present in an entire string
"""
s = "Rajanikanth"
cnt = s.count('a')
print(cnt)
cnt1 = s.count('an')
print(cnt1)
"""
# 4) index() :- This function will return the index value of first occurace of specified sub-string.
#               If the specified value is not present in the string then the index() will through an errr.
"""
s = "Rajanikanth"
ind = s.index('a')
print(ind)
ind1 = s.index('an')
print(ind1)
ind2 = s.index('x') #ERROR
print(ind2)
"""
# 5) rindex() :- This function will return the index value of last occurace of specified sub-string.
#                If the specified value is not present in the string then the index() will through an errr.
"""
s = "Rajanikanth"
rind = s.rindex('a')
print(rind)
rind1 = s.rindex('an')
print(rind1)
rind2 = s.rindex('x') #ERROR
print(rind2)
"""
# 6) find() :- This function works same as index(), It will return the index value of first occurace of specified sub-string.
#              If the specified value is not present in the string then it will retrun -1.
"""
s = "Rajanikanth"
f = s.find('a')
print(f)
f1 = s.find('an')
print(f1)
f2 = s.find('x') # -1 for not present in the string
print(f2)
"""
# 7) rfind() : This function works same as rindex(), It will return the index value of last occurace of specified sub-string.
#              If the specified value is not present in the string then it will retrun -1.
"""
s = "Rajanikanth"
rf = s.rfind('a')
print(rf)
rf1 = s.rfind("an")
print(rf1)
rf2 = s.rfind('x')  # -1 for not present in the string
print(rf2)
"""
# 8) startswith() :- This function will retrun True if the string starts with the specifed value.
"""
s = "Rajanikanth"
sw = s.startswith('R')
print(sw)
sw1 = s.startswith('Raj')
print(sw1)
"""
# 9) endswith() :- This function will return True if the string ends with the specified value.
"""
s = "Rajanikanth"
ew = s.endswith("h")
print(ew)
ew1 = s.endswith("anth")
print(ew1)
"""
# 10) lower() :- This function coverts a string into lower case.
"""
s = "Rajanikanth"
lw = s.lower()
print(lw)
"""
# 11) upper() :- This function coverts a string into upper case.
"""
s = "Rajanikanth"
up = s.upper()
print(up)
"""
# 12) swapcase() :- This function will convert the character present in lowercase to uppercase and vice versa.
"""
s = "Rajanikanth"
sc = s.swapcase()
print(sc)
"""
# 13) replace() :- This function will replace a sub-string as per the specified value from the existing string
"""
s = "Rajanikanth"
rep = s.replace('a', '@')
print(rep)
rep1 = s.replace('an', 'xxx')
print(rep1)
rep2 = s.replace('a', '@', 2)
print(rep2)
"""
# 14) len() :- This function will find the lenght of a string
"""
s = "Rajanikanth"
l = len(s)
print(l)
"""
# 15) lstrip() :- This function will trim/remove the blank spaces from the left side.
"""
s = "  Hello"
print(s)
s1 = s.lstrip()
print(s1)
"""
# 16) rstrip() :- This function will trim/remove the blank spaces from the right side.
"""
s = "  Hello     "
print(s)
rs = s.rstrip()
print(rs)
"""
# 17) strip() :- This function will trim/remove the blank spaces from both left&righ side.
"""
s = "  Hello     "
st = s.strip()
print(st)
"""
# 18) split() :- This function will split/seperate a string at a specifed seperator and return a list.
"""
s = "I Love India"
sp = s.split()
print(sp)
print(type(sp))
print(len(sp))
a = "Rajanikanth"
sp1 = a.split('a')
print(sp1)
sp2 = a.split('a', 2)
print(sp2)
"""
# 19) rsplit() :- This function will split/seperate a string at a specified seperator from righ-to-left and return a list.
"""
a = "Rajanikanth"
rsp = a.rsplit('a')
print(rsp)
rsp = a.rsplit('a', 2)
print(rsp)
"""
# 20) partition() :- This function will search for a specfied character/sub-string and split the string into a tuple, containing three elemnts(before string, specified char/sub-str, remaining string)
"""
a = "Rajanikanth"
par = a.partition('i')
print(par)
print(type(par))
print(len(par))
par1 = a.partition('an')
print(par1)
"""
# 21) rpartiotion() :- This function will search for a specifed character/sub-string from right-to-left and split the string into a tuple.
"""
a = "Rajanikanth"
rpar = a.rpartition('an')
print(rpar)
"""
# 22) ljust() :- This function return the left justified version of a string.
"""
s = "india"
j = s.ljust(10, '*')
print(j)
"""
# 23) rjust() :- This function returns the right justified version of a string.
"""
s = "india"
j1 = s.rjust(10, "#")
print(j1)
"""
# 24) center() :- This function will return the centered justifed version of a stirng.
"""
s = "india"
jc = s.center(9, '$')
print(jc)
"""
# 25) isdecimal() :- This function will return True if all the characters in a string are decimal.
"""
s = '22312'
ans = s.isdecimal()
print(ans)
s1 = '22312abc'
ans1 = s1.isdecimal()
print(ans1)
"""
# 26) isnumceric() :- This function will return True if all the charcters are numberic in nature.
"""
s = '22312'
ans = s.isnumeric()
print(ans)
s1 = '22312abc'
ans1 = s1.isnumeric()
print(ans1)
"""
# 27) isalpha() :- This function will return True if all the characters of a string are alphabets.
"""
s = "indira"
ans = s.isalpha()
print(ans)
s1 = 'indira123'
ans1 = s1.isalpha()
print(ans1)
"""
# 28) isalnum() :- This function will return True if all the characters of a string are alphanumeric.
"""
s = 'abc1234'
ans = s.isalnum()
print(ans)
s1 = 'abc'
ans1 = s1.isalnum()
print(ans1)
s2 = '123'
ans2 = s2.isalnum()
print(ans2)
"""
# 29) isprintable() :- This function will return True if all the characters of a string are printable in nature.
"""
s = '\n'
ans = s.isprintable()
print(ans)
s1 = '*'
ans1 = s1.isprintable()
print(ans1)
"""
# 30) isidentifier() :- This function will return True of string is an identifier(can be a variable).
"""
s = "ACCNO"
ans = s.isidentifier()
print(ans)
s1 = "12ACCNO"
ans1 = s1.isidentifier()
print(ans1)
s2 = "_ACCNO"
ans2 = s2.isidentifier()
print(ans2)
s3 = "PHP_LANG"
ans3 = s3.isidentifier()
print(ans3)
"""
# 31) isspace() :- This function will return True if all the characters in a string are white spaces.
"""
s = "   "
ans = s.isspace()
print(ans)
s1 = " \t "
ans1 = s1.isspace()
print(ans1)
s2 = "  a   \t"
ans2 = s2.isspace()
print(ans2)
"""
# 32) isupper() :- This function will return True if all the characters in a string are in uppercase.
"""
s = "ICCS"
ans = s.isupper()
print(ans)
s1 = "iCcS"
ans1 = s1.isupper()
print(ans1)
"""
# 33) islower() :- This function will return True of all the characters in a string are in lowercase.
"""
s = "iccs"
ans = s.islower()
print(ans)
s1 = "ICCS"
ans1 = s1.islower()
print(ans1)
"""
# 34) join() :- This fuction will take all the items from an iterable and convert them into a string.
"""
lst = ['indira', 'college', 'of', 'commerce', 'and', 'science']
ans = " ".join(lst)
print(ans)
ans = '#'.join(lst)
print(ans)
ans = "**".join(lst)
print(ans)
Dict = {"name": "John", "country": "Norway"}
sep = "TEST"
x = sep.join(Dict)
print(x) # When joining dictionry, the retured values are the keys, not the values.
"""


# LIST
"""
* List is a squence or collection of elements.
* List is mutable in natue.
* List is ordered in nature.
* The elements present in a list can be homogenous or hetrogenous.
* The elements in a list can be of mutable and immutable nature.
"""
# ways to create a list
"""
lst1 = []
print(lst1)
print(type(lst1))
lst2 = list()
print(lst2)
lst3 = [56, 12, 22, -14, 45]
print(lst3)
print(type(lst3))
lst4 = lst3
print(lst4)
tup = (7, 2, 3, 55, 67)
lst5 = list(tup)
print(lst5)
myset = {10, 22, 6, -2, 7, 1, -2}
lst6 = list(myset)
print(lst6)
lst7 = list('Indira')
print(lst7)
"""
# Operations on a list

# 1)Concatination
"""
lst1 = [3, 2, "Hello"]
lst2 = [6.2, "Hi", 5.6, 11]
ans = lst1 + lst2
print(ans)
"""
# 2)List repetation
"""
lst = [3, 2, "Hello"]
rep = lst * 3
print(rep)
"""
# 3) Using membership operator
"""
lst2 = [6.2, "Hi", 5.6, 11]
ans = "Hi" in lst2
print(ans)
"""
# 4) Indexing operation
"""
lst2 = [6.2, "Hi", 5.6, 11, 8]
print(lst2[1])
print(lst2[-4])
"""
# 5) Slicing operation
"""
lst2 = [6.2, "Hi", 5.6, 11, 8]
print(lst2[::])
print(lst2[1:4])
"""
# 6) Updation operation
"""
lst = [5, -1, 8, 11, 6, 9, 15]
lst[3] = 'Indira'
print(lst)
"""
# 7) Deletion operation
"""
lst = [5, -1, 8, 11, 6, 9, 15]
del lst[4]
print(lst)
"""
# 8) Iterating over a list
# using for loop
"""
lst = [10, 22, 3, 4, 5, 66, 77, 89, 100]
for i in lst:
    print(i)
"""
# using while loop
"""
lst = [10, 22, 3, 4, 5, 66, 77, 89, 100]
i = 0
while (i < len(lst)):
    print(lst[i])
    i = i+1
"""

# Built-in functions of List
# 1)max() :- This function return the maximum value from a list.
"""
lst = [10, 22, 3, 4, 5, 66, 77, 89, 100]
ans = max(lst)
print(ans)
"""
# 2) min() :- This function return the minimum value from a list.
"""
lst = [10, 22, 3, 4, 5, 66, 77, 89, 100]
ans = min(lst)
print(ans)
"""
# 3) len() :- This function returns the total length of a list
"""
lst = [10, 22, 3, 4, 5, 66, 77, 89, 100]
ans = len(lst)
print(ans)
"""
# 4) sum() :- This function will add all the homogenous elements from a list.
"""
lst = [10, 22, 3, 4, 5, 66, 77, 89, 100]
ans = sum(lst)
print(ans)
"""
# 5) all() :- This function will return True if all the items present in a iterable are true/positive.
"""
lst = [10, 22.5, 3, 0.0001, 5]
ans = all(lst)
print(ans)
lst1 = [10, 22.5, 3, 0.000, 5]
ans1 = all(lst1)
print(ans1)
"""
# 6) any() :- This function will return True if any one item present in a iterable is true/positive.
"""
lst = [10, 22.5, 3, 0.0001, 5]
ans = any(lst)
print(ans)
lst1 = [False, 0, None, [], {}, (), ""]
ans1 = any(lst1)
print(ans1)
lst2 = [False, 0, None, [], {}, (), "", 56]
ans2 = any(lst2)
print(ans2)
"""
# 7) append() :- This function will add elements at the end of a list(it will add the element as it is,entirely).
"""
lst = [10, 22, 3, 4, 5, 66, 77, 89, 100]
lst.append(150)
print(lst)
lst.append([11, 22, 33])
print(lst)
"""
# 8) extend() :- This function demands for iterable and appends the elements of the iterable into the list individually.
"""
lst = [10, 22, 3, 4, 5, 66, 77, 89, 100]
lst.extend([11, 22, 44, 55])
print(lst)
"""
# 9) insert() :- This function inserts a value at a specified position.
"""
lst = [10, 22, 3, 4, 5, 66]
lst.insert(2, 'ICCS')
print(lst)
lst.insert(9, 'Hello') # python will add at the end.
print(lst)
"""
# 10) pop() :- This function deletes the element at a specified position, by defalut it will delete the last element.
"""
lst = [10, 22, 3, 4, 5, 66]
lst.pop()
print(lst)
lst.pop(3)
print(lst)
"""
# 11) remove() :- This function deletes the first occurace of specified value.
"""
lst = [10, 2, 22, 3, 2, 4, 5, 66]
lst.remove(2)
print(lst)
"""
# 12) sort() :- This function will sort the values present into list if the list contains homogenous elements.
"""
lst = [10, 2, 22, 3, 2, 4, 5, 66]
lst.sort()
print(lst)
lst.sort(reverse=True)
print(lst)
"""
# 13) reverse() :- This function will reverse the list after sorting the elements.
"""
lst = [10, 2, 22, 3, 2, 4, 5, 66]
lst.reverse()
print(lst)
"""
# 14) copy() :- This function will create a shallow copy of the list.
"""
lst = [10, 2, 22, 3, 2, 4, 5, 66]
lst2 = lst.copy()
print(lst2)
print(id(lst), " and ", id(lst2))
"""
# 15) index() :- This function will return the index of first occurance of specified value.
"""
lst = [10, 2, 22, 3, 2, 4, 5, 66]
ans = lst.index(2)
print(ans)
"""
# 16) clear() :- This function will remove/delete all the elements from the list.
"""
lst = [10, 2, 22, 3, 2, 4, 5, 66]
lst.clear()
print(lst)
"""

#TUPLE in python
"""
* Tuple is a sequence or collection of elements
* Tuple is immutable in nature.
* Tuple is ordered in nature.
* The elements present in a tuple can be homogenous or hetrogenous.
* The elements present in a tuple can be mutable or immutable.
"""

# ways to create a tuple
# () - using symbole
# tuple() - using built-in function
"""
tup1 = ()
print(tup1)
print(type(tup1))
tup2 = tuple()
print(tup2)
tup3 = (6, 1, 8, 9, 4)
print(tup3)
tup4 = tup3
print(tup4)
lst = [12, 33, 56, 74]
tup5 = tuple(lst)
print(tup5)
myset = {7, 33, 90, 2, 44, 2, 55}
tup6 = tuple(myset)
print(tup6)
tup7 = tuple('indira')
print(tup7)
tup8 = ("ICCS",)
print(tup8)
"""
# Operations on a tuple
# 1) Indexing
"""
tup = (1, 3, 7, 8, 7, 5, 4, 6, 8, 5)
print(tup[3])
print(tup[-2])
"""
# 2) Slicing
"""
tup = (1, 3, 7, 8, 7, 5, 4, 6, 8, 5)
print(tup[::-1])
print(tup[1:5:])
print(tup[::2])
print(tup[1::])
print(tup[:-1:])
# tuple packing
"""
# 3) Iterating over a tuple
#   using for loop
"""
tup = (1, 3, 7, 8, 7, 5, 4, 6, 8, 5)
for i in tup:
    print(i)
"""
#   using while loop
"""
tup = (1, 3, 7, 8, 7, 5, 4, 6, 8, 5)
i = 0
while (i < len(tup)):
    print(tup[i])
    i += 1
"""

"""
tup = 25, 'Pune', 'IccS', 66.4, 99.9
print(tup)    
"""
# tuple unpacking
"""
tup = (22, 'Pune', 'Indira', 99.9)
a, b, c, d = tup
print(a, b, c, d)
"""

# Built-in functions
# 1) count() :- This function will return the number of times a specified value appears into the tuple.
"""
tup = (1, 3, 7, 8, 7, 5, 4, 6, 8, 5)
ans = tup.count(5)
print(ans)
"""
# 2) index() :- This function will return the index of first occurance of specified value.
"""
tup = (1, 3, 7, 8, 7, 5, 4, 6, 8, 5)
ans = tup.index(8)
print(ans)
"""

#SET in python
"""
* A set is a collectipn of elements.
* The elements of a set are also known as keys.
* The elements of a set can be homogenous or hetrogenous.
* The set is unordered in nature.
* The set contains only distinct elements(duplicate elements are not allowed)
* The set is mutable in nature.
* All elements of the set must be immutable.
* syntax : 
   - {}
   - set()
"""
# ways to create a set
"""
s1 = {}
print(s1)
print(type(s1))
s2 = set()
print(s2)
s3 = {6, 1, 22, 6.5, 9-2j, "Hello"}
print(s3)
s4 = set(s3)
print(s4)
lst = [6, 22, 123, 45, 66]
s5 = set(lst)
print(s5)
tup = (5, 1, 4, 6, 89, 20)
s6 = set(tup)
print(s6)
s7 = set('malayalam')
print(s7)
s8 = {6, 1, (1, 23, 4), "Hello", 5.6, 4+3j}
print(s8)
s9 = {6, 1, [1, 23, 4], "Hello", 5.6, 4+3j}  # ERROR
s10 = {6, 1, {1, 23, 4}, "Hello", 5.6, 4+3j}  # ERROR
"""
# Operations on set
# 1) using membership operator
"""
s3 = {6, 1, 22, 6.5, 9-2j, "Hello"}
ans = 22 in s3
print(ans)
"""
# 2) iterating over a set
# using for loop
"""
s3 = {6, 1, 22, 6.5, 9-2j, "Hello"}
for i in s3:
    print(i)
"""
# Built-in function of set
# 1) difference :- This function will return the differece between two set.
"""
s1 = {4, 1, 8, 2}
s2 = {8, 2, 5, 9, 3}
sd = s1 - s2
print(sd)
sd2 = s1.difference(s2)
print(sd2)
"""
# 2) union() :- This function will return the union of sets.
"""
s1 = {3, 1, 8, 2, 4}
s2 = {5, 4, 9, 3}
su = s1 | s2
print(su)
su2 = s1.union(s2)
print(su2)
"""
# 3) intersection() :- This function will return a set which is the intersection of two or more sets.
"""
s1 = {3, 1, 8, 2, 4}
s2 = {5, 4, 9, 3}
si1 = s1 & s2
print(si1)
si2 = s1.intersection(s2)
print(si2)
"""
# 4) symmetric_differece() :- This function will return a set with the seymmetric differece of two sets.
"""
s1 = {3, 1, 8, 2, 4}
s2 = {5, 4, 9, 3}
sd1 = s1 ^ s2
print(sd1)
sd2 = s1.symmetric_difference(s2)
print(sd2)
"""
# 5) isdisjoint() :- This function will check whether two sets have a intersection or not.
"""
s1 = {3, 1, 8, 2, 4}
s2 = {9, 7, 6}
ans = s1.isdisjoint(s2)
print(ans)
"""
# 6) issuperset() :- This function will return True if one set contains another set.
"""
s3 = {5, 9, 8, 2}
s4 = {2, 5}
ans1 = s3 > s4
ans2 = s3.issuperset(s4)
print(ans1, ans2)
"""
# 7) issubset() :- This function will return True if another set conatins this set.
"""
s3 = {5, 9, 8, 2}
s4 = {2, 5}
ans1 = s4 < s3
print(ans1)
ans2 = s4.issubset(s3)
print(ans2)
"""
# 8) add() :- This function will accept only one element and add to the set.
"""
s3 = {5, 9, 8, 2}
s3.add(10)
print(s3)
"""
# 9) update() :- This function demands for an iterable and add the value by reading them one-by-one to the set.
"""
s3 = {5, 9, 8, 2}
s3.update([1.5, 10.2, 66.5])
print(s3)
"""
# 10) discard() :- This function will delete a specified key value from the set.
#                  It will always return None eve after the deletion of elemet.
""" 
s3 = {5, 9, 8, 2}
ans = s3.discard(8)
print(ans)
print(s3)
"""
# 11) pop() :- This function will delete any random element from the set.
"""
s3 = {5, 9, 8, 2}
s3.pop()
print(s3)
s3.pop()
print(s3)
"""
# 12) remove() :- This function will remove the specified value from the set.
"""
s3 = {5, 9, 8, 2}
s3.remove(2)
print(s3)
"""

#Frozenset in Python
"""
* frozenset in python is just like a set, the only differece is that it is immutable in nature.
* syntax : 
            frozenset()
"""
# way to create a frozenst
"""
lst = [6, 1, 2, 46, 3, 9, 6]
fz = frozenset(lst)
print(fz)
"""

#Dictionary in Python
"""
* A Dictionary is the collection of key-value pair.
* The key's must be unique in nature.
* The values can be same/duplicate/repeated and they can be mutable or immutable.
* The key's must be immutable in nature.
* A Dictionary is orderd in nature.
* syntax : 
    (i) {key : value1, key : value1, etc...}
    (ii) dict() 
"""
# ways to create a dictonary
"""
d1 = {}
print(type(d1))
d2 = dict()
print(d1, type(d1))
d3 = {1: 'ABC', 2: 'PQR', 3: 'XYZ', 4: 'PQR', 5: 'LMN'}
print(d3)
# The value will be replaced with the recent value, it will not throw an error.
d3 = {1: 'ABC', 2: 'PQR', 3: 'XYZ', 4: 'PQR', 5: 'LMN', 3: 'XXX'}
print(d3)
lst = [[1, 1], [2, 4], [3, 9]]
d4 = dict(lst)
print(d4)
tup = ((1, 1), (2, 4), (3, 9))
d5 = dict(tup)
print(d5)
lst_tup = [('MH', 'Mumbai'), ('GA', 'Panji'), ('UP', 'Lacknow')]
d6 = dict(lst_tup)
print(d6)
mixed_mode = ([1, 'ABC'], [2, 'PQR'])
d7 = dict(mixed_mode)
print(d7)
d8 = dict(roll=101, name='Rahul', per=6.7, city='Pune')
print(d8)
"""


"""
# Access the dictonary values
d = {'roll': 101, 'name': "Rahul", 'per': 6.7}
print(d['name'])
# Updating the values
d['per'] = 99.9
print(d)
# Adding the new key and value
d['city'] = 'Pune'
print(d)
# Deleting the key&value
del d['per']
print(d)
"""
"""
#ERROR - dictionary must have key as a immtable value, and it should be a single value.
temp = {[10, 20]: "ABC"}
print(temp)
"""
# Nested dictionary
"""
stud = {
    1: {'roll': 101, 'name': 'OM'},
    2: {'roll': 102, 'name': 'Dustin'},
    3: {'roll': 103, 'name': 'Well'}
}
# print(stud)
# print("2nd record is = ", stud[2])
# print("2nd record is = ", stud[2]['name'])
stud[3]['city'] = 'Pune'
# print(stud)
print("3rd record is = ", stud[3])
"""
# Buit-in functions
# 1) get() :- This funcition will return the value of specified key.
"""
d3 = {1: 'ABC', 2: 'PQR', 3: 'XYZ', 4: 'PQR', 5: 'LMN', 3: 'XXX'}
print("The value of 5th key is = ", d3.get(5))
ans = d3.get(2)
print(ans)
ans1 = d3.get(6)
print(ans1)
print(d3.get(6, "Sorry the data is not available")) # we can provide a modified error message.
"""
# 2) keys() :- This function return the list of all the keys present in our dictionar.
"""
d3 = {1: 'ABC', 2: 'PQR', 3: 'XYZ', 4: 'PQR', 5: 'LMN', 3: 'XXX'}
ans = d3.keys()
print(ans)
"""
# 3) values() :- This function will return the list of all the values present in out dictionary.
"""
d3 = {1: 'ABC', 2: 'PQR', 3: 'XYZ', 4: 'PQR', 5: 'LMN', 3: 'XXX'}
ans = d3.values()
print(ans)
"""
# 4) items() :- This function will return a list which contains a tuple of each key-value pair.
"""
d3 = {1: 'ABC', 2: 'PQR', 3: 'XYZ', 4: 'PQR', 5: 'LMN', 3: 'XXX'}
ans = d3.items()
print(ans)
"""
# 5) pop() :- This function will remove the value of spcified key.
"""
d3 = {1: 'ABC', 2: 'PQR', 3: 'XYZ', 4: 'PQR', 5: 'LMN', 3: 'XXX'}
ans = d3.pop(4)
print(ans)
print(d3)
# ans1 = d3.pop(6)
# print(ans1)
ans2 = d3.pop(6, "Sorry the data is not available.")
print(ans2)
"""
# 6) popitem() :- This function will remove the last inserted key-value pair.
"""
d3 = {1: 'ABC', 2: 'PQR', 3: 'XYZ', 4: 'PQR', 5: 'LMN', 3: 'XXX'}
ans = d3.popitem()
print(ans)
print(d3)

"""
# 7) update() :- This function will update the dictionary with spcified key-value pair.
"""
d3 = {1: 'ABC', 2: 'PQR', 3: 'XYZ', 4: 'PQR', 5: 'LMN', 3: 'XXX'}
#d = {8: 'ICCS', 9: 'indira'}
# d3.update(d)
# print(d3)
d3.update({10: 'AAA'})
print(d3)
"""
