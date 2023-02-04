"""
3. Write a Python script to check if a given key already exists in a
dictionary.
"""
d = {1: 10, 2: 20, 3: 30, 4: 40, 5: 50, 6: 60}

while (True):
    k = int(input("Enter a key to check :(press 0 to exit) "))
    if (k == 0):
        exit(0)

    if k in d:
        print(f"Key {k} is available in the dictionary...")
    else:
        print(f"Key {k} is not available in the dictionary...")
