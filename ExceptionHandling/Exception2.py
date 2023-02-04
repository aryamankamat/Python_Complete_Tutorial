try:
    n1 = int(input("Enter a number = "))
    n2 = int(input("Enter 2nd number = "))
    ans = (n1 / n2)
    # ans = (n1 / n2) * n3
except ZeroDivisionError as e:
    print("Error desc = ",e)
except ValueError as e:
    print("Error desc = ",e)
except NameError as e:
    print("Error desc = ", e)
except Exception as e:
    print("Error desc = ", e)
else:
    print("Will execute only of try has no error.")
finally:
    print("This block will execute anyway.")