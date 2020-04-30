"""
Given an array of non-negative integers, you are initially positioned at the first index of the array.

Each element in the array represents your maximum jump length at that position.

Determine if you are able to reach the last index.
"""

# Example 1:

# Input: [2,3,1,1,4]
# Output: true
# Explanation: Jump 1 step from index 0 to 1, then 3 steps to the last index.

# Example 2:

# Input: [3,2,1,0,4]
# Output: false
# Explanation: You will always arrive at index 3 no matter what. Its maximum
#              jump length is 0, which makes it impossible to reach the last index.

#Solution
# https://leetcode.com/problems/jump-game/discuss/596454/Python-Simple-solution-with-thinking-process-Runtime-O(n)

nums = [3,2,1,1,4]

def canJump(nums):
    last_position = len(nums)-1
   
    for i in range(len(nums)-2,-1,-1): # Iterate backwards from second to last item until the first item
       if (i + nums[i]) >= last_position: # If this index has jump count which can reach to or beyond the last position
           last_position = i # Since we just need to reach to this new index
    return last_position == 0	


print(canJump(nums))
