
"""
Given an array of integers, 
return indices of the two numbers such that they add up to a specific target.

You may assume that each input would have exactly one solution,
and you may not use the same element twice.
"""

nums = [2, 7, 11, 15]
target = 9



def TwoSum(nums, target):
    for i in range(0, len(nums)):
        if target-nums[i] in nums[i+1:]:
            return [i, nums.index(target-nums[i])]

print(TwoSum(nums, target))
