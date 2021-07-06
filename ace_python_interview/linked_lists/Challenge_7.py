# Find Middle Node of Liked List

'''
Implement a function that will take a linked list as an input and return the value of the middle node.
If the length of the list is even, the middle value will occur at length/2. For a list of odd length, the middle value will be (length+1)/2
'''

from Node import Node
from LinkedList import LinkedList

#my solution
def find_mid(lst):
    current = lst.get_head()
    lst_len = lst.length()

    if lst_len % 2 == 0:
        pos = lst_len//2

    else:
        pos = (lst_len +1)//2

    get_pos = 0

    while current:
        get_pos += 1
        if get_pos == pos:
            return current.data
        else:
            current = current.next_element


#Brute Force 

'''
The algorithm makes a linear traversal over the list. Hence, the time complexity is O(n).
'''

def find_mid2(lst):
    if lst.is_empty():
        return None

    node = lst.get_head()
    mid = 0
    if lst.length() % 2 == 0:
        mid = lst.length()//2
    else:
        mid = lst.length()//2 + 1

    for i in range(mid - 1):
        node = node.next_element

    return node.data


# Two Pointers
'''
We are traversing the linked list at twice the speed, so it is certainly faster. However, the bottleneck complexity is still O(n).
'''

def find_mid3(lst):
    if lst.is_empty():
        return -1

    current_node = lst.get_head()

    if current_node.next_element == None:
		#Only 1 element exist in array so return its value.
        return current_node.data
    
    mid_node = current_node
    current_node = current_node.next_element.next_element

    while current_node:
        mid_node = mid_node.next_element
        current_node = current_node.next_element

        if current_node:
            current_node = current_node.next_element
    if mid_node:
        return mid_node.data
    return -1
        





lst = LinkedList()
lst.insert_at_head(22)
lst.insert_at_head(21)
lst.insert_at_head(10)
lst.insert_at_head(14)
lst.insert_at_head(7)

lst.print_list()
print(find_mid3(lst))
