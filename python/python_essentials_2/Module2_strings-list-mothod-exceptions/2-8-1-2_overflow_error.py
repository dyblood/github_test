# 2.8.1.2 - OverflowError

# OverflowError
    # Location: BaseException <- Exception <- ArithmeticError <- OverflowError
    # a concrete exception raised when an operation produces a number too big to be successfully stored
    
# This code causes the MemoryError exception.
# Warning: executing this code may affect your OS.
# Don't run it in production environments!

string = 'x'
try:
    while True:
        string = string + string
        print(len(string))
except MemoryError:
    print('This is not funny!')