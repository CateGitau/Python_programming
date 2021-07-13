class Node(object):
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

class BinaryTree(object):
    def __init__(self, root):
        self.root = Node(root)


root=BinaryTree(1)
root.left = BinaryTree(2)
root.right = BinaryTree(3)
root.left.right= BinaryTree(4)
root.left.left = BinaryTree(5)
root.right.left = BinaryTree(6)
root.right.right = BinaryTree(7)
