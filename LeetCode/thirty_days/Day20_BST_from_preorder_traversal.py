"""
Return the root node of a binary search tree that matches the given preorder traversal.

(Recall that a binary search tree is a binary tree where for every node, any descendant 
of node.left has a value < node.val, and any descendant of node.right has a value > node.val. 
Also recall that a preorder traversal displays the value of the node first, then traverses node.left, 
then traverses node.right.)
"""

# Example 1:

# Input: [8,5,1,7,10,12]
# Output: [8,5,10,1,7,null,12]



# Idea is simple.
# First item in preorder list is the root to be considered.
# For next item in preorder list, there are 2 cases to consider:
# If value is less than last item in stack, it is the left child of last item.
# If value is greater than last item in stack, pop it.
#         The last popped item will be the parent and the item will be the right child of the parent.



class Solution:
    def bstFromPreorder(self, preorder: List[int]) -> TreeNode:
        root = TreeNode(preorder[0])
        stack = [root]
        for value in preorder[1:]:
            if value < stack[-1].val:
                stack[-1].left = TreeNode(value)
                stack.append(stack[-1].left)
            else:
                while stack and stack[-1].val < value:
                    last = stack.pop()
                last.right = TreeNode(value)
                stack.append(last.right)
        return root