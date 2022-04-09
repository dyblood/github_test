# 3.2.1.6 - stack: object approach cont.

# any class component has a name starting with two underscores (__) it becomes private
    # means that it can be accessed only from within the class

## this is how python implements the encapsulation concept

class Stack:
    def __init__(self):
        self.__stack_list = [] 

stack_object = Stack()
print(len(stack_object.__stack_list))