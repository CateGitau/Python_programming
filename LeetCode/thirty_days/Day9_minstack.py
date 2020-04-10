"""
Design a stack that supports push, pop, top, and retrieving the minimum element in constant time.

    push(x) -- Push element x onto stack.
    pop() -- Removes the element on top of the stack.
    top() -- Get the top element.
    getMin() -- Retrieve the minimum element in the stack.

"""

class MinStack(object):

    def __init__(self):
        """
        initialize your data structure here.
        """
        self.elements = []
        self.min_elements = []



    def push(self, x):
        """
        :type x: int
        :rtype: None
        """
        if len(self.elements) == 0:
            self.min_elements.append(x)
        else:
            self.min_elements.append(min(self.min_elements[len(self.elements)- 1], x))

        self.elements.append(x)
    def pop(self):
        """
        :rtype: None
        """
        self.min_elements.pop()
        return self.elements.pop()
        

    def top(self):
        """
        :rtype: int
        """
        return self.elements[len(self.elements) -1]

    def getMin(self):
        """
        :rtype: int
        """
        return self.min_elements[len(self.elements)- 1]

# Your MinStack object will be instantiated and called as such:
obj = MinStack()
obj.push(-1)
#obj.push(0)
#obj.push(-3)
print(obj)
print(obj.top())

print(obj.getMin())
#obj.pop()



#param_4 = obj.getMin()
#print(param_4)

