from collections import defaultdict
from collections import deque

class Node(object):
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

class BinaryTree(object):
    def __init__(self, root):
        self.root = Node(root)

    def levelorder_print(self, start):
        if start is None:
            return

        queue = deque()
        queue.append(start)

        traverse = ''
        while queue:
            node = queue.popleft()
            traverse+= str(node.value) + '-'

            if node.left:
                queue.append(node.left)

            if node.right:
                queue.append(node.right)

        return traverse






tree = BinaryTree(1)
tree.root.left = Node(2)
tree.root.right = Node(3)
tree.root.left.left = Node(4)
tree.root.left.right = Node(5)
tree.root.right.left = Node(6)
tree.root.right.right = Node(7)

print(tree.levelorder_print(tree.root))
