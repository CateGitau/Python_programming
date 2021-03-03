'''
Given an integer array nums where the elements are sorted in ascending order, 
convert it to a height-balanced binary search tree.

A height-balanced binary tree is a binary tree in which the depth of 
the two subtrees of every node never differs by more than one.
'''

# Definition for a  binary tree node
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

def sortedArrayToBST(num):
    if not num:
        return None

    mid = len(num) // 2

    root = TreeNode(num[mid])
    root.left = sortedArrayToBST(num[:mid])
    root.right = sortedArrayToBST(num[mid+1:])

    return root

# Function to print tree nodes in  
# InOrder fashion  
def inOrder(root): 
    if root != None: 
        inOrder(root.left)  
        print(root.val,end=" ")  
        inOrder(root.right) 
    else:
        None

arr = [-10,-3,0,5,9] 
n = len(arr) 
root = None
root = sortedArrayToBST(arr) 
inOrder(root) 