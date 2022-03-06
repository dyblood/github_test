#cont is the variable that is tested for in the while loop.
cont = input("Would you like to solve the math problem [y/n]: ")
while True:
    if cont == "y":
        x =  input("x = ") #User inputs value for x.
        x = float(x) #turns x into a float integer
        y = 3*x**3 - 2*x**2 + 3*x - 1
        print("y =", y)
        cont = input("Would you like to do another math problem: [y/n]: ")
    else:
        print("Come back if you want to solve another problem!")
        break