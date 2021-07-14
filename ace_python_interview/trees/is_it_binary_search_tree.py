'''
In a binary search tree, each node's key value is smaller than the key
value of all nodes in the right subtree and are greater than the key values
of all nodes in the left subtree

L < N < R 
'''

##################################### HAS ISSUE #########################################
import sys

class Node(object):
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None


# def is_bst_rec(root, min_value, max_value):
#   if root == None:
#     return True

#   if root.data < min_value or root.data > max_value:
#     return False

#   return is_bst_rec(root.left, min_value, root.data) and is_bst_rec(root.right, root.data, max_value)

# def is_bst(root):
#   return is_bst_rec(root, -sys.maxsize - 1, sys.maxsize)
def is_bst_rec(root, min_value, max_value):
  if root == None:
    return True

  if root.data < min_value or root.data > max_value:
    return False

  return is_bst_rec(root.left, min_value, root.data) and is_bst_rec(root.right, root.data, max_value)

def is_bst(root):
  return is_bst_rec(root, -sys.maxsize - 1, sys.maxsize)


#
#           8
#         /    \
#        3      10
#       / \     /  \ 
#      1   2    6   7
#

#True



root = Node(100)
root.left = Node(50)
root.right = Node(200)
# root.left.left = Node(1)
# root.left.right = Node(2)
# # root.right.left = Node()
# root.right.right = Node(9)

if is_bst(root) == True:
    print('True')
else:
    print('False')

