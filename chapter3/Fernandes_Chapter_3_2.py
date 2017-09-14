# Name: Anderson Fernandes
# Date: September 13, 2017
# Description: Exercise 2, Chapter 3

hours = input("Enter hours worked: ")
try:
    hours = float(hours)
    rate = input("Enter hourly rate: ")
    try:
        rate = float(rate)
        salary = (hours * rate)
        if (hours > 40):
        	salary = (40 * rate) + (hours - 40) * rate * 1.5
        print("Salary = $", salary)
    except:
        print("Error, please enter numeric input")
except:
    print("Error, please enter numeric input")
