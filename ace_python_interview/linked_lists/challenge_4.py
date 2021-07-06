#Find the length of a LInked List
#Length of List == # of Nodes 

from Node import Node
from LinkedList import LinkedList

'''
Since this is a linear algorithm, the time complexity will be O(n).
'''
def length(lst):
    current =  lst.get_head()

    counter = 0

    while current:
        counter+=1
        current = current.next_element
    
    return counter


lst = LinkedList()
lst.insert_at_head(1)
lst.insert_at_head(4)
lst.insert_at_head(3)
lst.insert_at_head(2)
lst.insert_at_head(7)
print(length(lst))


