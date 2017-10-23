# Name: Anderson Fernandes
# Date: October 8, 2017
# Description: Exercise 6, computepay with functions

# Imports

# Functions

def computepay(hours, rate):
    salary = (hours * rate)
    if (hours > 40):
    	salary = (40 * rate) + (hours - 40) * rate * 1.5
    return salary

# Main Function

def main():
    h = float(input("Enter hours worked: "))
    r = float(input("Enter hourly rate: "))
    salary = computepay(h, r)
    print(salary)

# Main

main()
