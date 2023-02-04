"""
Write an anonymous function to find area of square and rectangle.(Hint: use lambda function)
"""


def square(x): return x ** 2


def rectangle_area(x, y): return x * y


ans = square(5)
ans1 = rectangle_area(4, 5)
print(f"Area of square is = {ans}")
print(f"Area of rectangle is = {ans1}")
