"""
Write a program that reads a Celsius degree from
the console and converts it to Fahrenheit and displays the result. The formula for
the conversion is as follows:
fahrenheit = (9 / 5) * celsius + 32 
"""
cel = int(input("Enter temperature in Celsius : "))
Faren = ((9/5) * cel + 32)
print(cel,"Celsius in Fahrenheit is = ",Faren)
