"""
1.A cashier has currency notes of denomination 1, 5 and 10.
Write python script to accept the amount to be withdrawn from
the user and print the total number of currency notes of each denomination the cashier will have to give.
"""

amt = int(input("Enter your amount : "))
note10 = amt/10
note5 = (amt%10)/5
note1 = (amt%5)
print("The note of 10 = ",round(note10))
print("The notes of 5 = ",int(note5))
print("The notes of 1 = ",round(note1))
