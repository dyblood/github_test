# Effects and results: lists and functions

from re import S


def list_sum(lst): #lst is the parameter
    s = 0

    for elem in lst:
        s += elem
    
    return s 

print(list_sum([5, 4, 3])) #passing a list to a function

#--------------------------------------------------------------------------

def strange_list_fun(n):#n will determin how of list you want to generate
    strange_list = []

    for i in range(0, n): #n determins how long of list you will generate
        strange_list.insert(0, i) #list will be in reverse order 

    return strange_list

print(strange_list_fun(5)) #5 identifies that the range will be range(0, 5)