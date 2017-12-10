# Student name: Anderson Fernandes
# Date: 12-9-2017
# Python 3.X dev environment
# Lesson 7 Programming Assignment A
# Complete the code below by:
# 1. Writing the code to complete each function as described.
# 2. Writing the additional test cases to test the functions.
# ----------------------------------

#def withoutX(aStr):
def withoutX(aStr):
	if aStr[:1] == "x":
		aStr = aStr[1:]
	if aStr[-1:] == "x":
		aStr = aStr[:-1]
	return aStr

# ------------------------------------
#def frontAgain(aStr):
def frontAgain(aStr):
	if aStr[:2] == aStr[-2:]:
		return True
	else:
		return False



# ------------------------------------
#def doubleChar(aStr):
def doubleChar(str):
	newStr = ""
	for char in str:
		newStr += char
		newStr += char
	return newStr



def main():

	#Testing doubleChar(aStr)
	print("Testing doubleChar(aStr)" )
	assert(doubleChar("hello") == "hheelllloo")
	assert(doubleChar("Hi") == "HHii")
	assert(doubleChar("Hi-There") == "HHii--TThheerree")
	assert(doubleChar("Stuff") == "SSttuuffff")
	assert(doubleChar("Things") == "TThhiinnggss")
	print("If no Assert errors to this point - doubleChar(aStr) works.")
	print("\n")

	#Testing frontAgain(aStr):
	print("Testing frontAgain(aStr)" )
	assert(frontAgain("edited") == True)
	assert(frontAgain("edit") == False)
	assert(frontAgain("ed") == True)
	assert(frontAgain("Stuff") == False)
	assert(frontAgain("Things") == False)
	print("If no Assert errors to this point - frontAgain(aStr) works.")
	print("\n")

	#Testing withoutX(aStr):
	print("Testing withoutX(aStr)" )
	assert(withoutX("xHix") == "Hi")
	assert(withoutX("xHi") == "Hi")
	assert(withoutX("Hxix") == "Hxi")
	assert(withoutX("xThingsx") == "Things")
	assert(withoutX("xHxix") == "Hxi")
	print("If no Assert errors to this point - withoutX(aStr) works.")




main()
