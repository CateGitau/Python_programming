from collections import deque

class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None


class BinaryTree:
    def __init__(self, root):
        self.root = Node(root)

    def find_level_averages(self, root):
        result = []
        if root is None:
            return

        queue = deque()
        queue.append(root)

        while queue:
            levelLen = len(queue)
            levelSum = 0.0

            for _ in range(levelLen):
                currentNode = queue.popleft()
                levelSum+= currentNode.value

                if currentNode.left:
                    queue.append(currentNode.left)

                if currentNode.right:
                    queue.append(currentNode.right)

            result.append(levelSum/levelLen)
        return result



#
#           1
#         /    \
#        2      3
#       / \     /  \ 
#      4   5    6   7
#

#averages are [1, 2.5, 5.5]



tree = BinaryTree(1)
tree.root.left = Node(2)
tree.root.right = Node(3)
tree.root.left.left = Node(4)
tree.root.left.right = Node(5)
tree.root.right.left = Node(6)
tree.root.right.right = Node(7)

print(tree.find_level_averages(tree.root))