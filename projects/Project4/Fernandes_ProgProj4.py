# Name: Anderson Fernandes
# Date: December 9, 2017
# Description: Programming Project 4, sunspots

# Imports


# Functions

# Returns a two dimensional list with sunspot data for each year/month
def datafy():
    try:
        sunspotsData = open('sunspots.txt')
    except:
        print('Cannot open sunspots data file')
    # empty two dimensional list that will hold sunspot data
    dataList = []
    # loop through each line
    for line in sunspotsData:
        # separate year and monthly data
        yearData = line.split()
        # get the year and add it to the list
        year = yearData[0]
        dataList.append(year)
        # get monthly data and add it to the list
        data = yearData[1:13]
        # convert numbers to floats so we can perform calculations
        data = list(map(float, data))
        # add to dataList
        dataList.append(data)
    # return list with data
    return dataList

#-------------------------------------------------------------------------------

# This function calculates the average sunspots, given a particular year
def averageSunspots(year):
    # First year is index 0 of the list
    firstYear = 1945
    # The year is always in the even indexes
    yearIndex = (year - 1945) * 2
    # Sunspot data is always in odd indexes
    dataIndex = yearIndex + 1
    # Get list from file
    data = datafy()
    # If the year is not on the data file, return an error
    lowerYear = int(data[0])
    higherYear = int(data[len(data) - 2])
    if (year >= lowerYear) and (year <= higherYear):
        yearlyData = data[dataIndex]
        # Get Average
        average = sum(yearlyData) / len(yearlyData)
        writeData(year, average)
        return ("The average sunspot activity in " + str(year) + " was " +  str(average))
    else:
        return (str(year) + " is not on the data file.")

#-------------------------------------------------------------------------------

# This function writes query data into results.txt
def writeData(year, average):
    year = str(year)
    average = str(average)
    fout = open("results.txt", "a")
    fout.write(year + " " + average + "\n")

#-------------------------------------------------------------------------------

# Main Function
def main():
    print("NASA Sunspot Data \n")
    yr = int(input("Enter a year between 1945 and 2008: "))
    avg = averageSunspots(yr)
    print(avg)

# Main
main()
