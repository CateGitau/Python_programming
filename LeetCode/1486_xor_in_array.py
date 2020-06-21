"""
Given an integer n and an integer start.

Define an array nums where nums[i] = start + 2*i (0-indexed) and n == nums.length.

Return the bitwise XOR of all elements of nums.
"""

n, start = 5, 0

def xorOperation(n, start):
   ans = 0
   
   for i in range(n):
       ans ^= (start + 2* i)
       
   return ans

print(xorOperation(n, start))
