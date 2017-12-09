# Name: Anderson Fernandes
# Date: September 24, 2017
# Description: Programming Project 2, Calculate Interest Rate 2.0

# Imports


# Functions
def fileHeader():
    #fout = open('result.txt', 'w')
    author = 'Anderson Fernandes'
    profession = 'Full Stack Web Developer'
    header = author + ' - ' + profession + '\n'
    #fout.write(header)
    return header

def toUpper(words):
    upper = []
    for word in words:
        word = word.upper()
        upper.append(word)
    return str(upper)

def toLower(words):
    lower = []
    for word in words:
        word = word.lower()
        lower.append(word)
    return str(lower)

def avgCharsPerWord():
    fhand = open('data.txt')
    charCount = 0
    trimmedWords = []
    # This array will hold the size of each word
    # sizeOfWords(numberOfLetters) will find the amount of words with numberOfLetters letters
    sizeOfWords = []
    for line in fhand:
        words = line.split()
        for word in words:
            # Count the number of words only, exclude punctuation
            if (word != '.') or (word != '!') or (word != '?') or (word != ',') or (word != '--'):
                trimmedWords.append(word)
        wordCount = len(trimmedWords)
        for trimmedWord in trimmedWords:
            sizeOfWords.append(len(trimmedWord))
            for character in trimmedWord:
                charCount +=1

    avg = charCount / wordCount

    # Writing result.txt
    foutResult = open('result.txt', 'w')
    foutResult.write('Average Number of Characters per Word: ' + str(avg))
    for numberEachLength in range(max(sizeOfWords)):
        if (numberEachLength >= 2 and numberEachLength <= 10):
            foutResult.write(str(sizeOfWords.count(numberEachLength)) + ' words of length ' + str(numberEachLength))
        if (numberEachLength >= 11):
            foutResult.write(str(sizeOfWords.count(numberEachLength)) + ' words of length ' + str(numberEachLength) + ' or more')
    foutResult.write('Total number of words: '+ str(wordCount))

    # Writing uppercase.txt
    foutUppercase = open('uppercase.txt', 'w')
    foutUppercase.write(fileHeader())
    foutUppercase.write(toUpper(trimmedWords))

    # Writing lowercase.txt
    foutLowercase = open('lowercase.txt', 'w')
    foutLowercase.write(fileHeader())
    foutLowercase.write(toLower(trimmedWords))

# Main Function
def main():
    avgCharsPerWord()

# Main
main()
