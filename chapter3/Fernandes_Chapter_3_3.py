# Name: Anderson Fernandes
# Date: September 13, 2017
# Description: Exercise 3, Chapter 3

grade = input("Enter a grade: ")
try:
    grade = float(grade)
    # Check if grade is out of range
    if (grade < 0.0 or grade > 1.0):
        print("Bad score")
    else:
        # Find letter grade
        if (grade >= 0.9):
            print("A")
        elif (grade >= 0.8):
            print("B")
        elif (grade >= 0.7):
            print("C")
        elif (grade >= 0.6):
            print("D")
        else:
            print("F")
except:
    print("Bad score")
