'''
Stack FILO
A stack has the following elements:
pop() - removes an element from the top of the stack
peek() - gets/prints the top element of the stack
push(element) - adds element to stack
is_empty() - returns Boolian, True if empty False if Not
size() - returns size of stack
'''

class MyStack(object):
    def __init__(self):
        self.stack_list = []
        self.stack_size = 0

    def is_empty(self):
        return self.stack_size == 0

    def size(self):
        return self.stack_size

    def pop(self):
        if self.is_empty():
            return None
        else:
            self.stack_size -= 1
            return self.stack_list.pop()

    def peek(self):
        if self.is_empty():
            return None
        return self.stack_list[-1]
    
    def push(self, value):
        self.stack_size += 1
        self.stack_list.append(value)


if __name__== '__main__':
    stack_obj = MyStack()

    print("Pushing elements into the stack")
    for i in range(5):  
        print(i)
        stack_obj.push(i)

    print("is_empty(): " + str(stack_obj.is_empty())) 
    print("peek(): " + str(stack_obj.peek()))
    print("size(): " + str(stack_obj.size()))

    print("Popping elements from the stack")
    for x in range(5):  
        print(stack_obj.pop())

    print("is_empty(): " + str(stack_obj.is_empty()))
    print("peek(): " + str(stack_obj.peek()))
    print("size(): " + str(stack_obj.size()))

