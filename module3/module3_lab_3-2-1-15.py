#German mathematician named Lothar Collatz's hypothesis

#user input
c0 = int(input("Input any non-negative and non-zero integer number: "))
steps = 0

while c0 != 1:
    if c0%2 == 0:
        c0 //= 2
        print(c0)
    else:
        c0 = 3 * c0 + 1
        print(c0)
    steps +=1
print("Total Steps: ", steps)
