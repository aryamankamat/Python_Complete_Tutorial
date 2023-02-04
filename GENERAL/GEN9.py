"""
9. Write a Python program to parse a string to Float or Integer.
"""
text = input("Enter a number : ")
Tofloat = float(text)
Toint = int(text)
print("The string to float value is = ",
      Tofloat, "and type is = ", type(Tofloat))
print("The string to Integer value is = ",
      Toint, "and type is = ", type(Toint))
