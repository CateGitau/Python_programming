# Search in a Singly Linked List
# takes 0(n) time complexity because you traverse the whole list until we find the desired value

class Node:
    def __init__(self, data):
        self.data = data
        self.next_element = None


class LinkedList:
    def __init__(self):
        self.head_node = None

    def get_head(self):
        return self.head_node

    def is_empty(self):
        if(self.head_node is None):  # Check whether the head is None
            return True
        else:
            return False

    # Inserts a value at the end of the list
    def insert_at_tail(self, value):
        # Creating a new node
        new_node = Node(value)

        # Check if the list is empty, if it is simply point head to new node
        if self.get_head() is None:
            self.head_node = new_node
            return

        # if list not empty, traverse the list to the last node
        temp = self.get_head()

        while temp.next_element is not None:
            temp = temp.next_element

        # Set the nextElement of the previous node to new node
        temp.next_element = new_node
        return

    # Supplementary print function
    def print_list(self):
        if(self.is_empty()):
            print("List is Empty")
            return False
        temp = self.head_node
        while temp.next_element is not None:
            print(temp.data, end=" -> ")
            temp = temp.next_element
        print(temp.data, "-> None")
        return True

#iterative solution
#0(1) space complexity
def search(lst, value):
    # start from the first element

    current = lst.get_head()

    while current:
        if current.data == value:
            return True
        #else, continue traversing
        current = current.next_element
    return False

#recursive solution
#O(n) space complexity 
def search(node, value):

    # Base case
    if(not node):
        return False  # value not found

    # check if the node's data matches our value
    if(node.data is value):
        return True  # value found

    # Recursive call to next node in the list
    return search(node.next_element, value)


#test
lst = LinkedList()
lst.insert_at_tail(1)
lst.insert_at_tail(2)
lst.insert_at_tail(3)

print(search(lst, 2))

print(lst.print_list())