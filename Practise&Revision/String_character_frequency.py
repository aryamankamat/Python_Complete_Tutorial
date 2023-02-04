"""Write a python program to calculate the frequency of characters present in a string."""

s = "Rajanikanth"
count = {}

for i in s:
    if i in count.keys():
        count[i] = count[i] + 1
    else:
        count[i] = 1

# print(count)

for k, v in count.items():
    print(k, "=", v)
