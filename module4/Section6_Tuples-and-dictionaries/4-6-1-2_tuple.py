#4.6.1.2 How to use a tuple

my_tuple = (1, 10, 100, 1000)

print(my_tuple[0])
print(my_tuple[-1])
print(my_tuple[1:])
print(my_tuple[:-2])

for elem in my_tuple:
    print(elem)

#NOTE: do not try to modify a tuple => a tuple IS NOT a list!!
#--------------------------------------------------------------------
my_tuple = (1, 10, 100)

t1 = my_tuple + (1000, 10000)
t2 = my_tuple * 3

print(len(t2))
print(t1)
print(t2)
print(10 in my_tuple)
print(-10 not in my_tuple)

#----------------------------------------------------------------------
var = 123

t1 = (1, )
t2 = (2, )
t3 = (3, var) #NOTE: a tuple's element can be variables

t1, t2, t3 = t2, t3, t1

print(t1, t2, t3)