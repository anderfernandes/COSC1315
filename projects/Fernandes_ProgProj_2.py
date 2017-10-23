# Name: Anderson Fernandes
# Date: September 24, 2017
# Description: Programming Project 2, Calculate Interest Rate 2.0

# Imports

# Functions

# This function returns the monthly payment
def calculatePayment(LoanAmt, NumberMonths):

    InterestRate = getInterestRate(LoanAmt, NumberMonths)
    # Reading number of months
    NumberMonths = int(NumberMonths)
    # Calculating the monthly interest rate
    MonthlyRate = InterestRate/1200
    # Calculating the monthly payment
    Payment = LoanAmt * MonthlyRate * ((1 + MonthlyRate)**NumberMonths) / ((1 + MonthlyRate)**NumberMonths - 1)
    # Print monthly payment rounded to two decimal places
    payment = round(Payment, 2)

    return payment

# This function returns the interest rate
def getInterestRate(LoanAmt, NumberMonths):
    ## If Loan Amount is between $500 and $2500
    if ((LoanAmt >= 500) and (LoanAmt <= 2500)):
        ## If number of payments in between...
        if ((NumberMonths >= 6) and (NumberMonths <= 12)):
            InterestRate = 8
        elif ((NumberMonths >= 13) and (NumberMonths <= 36)):
            InterestRate = 10
        elif ((NumberMonths >= 37) and (NumberMonths <= 48)):
            InterestRate = 12
    elif ((LoanAmt >= 2501) and (LoanAmt <= 10000)):
        ## If number of payments in between...
        if ((NumberMonths >= 6) and (NumberMonths <= 12)):
            InterestRate = 7
        elif ((NumberMonths >= 13) and (NumberMonths <= 36)):
            InterestRate = 8
        elif ((NumberMonths >= 37) and (NumberMonths <= 48)):
            InterestRate = 6
    elif (LoanAmt >= 10001):
        ## If number of payments in between...
        if ((NumberMonths >= 6) and (numberMonths <= 12)):
            InterestRate = 5
        elif ((NumberMonths >= 13) and (numberMonths <= 36)):
            InterestRate = 6
        elif ((NumberMonths >= 37) and (numberMonths <= 48)):
            InterestRate = 7
    return InterestRate

# This function gets inputs from the user
def loanCalculator():
    inp = "Y"
    while (inp != "n"):
        # Reading loan amount from user
        LoanAmt = input("\nEnter loan amount: $ ")
        try:
            LoanAmt = float(LoanAmt)
            if (LoanAmt >= 500):
                # Reading Number of Payments from the user
                NumberMonths = input("Enter the number of payments you want to make: ")
                try:
                    NumberMonths = int(NumberMonths)
                    if ((NumberMonths >= 6) and (NumberMonths <= 48)):
                        payment = calculatePayment(LoanAmt, NumberMonths)
                        print("Your monthly payment is going to be $", str(payment))
                        inp = input("Would you like to calculate another loan? y/n: ")
                    else:
                        print("Out of bounds. Please select a number between 6 and 48\n")

                except:
                    print("Please enter an integer for the number of months\n")
            else:
                print("We do not finance loans below $500\n")


        except:
            print("Please enter a number for the Amount of Loan\n")


# Main Function
def main():
    print("Andersoft Loan Calculator 2.0")
    loanCalculator()

# Main
main()
