"""
Program to Get Data Items from a List Appearing Odd Number of Times.
"""
# arr = [2, 3, 5, 4, 5, 2, 4, 3, 5, 2, 4, 4, 2]
arr = [1, 2, 3, 4, 5, 1, 3, 3, 4]
# method 1
n = len(arr)
lst = []
for i in range(0, n):
    cnt = 0
    for j in range(0, n):
        if (arr[i] == arr[j]):
            cnt = cnt + 1

    if (cnt % 2 != 0):
        print(arr[i])
"""
"""

# method 2
"""
cnt = 0
for i in arr:
    cnt = cnt ^ i
print(cnt)
"""
