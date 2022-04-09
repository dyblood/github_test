# 3.2.1.14 - lab: Counting Stack

# Hints:
    # introduce a property designed to count pop operations and name it in a way which guarantees hiding it
    # initialize it to zero inside the constructor
    # provide a method which returns the value currently assigned to the counter (name it get_counter() )

class Stack:
    def __init__(self):
        self.__stk = []

    def push(self, val):
        self.__stk.append(val)

    def pop(self):
        val = self.__stk[-1]
        del self.__stk[-1]
        return val


class CountingStack(Stack):
    def __init__(self):
        Stack.__init__(self)
        self.__counter = 0

    def get_counter(self):
        return self.__counter

    def pop(self):
        self.__counter += 1
        return Stack.pop(self)
	

stk = CountingStack()
for i in range(100):
    stk.push(i)
    stk.pop()
print(stk.get_counter())