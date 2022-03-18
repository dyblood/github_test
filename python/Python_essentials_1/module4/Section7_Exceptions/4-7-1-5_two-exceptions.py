#4.7.1.5 Two Exceptions

#If there is more than one kind of error that can occur
#the except must define the type of error that might occur

try:
    value = int(input("Enter a natuaral number:"))
    print("The reciprocal of", value, "is", 1/value)
except (TypeError, ZeroDivisionError):
    print("I dunno what to do")
# except ZeroDivisionError:
#     print("Division by zero is not allowed in our Universe!")
except: #default except branch NOTE: must be the last branch
    print("I have no idea what you did....")