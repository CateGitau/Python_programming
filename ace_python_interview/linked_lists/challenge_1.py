# Insertion at Tail
'''
We need to insert a new object at the end of the linked list. You can naturally guess, that this newly added node will point to None as it is at the tail.
'''
#time complexity is O(n) because it traverses the whole list

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

def insert_at_position(lst, value, position):
    #new element
    new_element = Node(value)

    #checking if head is None
    # if lst.get_head() is None:
    #     new_element.next_element = lst.head_node
    #     lst.head_node = new_element
    #     return
    
    counter = 1
    current = lst.get_head()

    if position > 1:
        while current and counter < position:
            if counter == position - 1:
                new_element.next_element = current.next_element
                current.next_element = new_element

            current = current.next_element
            counter +=1

    elif position ==1:
        new_element.next = current
        current = new_element

    return



'''
In deletion In the worst case, you would have to traverse until the end of the list. This means the time complexity will be O(n).
'''


#test
if __name__ == "__main__":

    lst = LinkedList()
    insert_at_tail(lst, 1)
    insert_at_tail(lst, 2)
    insert_at_tail(lst, 3)

    print(insert_at_position(lst, 6, 2))

    print(lst.print_list())

    print(search_recursive(lst.get_head(), 3))
