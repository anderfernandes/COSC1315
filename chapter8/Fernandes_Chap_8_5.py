# Name: Anderson Fernandes
# Date: December 2, 2017
# Description: Exercise 5, Chapter 8

# Imports


# Functions
def findSender(file):
    fhand = open(file)
    delimiter = 'From '
    results = []
    count = 0
    for line in fhand:
        if line.startswith(delimiter):
            words = line.split()
            print(words[1])
            count += 1
    count = str(count)
    print('There were ' + count + ' lines in the file with ' + delimiter + 'as the first word')

# Main Function
def main():
    fname = input('Enter a file name: ')
    findSender(fname)

# Main
main()
