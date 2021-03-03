'''
Given the head of singly linked list, reverse the list, and return the reversed list
'''

#https://www.geeksforgeeks.org/reverse-a-linked-list/

# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class LinkedList:
    # Function to initialize head
    def __init__(self):
        self.head = None

    def reverseList(self):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        prev = None
        while self.head:
            curr = self.head
            self.head = self.head.next
            curr.next = prev
            prev = curr
        return prev

    # Function to insert a new node at the beginning
    def push(self, new_data):
        new_node = ListNode(new_data)
        new_node.next = self.head
        self.head = new_node

    # Utility function to print the linked LinkedList
    def printList(self):
        temp = self.head
        while(temp):
            print(temp.val)
            temp = temp.next

# Driver code
llist = LinkedList()
llist.push(1)
llist.push(2)
llist.push(3)
llist.push(4)

print(llist.printList())
print(llist.reverseList())