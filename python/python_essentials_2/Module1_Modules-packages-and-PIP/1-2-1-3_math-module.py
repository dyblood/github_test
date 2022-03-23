#1.2.1.2 - 1.2.1.4: selectcted functions from the math module
#some functions provided by the math module
#--------------------------------------------------------------
#Some trigonometry functions:
from math import pi, radians, degrees, sin, cos, tan, asin
ad = 90
ar = radians(ad)
ad = degrees(ar)

print(ad == 90)
print(ar == pi / 2.)
print(sin(ar) / cos(ar) == tan(ar))
print(asin(sin(ar)) == ar)

print("-------------------------------------------------------------------")

#functions which are connected with expnentiation:

from math import e, exp, log

print(pow(e, 1) == exp(log(e)))
print(pow(2, 2) == exp(2 *log(2)))
print(log(e, e) == exp(0))

print("-------------------------------------------------------------------")

#general-purpose functions:

from math import ceil, floor, trunc

x = 1.4
y = 2.6

print(floor(x), floor(y))
print(floor(-x), floor(-y))
print(ceil(x), ceil(y))
print(ceil(-x), ceil(-y))
print(trunc(x), trunc(y))
print(trunc(-x), trunc(-y))

print("-------------------------------------------------------------------")
