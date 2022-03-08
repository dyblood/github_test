#To find any element of a two-dimensional list, you need two corrdinates:
    # a vertical one (row number)
    # and a horizontal one (column number)

#example:
#software for an automatic weather station
    #device records the air temperature on an hourly basis and does it through the month
    #total values: 24 x 31 = 744

#type of data type:
    #float because thermometer can measure temp with accuracy of 0.1 C  degrees
#rows will record the readings every hour on the hour
    #rows will have 24 elements (or collumns)
#each row will be assigned to a day of the month(assuming 31 days e/ month)
    #there will need to be 31 rows
#----------------------------------------------------------------------
#Pair of comprehensions = (h is for hour, d for day):
temps = [[0.0 for h in range(24)] for d in range(31)]
#----------------------------------------------------------------------
#Now determin the monthly average noon temperature
    #add up all 31 readings recorded at noon and divide by sum
total  = 0.0

for day in temps:
    total += day[11] #variable is not scalar -> e/ pass through the temps matrix assigns 
                     #it w/ the subsequent rows of the matrix (hence it is a list)
                     #has to be indexed w/ 11
average = total / 31

print("Average temperature at noon:", average)
#-----------------------------------------------------------------------
#Now find the highest temp
highest = -100.0
for day in temps: #NOTE: day variable iterates through all the rows in the temps matrix
    for temp in day: #NOTE: temp variable iterates through all the measurements taken in one day
        if temp > highest:
            highest = temp

print("The highest temperature was:", highest)
#-----------------------------------------------------------------------
# Now count the days when the temperature at noon was at leas 20.0 deg C

hot_days = 0

for day in temps:
    if day[11] >= 20.0:
        hot_days += 1

print(hot_days, "were hot.")
