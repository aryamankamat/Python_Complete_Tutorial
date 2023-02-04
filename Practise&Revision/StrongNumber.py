n = int(input("Enter a number : "))


strong = 0
num = n
print("The number is = ", n)
while (n):
    i = 1
    f = 1
    r = n % 10
    while (i <= r):
        f = f * i
        i += 1
    strong = strong + f
    n = n // 10

if (strong == num):
    print("The number is a strong number.")
else:
    print("The number is not a strong number.")


"""
my_sum = 0
my_num = int(input("Enter a number : "))
print("The number is")
print(my_num)
temp = my_num
while (my_num):
    i = 1
    fact = 1
    remainder = my_num % 10
    while (i <= remainder):
        fact = fact*i
        i = i+1
    my_sum = my_sum+fact
    my_num = my_num//10
if (my_sum == temp):
    print("The number is a strong number")
else:
    print("The number is not a strong number")
"""
