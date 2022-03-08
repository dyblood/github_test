# Positional parameter passing

def my_function(a, b, c):
    print(a, b, c)

my_function(1, 2, 3)

def introduction(first_name, last_name):
    print("Hello, my name is", first_name, last_name)

introduction("Luke", "Skywalker")
introduction("Jesse", "Quick")
introduction("Clark", "Kent")

introduction("Skywalker", "Luke")
introduction("Quick", "Jesse")
introduction("Kent", "Clark")

#--------------------------------------------------------------------
#Keyword argument passing

introduction(first_name="James", last_name="Bond")
introduction(last_name="Skywalker", first_name="Luke")
