
class Node(object):
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

def printPreorder(root):
    if root:
        print(root.value)
        printPreorder(root.left)
        printPreorder(root.right)

def printInorder(root):
    if root:
        printInorder(root.left)
        print(root.value)
        printInorder(root.right)


def printPostorder(root):
    if root:
        printPostorder(root.left)
        printPostorder(root.right)
        print(root.value)


# Driver code
root = Node(1)
root.left = Node(2)
root.right = Node(3)
root.left.left = Node(4)
root.left.right = Node(5)
print ("Preorder traversal of binary tree is")
printPreorder(root)
 
print ("\nInorder traversal of binary tree is")
printInorder(root)
 
print ("\nPostorder traversal of binary tree is")
printPostorder(root)