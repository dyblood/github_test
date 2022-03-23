# from math import pi #which entity from a module is acceptable in the code
#print(math.e) # .e will cause error -> specific entity was not imported
pi = 3.14

def sin(x):
    if 2*x == pi:
        return 0.99999999
    else:
        return None

from math import sin, pi

print(sin(pi/2)) #note no need to put math.sin or math.pi when imported like this

from math import * #imports all entity's in math module

#import module as alias #imports module with an alias

#example import math as ma #alias becomes ma
    #ma.sin() instead of math.sin()

import math as m

print(m.sin(m.pi/2)) #note module alias => m



