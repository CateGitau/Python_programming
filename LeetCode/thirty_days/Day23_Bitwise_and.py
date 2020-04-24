
"""
Given a range [m, n] where 0 <= m <= n <= 2147483647, 
return the bitwise AND of all numbers in this range, inclusive.
"""

# Example 1:

# Input: [5,7]
# Output: 4

# Example 2:

# Input: [0,1]
# Output: 0

#solution from: https://leetcode.com/problems/bitwise-and-of-numbers-range/discuss/56719/JavaPython-easy-solution-with-explanation

def rangeBitwiseAnd(self, m, n):
    i = 0
    while m != n:
        m >>= 1
        n >>= 1
        i += 1
    return n << i
