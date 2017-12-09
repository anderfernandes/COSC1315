# Name: Anderson Fernandes
# Date: December 2, 2017
# Description: Write a program to read through a file and print the contents of
#              the file (line by line) all in upper case

# Imports

# Functions
def printToUpper(fileName):
    fhand = open(fileName)
    for line in fhand:
        line = line.upper()
        print(line)
# Main Function
def main():
    file = input("Enter a file name: ")
    printToUpper(file)

# Main
main()
