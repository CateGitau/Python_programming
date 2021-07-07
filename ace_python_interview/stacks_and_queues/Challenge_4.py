# Implement a Queue Using Stacks


'''Implement the enqueue() and dequeue() functions using the MyStack class we created earlier.
enqueue() will insert a value into the queue and dequeue() will remove a value from the queue'''

from Stack import MyStack
# Push Function => stack.push(int)  //Inserts the element at top
# Pop Function => stack.pop()       //Removes and returns the element at top
# Top/Peek Function => stack.get_top()  //Returns top element
# Helper Functions => stack.is_empty() & stack.isFull() //returns boolean


class newQueue:
    # Can use size from argument to create stack
    def __init__(self):
        self.main_stack = MyStack()
        self.temp_stack = MyStack()

    # Inserts Element in the Queue
    def enqueue(self, value):
        # Push the value into main_stack in O(1)
        self.main_stack.push(value)
        print(str(value) + " enqueued")

    # Removes Element From Queue
    def dequeue(self):
        # If both stacks are empty, end operation
        if self.temp_stack.is_empty() and self.main_stack.is_empty():
            return None
        # Transfer all elements to temp_stack
        while self.main_stack.is_empty() is False:
            self.temp_stack.push(self.main_stack.pop())
        # Pop the first value. This is the oldest element in the queue
        temp = self.temp_stack.pop()
        print(str(temp) + " dequeued")
        return temp
        
if __name__ == "__main__" :
    queue = newQueue()
    for i in range(5):
        queue.enqueue(i+1)
    print("----------")
    for i in range(5):
        queue.dequeue()