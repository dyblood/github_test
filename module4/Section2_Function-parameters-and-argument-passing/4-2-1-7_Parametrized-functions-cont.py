def introduction(fn, ln="Smith"): #ln="Smith" creates a default value of Smith
    print("Hello, my name is", fn, ln)

introduction("James", "Doe") #ln has been defined so "Doe" is the ln

introduction("Henry") #ln was omitted so default value ("Smith") is used

introduction(fn="William") #ln was omitted so default value is used
#----------------------------------------------------------------------

def intro(fn="John", ln="Smith"): #both parameters were given default values
    print("Hello, my name is", fn, ln)

intro() #both parameter values omitted so default values are used for both

intro(ln="Hopkins") #fn parameter value omitted

