# Find the size of a Tree

'''The size of a tree is the total number of nodes in a Tree
'''

class Node(object):
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

class BinaryTree(object):
    def __init__(self, root):
        self.root = Node(root)


    def _size_(self, node):
        if node is None:
            return 0

        else:
            return 1 + self._size_(node.left) + self._size_(node.right)

#
#           1
#         /    \
#        2      3
#       / \     /  \ 
#      4   5    6   7
#

#size of this tree is = 7



tree = BinaryTree(1)
tree.root.left = Node(2)
tree.root.right = Node(3)
tree.root.left.left = Node(4)
tree.root.left.right = Node(5)
tree.root.right.left = Node(6)
tree.root.right.right = Node(7)

print(tree._size_(tree.root))