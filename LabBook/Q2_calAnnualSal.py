"""
2.Write a python script to accepts annual basic salary of an employee and calculates and displays the Income tax as per the following rules. 
	  Basic: 	< 2,50,000 		        Tax = 0
		       Basic: 2,50,000 to 5,00,000	Tax = 10%
                       Basic: > 5,00,000		Tax = 20
"""
income = int(input("Enter the employees income : "))
if(income <= 250000):
    tax = 0
elif(income > 250000) and (income <= 500000):
    tax = (income - 250000) * 0.10
else:
    tax = (income - 500000) * 0.20
print("You have to pay",tax,"Rupes of tax!")
