# 2.5.1.9 - LAB: The Digit of Life

# Your task is to write a program which:
    # asks the user her/his birthday 
    # (in the format YYYYMMDD, or YYYYDDMM, or MMDDYYYY - actually, the order of the digits doesn't matter)

    # outputs the Digit of Life for the date.

bday = input("Enter your bday (yyyymmdd): ")
if len(bday) != 8:
    print("You did not enter your Bday in the correct format.")

while True:
    dol = 0
    for num in bday:
        if not num.isdigit():
            continue
        else:
            dol += int(num)
    bday = str(dol)
    if dol < 10:
        break

print(dol)
