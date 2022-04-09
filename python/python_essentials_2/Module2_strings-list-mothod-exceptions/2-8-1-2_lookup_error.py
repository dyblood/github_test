# 2.8.1.2 - LookupError

# LookupError
    # Location: BaseException <- Exception <- LookupError
    # an abstract exception including all exceptions caused by errors resulting
        #from invalid references to different collections(lists, dictionaries tuples)
        
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