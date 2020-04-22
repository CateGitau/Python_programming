"""
Given an array of integers and an integer k, 
you need to find the total number of continuous subarrays whose sum equals to k.
"""

# Example 1:

# Input:nums = [1,1,1], k = 2
# Output: 2

nums = [1,2,3]
k = 3

# it works but not optimal smh

def subarraySum(nums, k):
    count = 0
    for i in range(len(nums)+1):
        for j in range(i + 1, len(nums) + 1):
            subs = nums[i:j]
            total = sum(subs)
            if total == k:
                count+= 1

    return count



# trying dictionary way
import collections

def subarraySum2(nums, k):
    running_sum = 0
    hash_table = collections.defaultdict(lambda:0)
    total = 0
    for x in nums:
        running_sum += x
        sum = running_sum - k
        if sum in hash_table:
            total += hash_table[sum]
        if running_sum == k:
            total += 1
        hash_table[running_sum] += 1
    return total

print(subarraySum2(nums, k))
            
