class Element():
    def __init__(self, value):
        self.value = value
        self.next = None

class LinkedList():
    def __init__(self, head = None):
        self.head = None

    def append(self, new_element):
        current = self.head

        if self.head:
            while current.next:
                current = current.next
                current.next = new_element
        else:
            self.head = new_element

    
    def insert(self, new_element, position):
        """Insert a new node at the given position.
        Assume the first position is "1".
        Inserting at position 3 means between
        the 2nd and 3rd elements."""

        counter = 1
        current = self.head

        while current and counter < position:
            if counter == position -1:
                new_element.next = current.next
                current.next = new_element

            current = current.next
            counter+=1
        
        if position == 1:
            new_element.next = self.head
            self.head = new_element


# Test cases
# Set up some Elements
e1 = Element(1)
e2 = Element(2)
e3 = Element(3)
e4 = Element(4)

# Start setting up a LinkedList
ll = LinkedList(e1)
ll.append(e2)
ll.append(e3)

ll.insert(e4,3)
# Should print 4 now



