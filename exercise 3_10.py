#Daniel Murdock
#Period 3
#Exercise 3_10
##################################CODE##################################
while True:
	
	def main(): #Function that runs the program
		totalSales = float(input("Please enter the total sales for the month: $"))
		calculate(totalSales)
		
	def calculate(total): #Function that calculates county sales tax, state sales tax, and total sales tax
		countySales = total * 0.02
		stateSales = total * 0.04
		totalSalesTax = stateSales + countySales
		display(countySales, stateSales, totalSalesTax)
		
	def display(countyTax, stateTax, totalTax): #Function that displays the taxes
		print("The county sales tax was: $" + format(countyTax, '.2f'))
		print("The state sales tax was: $" + format(stateTax, '.2f'))
		print("The total sales tax was: $" + format(totalTax, '.2f'))
		
	main() #Runs the program
	
#################################Sample Run##############################
#Please enter the total sales for the month: $100
#The county sales tax was: $2.00
#The state sales tax was: $4.00
#The total sales tax was: $6.00
#Please enter the total sales for the month: $
