# Detect Loop in a Linked List

'''
Loops in linked lists can be dangerous as they can end up programs iterating linked lists indefinitely. Now, you'll create an algorithm to detect them.
a loop is formed when a node in your linked list points to a previously traversed node.
'''

from Node import Node
from LinkedList import LinkedList

#my solution
def detect_loop(lst):
    values = []

    current = lst.get_head()

    while current:
        if current.data not in values:
            values.append(current.data)

        else:
            return True 
        
        current = current.next_element
    return False

#Floyd's Cycle-Finding Algorithm
'''This is perhaps the fastest algorithm for detecting a linked list loop. We keep track of two iterators, onestep and twostep
onestep moves forward one node at a time, while twostep iterates over two nodes. In this way, twostep is the faster iterator.
By principle, if a loop exists, the wto iterators will meet. Whenever this condition is fulfilled, the function returns true'''

'''
We iterate the list once. On average, lookup in a list takes O(1) time, which makes the total running time of this solution O(nnn). 
However, if we use sets in place of lists to store visited nodes , 
then a single look-up may take O(nnn) time. This can cause the algorithm to take O(n2n^2n​2​​) time.
'''
def detect_loop2(lst):
    #keep two iterators
    onestep = lst.get_head()
    twostep = lst.get_head()

    while onestep and twostep and twostep.next_element:
        onestep = onestep.next_element
        twostep = twostep.next_element.next_element

        if onestep == twostep:
            return True
    return False

lst = LinkedList()

lst.insert_at_head(21)
lst.insert_at_head(14)
lst.insert_at_head(7)

# Adding a loop
head = lst.get_head()
node = lst.get_head()

for i in range(4):
    if node.next_element is None:
        node.next_element = head.next_element
        break
    node = node.next_element

print(detect_loop2(lst))