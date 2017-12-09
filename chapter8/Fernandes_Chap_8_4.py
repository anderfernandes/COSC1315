# Name: Anderson Fernandes
# Date: December 2, 2017
# Description: Exercise 4, Chapter 8

# Imports

# Functions
def printListOfWords(file):
    fhand = open(file)
    listOfWords = []
    for line in fhand:
        words = line.split()
        for word in words:
            if (words[len(words) - 1] != word):
                listOfWords.append(word)
    print(sorted(listOfWords))

# Main Function
def main():
    fname = input('Enter file: ')
    printListOfWords(fname)

# Main
main()
