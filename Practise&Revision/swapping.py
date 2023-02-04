n1 = int(input("Enter 1st number : "))
n2 = int(input("Enter 2nd number : "))

#method 1
'''
print("Before Swapping :",n1,"and",n2)
temp = n1
n1 = n2
n2 = temp
print("After Swapping :",n1,"and",n2)
'''
#method 2
'''
print("Before Swapping :",n1,"and",n2)
n1 = n1 + n2
n2 = n1 - n2
n1 = n1 - n2
print("After Swapping :",n1,"and",n2)
'''
#method 3
'''
print("Before Swapping :",n1,"and",n2)
n1 = n1 ^ n2
n2 = n1 ^ n2
n1 = n1 ^ n2
print("After Swapping :",n1,"and",n2)
'''
#method 4
'''
print("Before Swapping :",n1,"and",n2)
n1 , n2 = n2 , n1
print("After Swapping :",n1,"and",n2)
'''
