#1.3.1.5 PATH

#variable is named path, available through the module named sys

import sys

for p in dir(sys):
    print(p)
for p in sys.path:
    print(p)

print(sys.api_version)

# from sys import path

# path.append('..\\modules')

# import module

# zeroes = [0 for i in range(5)]
# ones = [1 for i in range(5)]
# print(module.suml(zeroes))
# print(module.prodl(ones))