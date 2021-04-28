# Insertion at Tail
'''
We need to insert a new object at the end of the linked list. You can naturally guess, that this newly added node will point to None as it is at the tail.
'''

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

def insert_at_tail(lst, value):
    # creating a new node
    new_node = Node(value)

    #checking if head is None
    if lst.get_head() is None:
        lst.head_node = new_node
        return

    else:
        current = lst.get_head()
        while current.next_element:
            current = current.next_element
        
        current.next_element = new_node
        return

lst = LinkedList()
insert_at_tail(lst, 1)
insert_at_tail(lst, 2)
insert_at_tail(lst, 3)

print(lst.print_list())
