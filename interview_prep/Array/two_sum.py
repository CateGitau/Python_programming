'''
Given an array of integers nums and an integer target, return indices of the two numbers such that they add up to target.

You may assume that each input would have exactly one solution, and you may not use the same element twice.

You can return the answer in any order.
'''

nums = [3,2,4]
target = 6

def two_sum(nums, target):
    d = {}

    for i, n in enumerate(nums):

        if target-n in d:
            return [d[target-n], i]

        d[n]=i

print(two_sum(nums, target))


