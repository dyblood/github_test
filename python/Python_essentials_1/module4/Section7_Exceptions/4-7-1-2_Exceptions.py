#4.7.1.2 What data is not what it should be
#if user enters a value that is not a int an error will happen
#python has a way around this

try:
    value = int(input('Enter a natural number: '))
    print('The reciprocal of', value, 'is', 1/value)
except:
    print('I do not know what to do now.')
#if value entered does not meet the criteria the except portion will execute instead of 
#an error message

