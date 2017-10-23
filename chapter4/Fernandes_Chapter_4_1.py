# Name: Anderson Fernandes
# Date: October 8, 2017
# Description: Exercise 1, testing random

# Imports

import random

# Functions

def getRandom():
    for i in range(10):
        x = random.randint(5, 10)
        return (x)

# Main Function

def main():
    # First random integer number
    firstRandomNumber = getRandom()
    print(firstRandomNumber)
    # Second random integer
    secondRandomNumber = getRandom()
    print(secondRandomNumber)
    # Create a sequence
    t = [1, 2, 3]
    # Print two numbers from the sequence
    print(random.choice(t))
    print(random.choice(t))

# Main

main()
