"""
Write a Python program that inverts a dictionary. That is, it makes
key of one dictionary as value of another and vice versa.
"""

# Logic 1
"""
dct = {101: "akshat", 201: "ball"}
print("Original dicitonary is displayed below...", dct, sep='\n')
inverted_dic = dict(zip(dct.values(), dct.keys()))
print("Inverted dictionary is displayed below...", inverted_dic, sep='\n')
"""

# Logic 2
"""
dct = {101: "akshat", 201: "ball"}
print("Original dicitonary is displayed below...", dct, sep='\n')
invt_dic = {v: k for k, v in dct.items()}
print("Inverted dictionary is displayed below...", invt_dic, sep='\n')
"""

# Logic 3
"""
dct = {101: "akshat", 201: "ball"}
print("Original dicitonary is displayed below...", dct, sep='\n')
invt_dic = dict(map(reversed, dct.items()))
print("Inverted dictionary is displayed below...", invt_dic, sep='\n')
"""
