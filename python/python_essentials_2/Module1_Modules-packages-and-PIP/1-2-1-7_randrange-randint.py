#1.2.1.7 randrange and randint functions

from random import randrange, randint

print(randrange(1), end=" ")
print(randrange(0, 1), end=" ")
print(randrange(0,1,1), end=" ")
print(randint(0, 1))

for i in range(10):
    print(randint(1, 10), end=",")
print("\n------------------------------------------")

from random import choice, sample

my_list = [i for i in range(1, 11)]

print(choice(my_list))
print(sample(my_list, 5))
print(sample(my_list, 10))

