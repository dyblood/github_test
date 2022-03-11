#write and test a function which takes:
#one argument (a year)
    #returns True if the year is a leap year
    #or false if not a leap year

# Gregorian calander started in 1582
# if the year number isn't divisible by four, it's a common year;
# otherwise, if the year number isn't divisible by 100, it's a leap year;
# otherwise, if the year number isn't divisible by 400, it's a common year;
# otherwise, it's a leap year.

def is_year_leap(year):
    if year%400 == 0 or year%100 != 0 and year%4 == 0:
        return True #sets return value to true (True means that it is a leap year)
    else:
        return False #sets return value to false (False means that it is a common year)

test_data = [1900, 2000, 2016, 1987] #list of years testing to see if they are leap years
test_results = [False, True, True, False] #correct answers to test if function works
for i in range(len(test_data)): 
	yr = test_data[i] #setting year to the element in the list w/ an index of i
	print(yr,"->",end="")
	result = is_year_leap(yr) #running the function for a specific year and setting the return value to result
	if result == test_results[i]: #comparing the return value to the expected result
		print("OK")
	else:
		print("Failed")
