#---------------------------------------------------------------------------
#LAB 4.3.1.8


#--------------------------------------------------------------------------
#function to test if year is a leap year or not
# see 4-3-1-6 for notes of this function

def is_year_leap(year):
    if year%400 == 0 or year%100 != 0 and year%4 == 0:
        return True
    if year%400 != 0 or year%100 == 0 and year%4 != 0:
        return False 
    else:
        return 
#------------------------------------------------------------------------------
#function to see how many days are in a month
#see 4-3-1-7 for more notes of this function

def days_in_month(year, month):

    day = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31] 

    # day[month -1] because a month will not be 0
    
    if is_year_leap(year) == True: # if year is a leap year
        day[1] = 29 #feb has 29 days in leap year
        return day[month-1] 
    elif is_year_leap(year) == False:# if year is NOT a leap year
        return day[month-1]
    else: #if argument does not make since
        return
#------------------------------------------------------------------------------

def day_of_year(year, month, day):
    total = 0 #setting counter to 0
    for i in range(1, month): #create loop to add only days in the months before the months before month
        result = days_in_month(year, i)
        total += result
    day_num = total+day 
    return day_num


print(day_of_year(2000, 12, 31))
print(day_of_year(1999, 12, 31))
print(day_of_year(2021, 7, 29))