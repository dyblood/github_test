# 2.7.1.5 - raise exception

# raise instruction raises the specified exception named exc as if it was raised in a normal (natural way)

def bad_fun(n):
    raise ZeroDivisionError #raises a ZeroDivisionError

try:
    bad_fun(0)
except ArithmeticError:
    print("What happened? An error?")

print("THE END.")

print("---------------------------------------------")

def bad_fun(n):
    try:
        return n / 0
    except:
        print("I did it again!")
        raise #this kind of raise instruction may be used inside the except branch only


try:
    bad_fun(0)
except ArithmeticError:
    print("I see!")

print("THE END.")
