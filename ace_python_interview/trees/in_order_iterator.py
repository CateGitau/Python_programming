# Write and in-order iterator for a Binary Tree

'''
We are given the root of a binary tree. We have to write an iterator that takes in this root and iterates through the nodes of a binayr tree in an in-order way
'''

class Node(object):
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None


class InorderIterator:
    def __init__(self, root):
        self.stk = []

    # Assuming that when iterator is initialized
    # it is always at the first element of tree in its in-order
        self.populate_iterator(root)
    
    def populate_iterator(self, root):
        while root!= None:
            self.stk.append(root)
            root = root.left

    def hasNext(self):
        if not self.stk:
            return False
        else:
            return True

    # getNext returns null if there are no more elements in tree
    def getNext(self):
        if not self.stk:
            return None

        r_val = self.stk[-1]
        del self.stk[-1]

        #self.stk.remove(-1)
        temp = r_val.right
        self.populate_iterator(temp)


        return r_val

    # if you need to provide current element, that will be at top of stack always
def inorder_using_iterator(root):
    iter = InorderIterator(root)
    mystr = ""
    while iter.hasNext():
        ptr = iter.getNext()
        mystr += str(ptr.data) + " "
    return mystr


root1 = Node(100)
root1.left = Node(50)
root1.left.left = Node(25)
root1.left.right = Node(75)
root1.right = Node(250)
root1.right.left = Node(125)
root1.right.right = Node(300)

print("Inorder Iterator = ", end = "")
print(inorder_using_iterator(root1))