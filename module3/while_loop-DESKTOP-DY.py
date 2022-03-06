#This file has multiple different loop examples.
#Make sure to only run the portion of code between the dotted lines.

#--------------------------------------------------------------------------------------------

#cont is the variable that is tested for in the while loop.
cont = input("Would you like to solve the math problem [y/n]: ")
while cont == "y":
    if cont == "y":
        x =  input("x = ") #User inputs value for x.
        x = float(x) #turns x into a float integer
        y = 3*x**3 - 2*x**2 + 3*x - 1
        print("y =", y)
        cont = input("Would you like to do another math problem: [y/n]: ")
print("Come back if you want to solve another problem!")

#-----------------------------------------------------------------------------------------

# Store the current largest number here.
largest_number = -999999999

# Input the first value.
number = int(input("Enter a number or type -1 to stop: "))

# If the number is not equal to -1, continue.
while number != -1:
    # Is number larger than largest_number?
    if number > largest_number:
        # Yes, update largest_number.
        largest_number = number
    # Input the next number.
    number = int(input("Enter a number or type -1 to stop: "))

# Print the largest number.
print("The largest number is:", largest_number)

#----------------------------------------------------------------------------------------

# A program that reads a sequence of numbers
# and counts how many numbers are even and how many are odd.
# The program terminates when zero is entered.

odd_numbers = 0
even_numbers = 0

# Read the first number.
number = int(input("Enter a number or type 0 to stop: "))

# 0 terminates execution.
while number != 0:
    # Check if the number is odd.
    if number % 2 == 1:
        # Increase the odd_numbers counter.
        odd_numbers += 1
    else:
        # Increase the even_numbers counter.
        even_numbers += 1
    # Read the next number.
    number = int(input("Enter a number or type 0 to stop: "))

# Print results.
print("Odd numbers count:", odd_numbers)
print("Even numbers count:", even_numbers)

#------------------------------------------------------------------------------------------

counter = 5
while counter != 0:
    print("Inside the loop.", counter)
    counter -= 1
print("Outside the loop.", counter)

#------------------------------------------------------------------------------------------

counter = 5
while counter:
    print("Inside the loop.", counter)
    counter -= 1
print("Outside the loop.", counter)

#------------------------------------------------------------------------------------------
