#This program will convert pounds to kilograms
#2/12/19
#CTI-110 P2T1 - Sales Prediction
#Malachi Blackburn
#Gets the projected total sales
total_sales = float(input("Enter the projected sales: "))
#Calculates the profit as 23 percent of total sales
profit = total_sales * .23
#Display the profit
print("The profit is $", format(profit, ",.2f"))
