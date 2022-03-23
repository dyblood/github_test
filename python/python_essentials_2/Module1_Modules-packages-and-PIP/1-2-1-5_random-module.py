#1.2.1.5 Random Module
# allows you to operate with pseudorandom numbers
from random import random, seed

#random() function => produces a float number x coming from the range (0.0 - 1.0) or (0.0 <= x <= 1.0)
for i in range(5):
    print(random()) 

print("-----------------------------------------------------------------")

#seed() function => able to directly set the generator's seed.
#two of its variants
    #seed() => sets the seed with the current time
    #seed(int_value) => sets the seed w/ the int value

seed(0)

for i in range(5):
    print(random())

#NOTE: because seed is always the same value => the sequence of generated values always are the same
#NOTE: have the same seed removes the "randomness" from the code

