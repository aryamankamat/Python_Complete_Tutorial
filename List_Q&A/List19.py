"""
 Write a Python program to Interchange First and Last Element of a List.
"""
lst = [1, 29, 51, 7, 23]
print("Original list...", lst, sep='\n')
lst[0], lst[-1] = lst[-1], lst[0]
print("Updated list...", lst, sep='\n')
