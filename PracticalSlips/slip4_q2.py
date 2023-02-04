"""
Write a python program to count repeated characters in a string.
Sample string: 'thequickbrownfoxjumpsoverthelazydog' 
"""
sample_string = input("Enter a string = ")
count = {}

for i in sample_string:
    if i in count.keys():
        count[i] = count[i] + 1
    else:
        count[i] = 1

for k,v in count.items():
    print(k,"=",v)
