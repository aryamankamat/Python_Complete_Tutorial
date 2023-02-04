def String_check(s):
    d = {"Upper_case": 0, "Lower_case": 0}

    for i in s:
        if i.isupper():
            d["Upper_case"] = d["Upper_case"] + 1
        elif i.islower():
            d["Lower_case"] = d["Lower_case"] + 1
        else:
            pass

    print("Original String is = ", s)
    print("No.of upper case characters is = ", d["Upper_case"])
    print("No.of Lower case characters is = ", d["Lower_case"])


String_check("The quick Brown Fox")
