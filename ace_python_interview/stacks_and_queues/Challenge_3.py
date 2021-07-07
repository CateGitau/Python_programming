# Reversing First k Elelements of Queue
from Queue import MyQueue
from Stack import MyStack

'''The time complexity of this function is O(n)O(n)O(n) where n is the size of the queue as the entire queue is iterated over.
'''

def reverseK(queue, k):
    # Handling invalid input
    if queue.is_empty() is True or k > queue.size() or k < 0:
        return None

    stack = MyStack()
    for i in range(k):
        stack.push(queue.dequeue())
    while stack.is_empty() is False:
        queue.enqueue(stack.pop())
        
    size = queue.size()

    for i in range(size - k):
        queue.enqueue(queue.dequeue())
        # print(queue.queue_list)

    return queue

if __name__ == "__main__" :
    # testing our logic
    queue = MyQueue()
    queue.enqueue(1)
    queue.enqueue(2)
    queue.enqueue(3)
    queue.enqueue(4)
    queue.enqueue(5)
    queue.enqueue(6)
    queue.enqueue(7)
    queue.enqueue(8)
    queue.enqueue(9)
    queue.enqueue(10)
    print("the queue before reversing:")
    print(queue.queue_list)
    reverseK(queue, 5)
    print("the queue after reversing:")
    print(queue.queue_list)