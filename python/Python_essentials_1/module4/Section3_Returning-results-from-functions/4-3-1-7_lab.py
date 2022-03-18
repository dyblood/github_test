#---------------------------------------------------------------------------
#LAB 4.3.1.7

#write a test function that takes two arguments:
    # takes a given year and month
    # returns how many days in that month
#NOTE: only febuary will differ depending if it is a leap year

#--------------------------------------------------------------------------
#function to test if year is a leap year or not
# see 4-3-1-6 for notes of this function

def is_year_leap(year):
    if year%400 == 0 or year%100 != 0 and year%4 == 0:
        return True
    else:
        return False 
#------------------------------------------------------------------------------

def days_in_month(year, month):

    day = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31] 

    # day[month -1] because a month will not be 0
    
    if is_year_leap(year) == True: # if year is a leap year
        if month == 2:
            return day[month-1]+1 #index-1 => month != 0 // add 1 => leap year => feb = 29 days
        else:
            return day[month-1] # index -1 because a month will not be 0
    elif is_year_leap(year) == False:# if year is NOT a leap year
        return day[month-1]
    else: #if argument does not make since
        return #no expression so it will default to None   

#------------------------------------------------------------------------------
test_years = [1900, 2000, 2016, 1987]
test_months = [2, 2, 1, 11]
test_results = [28, 29, 31, 30]
for i in range(len(test_years)):
	yr = test_years[i]
	mo = test_months[i]
	print(yr, mo, "->", end="")
	result = days_in_month(yr, mo)
	if result == test_results[i]:
		print("OK")
	else:
		print("Failed")