"""
Write a Python program to Merge two lists.(Using Built-in function
and without using Built-in functions)
"""
lst1 = [1, 2, 3, 4, 5]
lst2 = [6, 7, 8, 9, 10]

# without using built-in function
lst3 = lst1 + lst2
print("Merged list without using built-in function...", lst3, sep='\n')

# using built-in function
lst4 = []
lst4.extend(lst1)
lst4.extend(lst2)
print("Merged list using built-in function...", lst4, sep='\n')
