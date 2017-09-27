# Name: Anderson Fernandes
# Date: September 24, 2017
# Description: Programming Project 1, Calculate Interest Rate

# Reading loan amount from user
LoanAmt = input("Enter loan amount: $ ")

try:
    LoanAmt = float(LoanAmt)
    # Reading interest rate from user
    InterestRate = input("Enter interest rate: ")

    try:
        InterestRate = float(InterestRate)
        # Making sure the interest rate isn't higher than 100%
        if (InterestRate > 100):
            print("Interest rate is too high...")
        else:
            NumberMonths = input("Enter the number of payments you want to make: ")

            try:
                # Reading number of months
                NumberMonths = int(NumberMonths)
                # Calculating the monthly interest rate
                MonthlyRate = InterestRate/1200
                # Calculating the monthly payment
                Payment = LoanAmt * MonthlyRate * ((1 + MonthlyRate)**NumberMonths) / ((1 + MonthlyRate)**NumberMonths - 1)
                # Print monthly payment rounded to two decimal places
                print("Your monthly payment is going to be $", round(Payment, 2))

            except:
                print("Bad number of payments. Make sure you enter an integer.")

    except:
        print("Bad interest rate. Please enter a number without the percent sign.")

except:
    print("Bad loan amount. Please enter a number.")
