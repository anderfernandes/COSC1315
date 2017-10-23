# Name: Anderson Fernandes
# Date: October 22, 2017
# Description: Exercise 1, Write a program which repeatedly reads numbers until
#              the user enters "done".

# Imports

# Functions
def doUntilDone():
    inp = 0
    num = 0
    count = 0
    while True:
        inp = input("Enter a number: ")
        if (inp == "done"):
            total = num
            average = num / count
            print("Total:", total, "Count:", count, "Average:", total / count)
            return False
        else:
            try:
                num += int(inp)
                count += 1
            except:
                print("Invalid input")

# Main Function
def main():
    doUntilDone()

# Main
main()
