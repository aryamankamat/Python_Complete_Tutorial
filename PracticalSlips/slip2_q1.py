"""
Write a Python program to check if a given key already exists in a dictionary. If
key exists replace with another key/value pair. 
"""
d = {1: 10, 2: 20, 3: 30, 4: 40, 5: 50, 6: 60}


def check(i):
    if i in d:
        d.pop(i)
        d.update({7: 70})
        print(d)
    else:
        print("The key is not present.")


if __name__ == '__main__':
    check(2)
