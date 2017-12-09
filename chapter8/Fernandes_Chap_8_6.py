# Name: Anderson Fernandes
# Date: December 2, 2017
# Description: Exercise 5, Chapter 8

# Imports


# Functions
def minMax():
    numbers = []
    while (True):
        inp = input('Enter a number: ')
        if inp == 'done': break
        value = float(inp)
        numbers.append(value)
    print('Maximum: ', max(numbers))
    print('Minimum: ', min(numbers))

# Main Function
def main():
    minMax()

# Main
main()
