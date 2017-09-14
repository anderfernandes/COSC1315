# Name: Anderson Fernandes
# Date: September 13, 2017
# Description: Exercise 1, Chapter 3

hours = float(input("Enter hours worked: "))
rate = float(input("Enter hourly rate: "))
salary = (hours * rate)
if (hours > 40):
	salary = (40 * rate) + (hours - 40) * rate * 1.5
print("Salary = $", salary)
