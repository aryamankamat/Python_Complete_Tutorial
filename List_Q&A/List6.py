"""
Write a Python program to find the list of words that are longer than n from a given list of words.
"""
str = "The quick brown fox jumps over the lazy dog"
word_lst = []
n = int(input("Enter the limit of word : "))
txt = str.split(" ")
for i in txt:
    if (len(i) > n):
        word_lst.append(i)
print(word_lst)
