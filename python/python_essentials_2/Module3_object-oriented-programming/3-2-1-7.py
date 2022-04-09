# 3.2.1.7 - object approach: a stack from scratch

# 'self' parameter is needed
    # It allows the method to access entities (properties and activities/methods) carried out by the actual object
    # You cannot omit it
    # Every time Python invokes a method, it implicitly sends the current object as the first argument
    # method is obligated to have at least one parameter, which is used by python itself
    
class Stack:
    def __init__(self): # 'self' parameter is needed
        self.__stack_list = []


    def push(self, val):
        self.__stack_list.append(val)


    def pop(self):
        val = self.__stack_list[-1]
        del self.__stack_list[-1]
        return val


stack_object = Stack()

stack_object.push(3)
stack_object.push(2)
stack_object.push(1)

print(stack_object.pop())
print(stack_object.pop())
print(stack_object.pop())
