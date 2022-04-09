# 2.7.1.2 - generalized exceptions

try:
    y = 1 / 0
except ZeroDivisionError:
    print("Ooooooppsss....")
print("The End.")

try:
    y = 1/0
except ArithmeticError: # the more general class of ZeroDivisionError
    print("Oooppss...")
print("The End.")