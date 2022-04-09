# 3.2.1.5 - stack: the object approach cont.

# any changes you make inside the constructor (__init__) that modifies the state of the 
# self parameter will be reflected in the newly created object.

class Stack:
    def __init__(self):
        self.stack_list = []

stack_object = Stack()
print(len(stack_object.stack_list))

#NOTE: 
    # dotted notation is used, just like when invoking methods;
    # general convention for accessing an objects properties
    # you need to name the object put a "." after it and specify the desired property's name
    # DON'T USE parentheses - you don't want to invoke a method - you want to access a property

    #if you set a property's value for the very first time (like in the constructorp), you are creating it;
    # from that moment on, the object has got the property and is ready to use its value;

    # we've tried to acces the stack_list property from outside the class immediately after the object has been created;
    # we want to check the current length of the stack