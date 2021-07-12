class Node(object):
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedList(object):
    def __init__(self, head = None):
        self.head = head

    def append(self, next_element):
        current = self.head
        if self.head:
            while current.next:
                current = current.next
            current.next = next_element
        else:
            self.head = next_element

    def print_list(self):
        if self.head is None:
            print('THis List is Empty')
            return False
        else:
            current = self.head
            while current.next:
                print(current.data, end='->')
                current = current.next

            print(current.data, '-> None')
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