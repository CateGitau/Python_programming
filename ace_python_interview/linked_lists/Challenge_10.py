# Return the Nth node from End

'''
In the find_nth function, a certain N is specified as an arguement. 
You simply need to return the node which is N spaces away from the Node end of the linked list
'''

from LinkedList import LinkedList
from Node import Node
# Access head_node => list.get_head()
# Check if list is empty => list.is_empty()
# Delete at head => list.delete_at_head()
# Delete by value => list.delete(value)
# Search for element => list.search()
# Length of the list => list.length()
# Remove duplicates => list.remove_duplicates()
# Node class  {int data ; Node next_element;}

# Function to find the nth node from end of Linked List


#Double iteration
'''It performs two iterations on the list so the complexity is O(n)'''
def find_nth(lst, n):
    #from front
# Find Length of list
    length = lst.length() - 1

    # Find the Node which is at (len - n + 1) position from start
    current_node = lst.get_head()

    position = length - n + 1

    if position < 0 or position > length:
        return -1

    count = 0

    while count is not position:
        current_node = current_node.next_element
        count += 1

    if current_node:
        return current_node.data
    return -1


#Two Pointers
'''
A single iteration is performed, which means that time complexity is O(n).
'''

def find_nth2(lst, n):

    if lst.is_empty():
        return -1

    nth_node = lst.get_head()  # This iterator will reach the Nth node
    end_node = lst.get_head()  # This iterator will reach the end of the list

    count = 0
    while count < n:
        if end_node is None:
            return -1
        end_node = end_node.next_element
        count += 1

    while end_node is not None:
        end_node = end_node.next_element
        nth_node = nth_node.next_element

    return nth_node.data



lst = LinkedList()
lst.insert_at_head(21)
lst.insert_at_head(14)
lst.insert_at_head(7)
lst.insert_at_head(8)
lst.insert_at_head(22)
lst.insert_at_head(15)


lst.print_list()
print(find_nth(lst, 5))
print(find_nth(lst, 1))
print(find_nth(lst, 10))