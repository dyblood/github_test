# 2.8.1.3 - ImportError & KeyError

# ImportError
    # location: BaseException <- Exception <- StandardError <- ImportError
    # concrete exception raised when an import operation fails

# One of these imports will fail - which one?

try:
    import math
    import time
    import abracadabra

except:
    print('One of your imports has failed.')

# KeyError:
    # Location: BaseException <- Exception <- LookupError <- KeyError
    # a concrete exception raised when you try to access a collections non-existent element

# How to abuse the dictionary
# and how to deal with it?

dictionary = { 'a': 'b', 'b': 'c', 'c': 'd' }
ch = 'a'

try:
    while True:
        ch = dictionary[ch]
        print(ch)
except KeyError:
    print('No such key:', ch)


