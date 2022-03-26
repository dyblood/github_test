#!/usr/bin/env python3
#first statement is a shabang ==> same thing for making bash scripts in linux #! /bin/bash
    #for unix and unix-like OSs (including mac) the shabang instructs the OS how to execute the contents of the file
    #has no effect on MS Windows

__counter = 0 #adding the "__" is a convention to tell the user using your module not to change the value


def sum1(the_list):
    global __counter
    __counter += 1
    the_sum = 0
    for element in the_list:
        the_sum += element
    return the_sum


def prod1(the_list):
    global __counter
    __counter += 1
    prod = 1
    for element in the_list:
        prod *= element
    return prod

if __name__ == "__main__":
    print("I prefer to be a module, but i can do some tests for you.")
    my_list = [i+1 for i in range(5)]
    print(sum1(my_list) == 15)
    print(prod1(my_list) == 120)
else:
    print("I like to be a module.")



