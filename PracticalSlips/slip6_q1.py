s = float(input("Enter the side of square = "))
square = lambda x: x ** 2
square_ans = square(s)
print(f"Area of square is = {square_ans:.2f}")
print()
l = float(input("Enter the lenght of rectangle = "))
b = float(input("Enter the breath of rectangle = "))
rectangle = lambda x, y: x * y
rectangle_area = rectangle(l, b)
print(f"Area of rectangle is = {rectangle_area:.2f}")
