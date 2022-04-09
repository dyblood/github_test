# 3.2.1.10 - object approach: a stack from scratch


class Stack: # superclass
    def __init__(self):
        self.__stack_list = []

    def push(self, val):
        self.__stack_list.append(val)

    def pop(self):
        val = self.__stack_list[-1]
        del self.__stack_list[-1]
        return val

# new class to evaluate the sum of all the elements currently stored in the stack
# subclass recieves all the componenets of the superclass
class AddingStack(Stack): # making subclass of the (Stack) class
    def __init__(self):
        Stack.__init__(self) # must explicitly invoke a superclass's constructor
                             # NOTE: if you don't do this you won't have access to __stack_list[]
        self.__sum = 0 # making a private variable so nobody manipulates the sum value


# Note the syntax:

    # you specify the superclass's name (this is the class whose constructor you want to run)

    # you put a dot (.)after it;
    
    # you specify the name of the constructor;
    
    # you have to point to the object (the class's instance) which has to be initialized by the constructor
    #  - this is why you have to specify the argument and use the self variable here; 
    # NOTE: invoking any method (including constructors) from outside the class never requires you to put
    #  the self argument at the argument's list - invoking a method from within the class demands explicit 
    # usage of the self argument, and it has to be put first on the list.