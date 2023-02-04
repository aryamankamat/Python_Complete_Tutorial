def checker(s):
    up = 0
    lw = 0
    for i in s:
        if (i.isupper()):
            up = up + 1
        elif (i.islower()):
            lw = lw + 1
        else:
            pass

    print("Original string is = ", s)
    print("No of uppercase characters are = ", up)
    print("No of lowercase characters are = ", lw)


checker('The quick Brown Fox')
