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
