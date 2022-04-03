# 2.5.1.4 - The IBAN Validator

# An IBAN-compliant account number consists of:

    # a two-letter country code taken from the ISO 3166-1 standard 
    # (e.g., FR for France, GB for Great Britain, DE for Germany, and so on)

    # two check digits used to perform the validity checks - 
    # fast and simple, but not fully reliable, tests, showing whether 
    # a number is invalid (distorted by a typo) or seems to be good;

    # the actual account number (up to 30 alphanumeric characters - 
    # the length of that part depends on the country)

# The standard says that validation requires the following steps (according to Wikipedia):

    # (step 1) Check that the total IBAN length is correct as per the country
    #          (this program won't do that, but you can modify the code to meet this requirement if you wish; 
    #          note: you have to teach the code all the lengths used in Europe)

    # (step 2) Move the four initial characters to the end of the string
    #          (i.e., the country code and the check digits)

    # (step 3) Replace each letter in the string with two digits,
    #          thereby expanding the string, where A = 10, B = 11 ... Z = 35;

    # (step 4) Interpret the string as a decimal integer and 
    #          compute the remainder of that number on division by 97; 
    #          If the remainder is 1, the check digit test is passed and the IBAN might be valid.

# IBAN Validator.

iban = input("Enter IBAN, please: ")
iban = iban.replace(' ','') # removes spaces in the IBAN if there are any

if not iban.isalnum(): #IBAN must contain digits and letters only
    print("You have entered invalid characters.") 
elif len(iban) < 15: #must be at least 15 characters
    print("IBAN entered is too short.")
elif len(iban) > 31: # Can't be longer than 31 characters
    print("IBAN entered is too long.")
else:
    iban = (iban[4:] + iban[0:4]).upper() # adds the first 4 characters to the end of the IBAN
    iban2 = ''
    for ch in iban:
        if ch.isdigit(): #if a digit add it to iban2 as is
            iban2 += ch
        else:
            iban2 += str(10 + ord(ch) - ord('A')) #if a letter convert to two digit (see step 3 above)
    iban = int(iban2)
    if iban % 97 == 1:
        print("IBAN entered is valid.")
    else:
        print("IBAN entered is invalid.")

#A   B   C   D   E   F   G   H   I   J   K   L   M   N   O    P   Q   R   S    T   U   V   W   X   Y   Z
#10  11  12  13  14  15  16  17  18  19  20  21  22  23  24  25   26  27  28   29  30  31  32  33  34  35