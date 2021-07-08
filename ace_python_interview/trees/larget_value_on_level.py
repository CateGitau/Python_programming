from collections import deque
class Node(object):
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

class BinaryTree(object):
    def __init__(self, root):
        self.root = Node(root)

    def find_largest_value(self, root):

        result = []
        if root is None:
            return result

        else:
            #initialize an empty queue
            queue = deque()
            queue.append(root)

            while queue:
                levelSize = len(queue)
                maxSize = 0
                
                for _ in range(levelSize):
                    currentNode = queue.popleft()
                    maxSize = max(maxSize, currentNode.value)

                    # insert the children of current node to the queue
                    if currentNode.left:
                        queue.append(currentNode.left)
                    if currentNode.right:
                        queue.append(currentNode.right)
            
                result.append(maxSize)
        return result 

#
#           1
#         /    \
#        2      3
#       / \     /  \ 
#      4   5    6   7
#

#averages are [1, 3, 7]



tree = BinaryTree(8)
tree.root.left = Node(3)
tree.root.right = Node(10)
tree.root.left.left = Node(1)
tree.root.left.right = Node(2)
tree.root.right.left = Node(9)
tree.root.right.right = Node(11)

print(tree.find_largest_value(tree.root))

