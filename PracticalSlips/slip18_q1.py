s = input("Enter a string = ")
result = ""
for i in range(len(s)):
    if i % 2 == 0:
        result = result + s[i]
print(result)
