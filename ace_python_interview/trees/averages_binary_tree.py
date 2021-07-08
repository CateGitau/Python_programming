from collections import deque
class Node(object):
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

class BinaryTree(object):
    def __init__(self, root):
        self.root = Node(root)


    def find_level_averages(self, root):
        result = []

        if root is None:
            return result

        #initializes empty queue
        queue = deque()

        #appends the root
        queue.append(root)

        #while queue is not empty
        while queue:
            #get the length of the queue
            levelSize = len(queue)
            levelSum = 0.0

            for _ in range(levelSize):
                currentNode = queue.popleft()
                #add the nnode's value to tje running sum
                levelSum += currentNode.value
                #insert the children of the current node to the queue
                if currentNode.left:
                    queue.append(currentNode.left)
                if currentNode.right:
                    queue.append(currentNode.right)

            #append the current level's average to the result array
            result.append(levelSum /levelSize)

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