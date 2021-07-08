class Node(object):
    def __init__(self, data):
        self.data = data
        self.right = None
        self.left = None

class BST(object):
    def __init__(self, root):
        self.root = Node(root)

    def insert(self, new_value):
        self.insert_helper(self.root, new_value)

    def insert_helper(self, current, new_value):
        if current.data < new_value:
            if current.right:
                self.insert_helper(current.right, new_value)
            else:
                current.right = Node(new_value)
        else:
            if current.left:
                self.insert_helper(current.left, new_value)
            else:
                current.left = Node(new_value)


#
#           1
#         /    \
#        2      3
#       / \     /  \ 
#      4   5    6   7
#

#averages are [1, 2.5, 5.5]



tree = BST(1)
tree.root.left = Node(2)
tree.root.right = Node(3)
tree.root.left.left = Node(4)
tree.root.left.right = Node(5)
tree.root.right.left = Node(6)
tree.root.right.right = Node(7)

print(tree.insert(10))