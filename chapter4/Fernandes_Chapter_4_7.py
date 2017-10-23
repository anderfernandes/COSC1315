# Name: Anderson Fernandes
# Date: October 8, 2017
# Description: Exercise 6, computegrade with functions

# Imports

# Functions

def computegrade(grade):
    try:
        grade = float(grade)
        letterGrade = ""
        # Check if grade is out of range
        if (grade < 0.0 or grade > 1.0):
            return("Bad score")
        else:
            # Find letter grade
            if (grade >= 0.9):
                letterGrade = "A"
            elif (grade >= 0.8):
                letterGrade = "B"
            elif (grade >= 0.7):
                letterGrade = "C"
            elif (grade >= 0.6):
                letterGrade = "D"
            else:
                letterGrade = "F"
        return letterGrade
    except:
        return("Bad score")

# Main Function

def main():
    g = input("Enter a grade: ")
    result = computegrade(g)
    print(result)

# Main

main()
