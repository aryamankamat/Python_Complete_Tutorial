"""
2. Write a Python script to concatenate following dictionaries to
create a new one.

**Sample Dictionary :
**dic1={1:10, 2:20}
dic2={3:30, 4:40}
dic3={5:50,6:60}
**Expected Result :** {1: 10, 2: 20, 3: 30, 4: 40, 5: 50, 6: 60}
"""

# Logic I
dic1 = {1: 10, 2: 20}
dic2 = {3: 30, 4: 40}
dic3 = {5: 50, 6: 60}
dic4 = dict()

for d in (dic1, dic2, dic3):
    dic4.update(d)

print("Updated new dictionary is below....", dic4, sep='\n')


# Logic II
"""
dic1={1:10, 2:20}
dic2={3:30, 4:40}
dic3={5:50,6:60}
dic1.update(dic2)
dic1.update(dic3)
print(dic1)
"""
