class Element():
    def __init__(self, value):
        self.value = value
        self.next = None


class LinkedLists():
    def __init__(self, head = None):
        self.head = head

    #appending a value at the end of the linked list

    def append(self, new_element):
        current = self.head

        if self.head:
            while current.next:
                current = current.next
                current.next = new_element
        else:
            self.head = new_element


    def search(self, element):
        current = self.head

        while current:
            if current.value == element:
                return True
            current = current.next

        return False

e1 = Element(1)
e2 = Element(2)
e3 = Element(3)
e4 = Element(4)

#start setting up a linkedlist
ll = LinkedLists(e1)
ll.append(e2)
ll.append(e3)

print(ll.search(9))