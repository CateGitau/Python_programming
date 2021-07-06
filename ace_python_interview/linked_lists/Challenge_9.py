# Union & Intersection of Liked Lists

'''
Union and intersection are two most popular operations which can be performed on data sets. Now, 
you will be implementing them for linked lists'''

from LinkedList import LinkedList
from Node import Node

'''If we did not have to care for duplicates, The runtime complexity of this algorithm would be O(m) where m is the size of the first list. 
However, because of duplicates, we need to traverse the whole union list. #
This increases the time complexity to O(l2)O(l^2)O(l​2​​) where l = m + n. Here, m is the size of the first list, and n is the size of the second list.'''

def union(list1, list2):
    # Return other list if one of them is empty

    # if (list1.is_empty()):
    #     return elements(list2)
    # elif (list2.is_empty()):
    #     return elements(list1)

    start = list1.get_head()

    #Traverse the first list till the tail
    while start.next_element:
        start = start.next_element
    
    #Link the last element of first list to the first element of the second list
    start.next_element = list2.get_head()
    list1.remove_duplicates()
    return list1

ulist1 = LinkedList()
ulist2 = LinkedList()
ulist1.insert_at_head(8)
ulist1.insert_at_head(22)
ulist1.insert_at_head(15)

print("List 1")
ulist1.print_list()

ulist2.insert_at_head(21)
ulist2.insert_at_head(14)
ulist2.insert_at_head(7)

print("List 2")
ulist2.print_list()

new_list = union(ulist1,ulist2)

print("Union of list 1 and 2")
new_list.print_list()

def intersection(list1, list2):
    result = LinkedList()
    visited_nodes = set()  # Keep track of all the visited nodes
    current_node = list1.get_head()

    # Traversing list1 and adding all unique nodes into the hash set
    while current_node:
        value = current_node.data
        if value not in visited_nodes:
            visited_nodes.add(value)  # Visiting current_node for first time
        current_node = current_node.next_element

    start = list2.get_head()

    # Traversing list 2
    # Nodes which are already present in visited_nodes are added to result
    while start:
        value = start.data
        if value in visited_nodes:
            result.insert_at_head(start.data)
        start = start.next_element
    result.remove_duplicates()
    return result





ilist1 = LinkedList()
ilist2 = LinkedList()

ilist1.insert_at_head(14)
ilist1.insert_at_head(22)
ilist1.insert_at_head(15)

ilist2.insert_at_head(21)
ilist2.insert_at_head(14)
ilist2.insert_at_head(15)

lst = intersection(ilist1, ilist2)
print("Intersection of list 1 and 2")
lst.print_list()