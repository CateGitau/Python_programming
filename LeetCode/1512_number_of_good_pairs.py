'''
Given an array of integers nums.

A pair (i,j) is called good if nums[i] == nums[j] and i < j.

Return the number of good pairs.
'''

nums = [1,2,3,1,1,3]


def numIdenticalPairs(nums):
    pairs = 0
    for i in range(len(nums)):
        for j in range(i+1, len(nums)):
            if nums[i] == nums[j]:
                pairs += 1
    return pairs


print(numIdenticalPairs(nums))


