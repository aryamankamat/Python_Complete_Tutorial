"""
Write a Python program to create a list of tuples with the first
element as the number and second element as the square of the number.
Expected Output: [(1,1),(2,4),(3,9),(4,16)]
"""
lst = []
while True:
    val = int(input("Enter a number : "))

    if val == 0:
        exit()
    else:
        val1 = val ** 2
        lst.append((val, val1))
        tup = tuple(lst)
        print('List : ', lst)
        # print('Tuple : ', tup)
