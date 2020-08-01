"""
Given the root node of a binary search tree, 
return the sum of values of all nodes with value between L and R (inclusive).

The binary search tree is guaranteed to have unique values.
"""

class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution(object):
    def rangeSumBST(self, root, L, R):
        """
        :type root: TreeNode
        :type L: int
        :type R: int
        :rtype: int
        """
        def dfs(node):
            if node:
                if L <= node.val <= R:
                    self.ans += node.value
                if L < node.val:
                    dfs(node.left)
                if node.val < R:
                    dfs(node.right)


    self.ans = 0
    dfs(root)
    return self.ans

sol = Solution()

