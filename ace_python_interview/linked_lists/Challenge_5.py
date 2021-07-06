# Reverse a Singly linked list


from Node import Node
from LinkedList import LinkedList

'''The algorithm runs in O(n) since the list is traversed once.'''

def reverse(lst):
    # To reverse linked, we need to keep track of three things
    previous = None # Maintain track of the previous node
    current = lst.get_head() # The current node
    next = None # The next node in the list

    while current:
        next = current.next_element
        current.next_element = previous
        previous = current
        current = next

    #Set the last element as the new head node
    lst.head_node = previous
    
    return lst

lst = LinkedList()
lst.insert_at_head(1)
lst.insert_at_head(4)
lst.insert_at_head(3)
lst.insert_at_head(2)
lst.print_list()

lst = reverse(lst)
lst.print_list()