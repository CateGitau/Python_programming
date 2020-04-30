"""
Given a 2D binary matrix filled with 0's and 1's, 
find the largest square containing only 1's and return its area.
"""

# Example:

# Input: 

# 1 0 1 0 0
# 1 0 1 1 1
# 1 1 1 1 1
# 1 0 0 1 0

# Output: 4


#solution
#https://leetcode.com/problems/maximal-square/discuss/600149/Python-Thinking-Process-Diagrams-DP-Approach

arr = [[1,0,1,0,0],
[1,0,1,1,1],
[1,1,1,1,1],
[1,0,0,1,0]]

print(arr)
def maximalSquare(matrix):
    if matrix is None or len(matrix) < 1:
            return 0
            
    rows = len(matrix)
    cols = len(matrix[0])

    dp = [[0]*(cols+1) for _ in range(rows+1)]
    max_side = 0
        
    for r in range(rows):
        for c in range(cols):
            if matrix[r][c] == '1':
                dp[r+1][c+1] = min(dp[r][c], dp[r+1][c], dp[r][c+1]) + 1 
                max_side = max(max_side, dp[r+1][c+1])

    return max_side * max_side

print(maximalSquare(arr))