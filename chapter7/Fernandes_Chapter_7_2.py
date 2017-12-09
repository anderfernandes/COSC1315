# Name: Anderson Fernandes
# Date: December 2, 2017
# Description: Write a program to prompt for a file name, and then read through
#              the file and look for lines

# Imports

# Functions
def avgSpamConf(fileName):
    spamText = 'X-DSPAM-Confidence: '
    fhand = open(fileName)
    spamSum = 0
    spamCount = 0
    for line in fhand:
        if line.startswith(spamText):
            spamConfidence = line.strip(spamText)
            spamConfidence = float(spamConfidence)
            spamSum += spamConfidence
            spamCount += 1
    spamAverage = spamSum / spamCount
    return spamAverage


# Main Function
def main():
    file = input("Enter a file name: ")
    averageSpamConfidence = avgSpamConf(file)
    print('Average spam confidence: ', averageSpamConfidence)

# Main
main()
