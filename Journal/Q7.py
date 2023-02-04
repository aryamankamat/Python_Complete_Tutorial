d = {1: 10, 2: 20, 3: 30, 4: 40, 5: 50, 6: 60}

def check(i):
    if i in d:
        d.pop(i)
        d.update({"color":"Green"})
        print(d)
    else:
        print("The key is not present.")

check(2)
