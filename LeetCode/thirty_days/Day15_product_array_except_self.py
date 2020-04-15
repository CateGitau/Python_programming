"""
Given an array nums of n integers where n > 1,  
return an array output such that output[i] is equal to the product of all the elements of nums except nums[i].
"""

# Example:

# Input:  [1,2,3,4]
# Output: [24,12,8,6]

# Constraint: It's guaranteed that the product of the elements of any prefix or suffix of the array 
# (including the whole array) fits in a 32 bit integer.

# Note: Please solve it without division and in O(n).

# Follow up:
# Could you solve it with constant space complexity? (The output array does not count as extra 
# space for the purpose of space complexity analysis.)

nums = [1,2,3,4]

def productExceptSelf(nums):
    """
    :type nums: List[int]
    :rtype: List[int]
    """
    """
    # Two passes (forward and backward). Example:
        [2,     3,       4,      5]
        -->     2       2*3    2*3*4
        5*4*3   5*4      5      <--
    
    Finally, combine results in each column.
    """
    if len(nums) <= 1:
        return nums
    res = [1]*len(nums)
    temp = nums[0]
    for i in range(1, len(nums)):
        res[i] = temp
        temp *= nums[i]
    temp = nums[-1]
    for i in range(len(nums)-1)[::-1]:
        res[i] = res[i]*temp
        temp *= nums[i]
    return res


print(productExceptSelf(nums)) 
