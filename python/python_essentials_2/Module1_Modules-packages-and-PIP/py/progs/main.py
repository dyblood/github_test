#import path with sys module if it is not already added
from sys import path
# path.append('...\\modules') # '\\' ==> because '\' is an escape characters '\\' ==> '\'
    #relative path
path.append('C:\\Users\\TDEM\\Desktop\\Youngblood\\github_test\\python\\python_essentials_2\\Module1_Modules-packages-and-PIP\\py\\modules')
    #absolute path

from module import sum1, prod1

zeroes = [0 for i in range(5)]
ones = [1 for i in range(5)]

print(sum1(zeroes))
print(prod1(ones))

import sys

for i in sys.path:
    print(i)
    