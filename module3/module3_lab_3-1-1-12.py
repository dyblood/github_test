#module3_lab_3-1-1-12

year = int(input("Enter a year: "))
cyear = "Common Year"
lyear = "Leap year"

# Gregorian calander started in 1582
# if the year number isn't divisible by four, it's a common year;
# otherwise, if the year number isn't divisible by 100, it's a leap year;
# otherwise, if the year number isn't divisible by 400, it's a common year;
# otherwise, it's a leap year.

if year < 1582:
    print("Year entered was not within the Gregorian calendar period.")
elif year%4 != 0: 
    print(cyear)
elif year%100 != 0:
    print(lyear)
elif year%400 != 0:
    print(cyear)
else:
    print(lyear)

