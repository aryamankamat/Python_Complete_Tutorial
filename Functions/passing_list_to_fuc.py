def check(lst):
    evencnt = 0
    oddcnt = 0

    for i in lst:
        if i % 2 == 0:
            evencnt = evencnt + 1
        else:
            oddcnt = oddcnt + 1

    return evencnt , oddcnt


lst =[20,25,14,19,16,24,28,88,44]
evencnt , oddcnt = check(lst)
print("Number of even number is = ",evencnt)
print("Number of odd number is = ",oddcnt)