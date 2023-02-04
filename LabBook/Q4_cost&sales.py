"""
4.Write a python script to accept the cost price and selling price from the keyboard.
Find out if the seller has made a profit or loss and display how much profit or loss has been made.
"""

cost_price = float(input("Enter the product cost price : "))
sales_price = float(input("ENter the product sales price : "))

if(cost_price > sales_price):
    amt = cost_price - sales_price
    print("The Loss amount = ",amt)
elif(sales_price > cost_price):
    amt = sales_price - cost_price
    print("The profit amount = ",amt)
else:
    print("NO profit and No loss")
