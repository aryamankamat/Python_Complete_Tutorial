dict = {"infinitely": "To an infinite extent or amount; without limit.",
        "evident": "clearly seen or understood; obvious.",
        "intend": "plan that something should be or do something.",
        "concern": "relate to; be about."}
# print(dict)
d = input("Enter a word to find its meaning: ")
ans = dict.get(d)
print(ans)
