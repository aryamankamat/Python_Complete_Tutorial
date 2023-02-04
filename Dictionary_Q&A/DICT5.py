"""
5\. Write a Python script to merge two Python dictionaries.
"""
# Logic I
"""
dic1={1:10, 2:20}
dic2={3:30, 4:40}
dic3={5:50,6:60}
dic1.update(dic2)
dic1.update(dic3)
print(dic1)
"""

# Logic II
"""
dic1 = {1: 10, 2: 20}
dic2 = {3: 30, 4: 40}
ans = dic1 | dic2
print(ans)
"""

# Logic III
"""
dic1 = {1: 10, 2: 20}
dic2 = {3: 30, 4: 40}
ans = {**dic1, **dic2}
print(ans)
"""

# Logic IV
"""
dic1 = {1: 10, 2: 20}
dic2 = {3: 30, 4: 40}
dic3 = dic2.copy()
dic3.update(dic1)
print(dic3)
"""
