# 2.5.1.3 - The Numbers Processor

# Numbers Processor.

# line = input("Enter a line of numbers - separate them with spaces: ")
# strings = line.split()
strings = input("Enter a line of numbers - separate them with spaces: ").split()
total = 0
count = 0
try:
    for substr in strings:
        total += float(substr)
        count += 1
    if count > 0:
        print("The total is:", total)
    else:
        print("You did not enter anything.")
except:
    print(substr, "is not a number.")
