#Example of type casting a string literal 
#into a numerical literal float from user input

numerical_float = float(input("Pick a number any number:  "))
    #Changes the string entered by the user to a numerical literal float

# numerical_integer = int(input("Pick a number any number:  "))
    #changes the string inputed by the user to a numerical literal integer

something = numerical_float ** 2.0
print(numerical_float, "to the power of 2 is: ", something)

#Type Conversion --> change a number into a string

leg_a = float(input("Input first leg length: "))
leg_b = float(input("Input second leg length: "))
print("Hypotenuse length is " + str((leg_a**2 + leg_b**2) ** .5))