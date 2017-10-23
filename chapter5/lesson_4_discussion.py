# Name: Anderson Fernandes
# Date: October 22, 2017
# Description: This program shows tables for the four basic operators

# Imports

# Functions
def printTable(number, operator):
    if (operator == "plus" or operator == "+"):
        for x in (range(0, 11)):
            print (number, "+", x, "=", number + x)
    elif (operator == "minus" or operator == "-"):
        for x in (range(0, 11)):
            result = (number + x) - number
            print (number + x, "-", number, "=", result)
    elif (operator == "times" or operator == "*"):
        for x in (range(0, 11)):
            print (number, "*", x, "=", number * x)
    elif (operator == "division" or operator == "/"):
        print ("0 /", number, "=", 0)
        for x in (range(1, 11)):
            result = (number * x) / number
            print (number * x, "/", number, "=", int(result))
    else:
        print("Unkown operator, please try again")

# Main Function
def main():
    print("Andersoft Math Tables 1.0")
    print("Type exit at anytime to close")
    while (True):
        operator = input("\nEnter sign of the operator: ")
        if (operator == "exit" or len(operator) == 0):
            print("Bye!")
            break
        else:
            number = input("Enter a number: ")
            if ((number == "exit") or (len(number) == 0)):
                print("Bye!")
                break
            else:
                number = int(number)
                printTable(number, operator)

# Main
main()
