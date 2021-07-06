# Remove Duplicates from LinkedList


'''
When a linked list is passed to this function, it removes any node which is a duplicate of another existing node
'''

from LinkedList import LinkedList
from Node import Node

def remove_duplicates(lst):
    if lst.is_empty():
        return None

    # If list only has one node, leave it unchanged
    if lst.get_head().next_element is None:
        return lst

    outer_node = lst.get_head()
    while outer_node:
        inner_node = outer_node #iterator of the ineer loop
        while inner_node:
            if inner_node.next_element:
                if outer_node.data == inner_node.next_element.data:
                    #Duplicate found, so now removing it
                    new_next_element = inner_node.next_element.next_element
                    inner_node.next_element = new_next_element
                
                else:
                    #Otherwise simply iterate ahead
                    inner_node = inner_node.next_element
            else:
                #Otherwise simply iterate
                inner_node = inner_node.next_element
        outer_node = outer_node.next_element
