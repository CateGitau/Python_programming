#Linked Lists


class Node(object):
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedList(object):
    def __init__(self):
        self.head = None
    
    # def get_head(self):
    #     return self.head

    #check if empty
    # def is_empty(self):
    #     if self.head is None:
    #         return True
    #     else:
    #         return False

    def append(self, new_element):
        current  = self.head
        if self.head:
            while current.next:
                current = current.next
            current.next  = new_element
        else:
            self.head = new_element
        
    #print function
    def print_list(self):
        if self.head is None:
            print('List is empty')
            return False
        temp = self.head
        while temp.next is not None:
            print(temp.data, end='->')
            temp = temp.next
        print(temp.data, "-> None")
        return True

# Set up some Elements
e1 = Node(1)
e2 = Node(2)
e3 = Node(3)
e4 = Node(4)

# Start setting up a LinkedList
ll = LinkedList()
ll.append(e1)
ll.append(e2)
ll.append(e3)
ll.append(e4)

ll.print_list()


