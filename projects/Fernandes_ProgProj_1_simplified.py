# Name: Anderson Fernandes
# Date: September 24, 2017
# Description: Programming Project 1, Calculate Interest Rate

# Reading loan amount from user
LoanAmt = float(input("Enter loan amount: $ "))

# Reading interest rate from user
InterestRate = float(input("Enter interest rate: "))

# Making sure the interest rate isn't higher than 100%
if (InterestRate > 100):
    print("Interest rate is too high...")
else:
    NumberMonths = int(input("Enter the number of payments you want to make: "))

    # Calculating the monthly interest rate
    MonthlyRate = InterestRate/1200
    # Calculating the monthly payment
    Payment = LoanAmt * MonthlyRate * (((1 + MonthlyRate)**NumberMonths) / ((1 + MonthlyRate)**(NumberMonths - 1)))
    # Print monthly payment rounded to two decimal places
    print("Your monthly payment is going to be $", Payment)
