# Name: Anderson Fernandes
# Date: October 22, 2017
# Description: Exercise 2, Write another program that prompts for a list of
#              numbers as above and at the end prints out both the maximum and
#              minimum of the numbers instead of the average.

# Imports
def doUntilDone():
    inp = 0
    nums = []
    count = 0
    while True:
        inp = input("Enter a number: ")
        if (inp == "done"):
            print("Max:", max(nums), "Min:", min(nums))
            return False
        else:
            try:
                nums.append(int(inp))
            except:
                print("Invalid input")

# Main Function
def main():
    doUntilDone()

# Main
main()
