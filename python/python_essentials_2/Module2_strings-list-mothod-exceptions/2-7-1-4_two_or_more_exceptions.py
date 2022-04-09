# 2.7.1.4 - handleing two or more exceptions in the same way

def bad_fun(n):
    return 1 / n

try:
    bad_fun(0)
except ArithmeticError:
    print("What happened? An exception was raised!")

print("THE END.")

# format for putting two different type of exceptions into one line
# try:
#     :
# except (exc1, exc2):
#     :  