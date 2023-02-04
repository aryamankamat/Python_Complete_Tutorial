"""
Write a Python program to add an item in a tuple.
"""
# Logic I
tup = (12, 1, 33, 89, 100)
print("Original tuple : ", tup)
n = int(input("Enter an element : "))
tup = tup + (n,)
print("Updated tuple is displayed below...", tup, sep='\n')


# Logic II
"""
tup = (12, 1, 33, 89, 100)
print("Original tuple : ", tup)

while True:
    print("Press 0 to exit...")
    n = int(input("Enter an element : "))
    if (n == 0):
        exit()
    tup = tup + (n,)
    print(tup)
"""
