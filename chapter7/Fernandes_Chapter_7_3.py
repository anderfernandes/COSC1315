# Name: Anderson Fernandes
# Date: December 2, 2017
# Description: Easter egg

# Imports

# Functions
def lineCounterWithEasterEgg(fileName):
    if (fileName == 'na na boo boo'):
        print('NA NA BOO BOO TO YOU TOO - You have been punk\'d!')
    else:
        try:
            fhand = open(fileName)
        except:
            print('File cannot be opened:', fileName)
            exit()
        count = 0
        for line in fhand:
            if line.startswith('Subject:'):
                count = count + 1
        print('There were', count, 'subject lines in', fileName)

# Main Function
def main():
    fname = input('Enter the file name: ')
    lineCounterWithEasterEgg(fname)
# Main
main()
