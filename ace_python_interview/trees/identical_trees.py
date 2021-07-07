# Check if two binary trees are identical

'''
Given the roots of two binary trees, determine if these trees are identical or not. 
Identical trees have the same layout and data at each node. Consider the following two identical binary trees that have the same layout and data.
'''

#The runtime of this solution is linear O(n)

class Node(object):
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

# class BinaryTree():
#     def __init__(self, root):
#         self.root = Node(root)

#     def search(self, find_val):
#         return self.preorder_search(tree1.root, find_val)

#     def print_tree(self):
#         return self.preorder_print(tree1.root, "")[:-1]

#     def preorder_search(self, start, find_val):
#         if start:
#             if start.value == find_val:
#                 return True
#             else:
#                 return self.preorder_search(start.left, find_val) or self.preorder_search(start.right, find_val)
    
#     def preorder_print(self, start, traversal):
#         if start:
#             traversal += (str(start.value) + "-")
#             traversal = self.preorder_print(start.left, traversal)
#             traversal = self.preorder_print(start.right, traversal)
#         return traversal

# Set up tree
root1 = Node(100)
root2 = Node(100)

root1.left = Node(50)
root1.right = Node(200)
root1.left.left = Node(25)
root1.right.left = Node(125)
root1.right.right = Node(350)

root2.left = Node(50)
root2.right = Node(200)
root2.left.left = Node(25)
root2.right.left = Node(125)
root2.right.right = Node(350)


def are_identical(root1, root2):
    if root1 == None and root2 == None:
        return True
    if root1 != None and root2 != None:
        return (root1.value == root2.value and
                are_identical(root1.left, root2.left) and
                are_identical(root1.right, root2.right))
    return False

if(are_identical(root1, root2)):
  print("The trees are identical")
else:
  print("The trees are not identical")