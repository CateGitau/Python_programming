# Given an array nums containing n distinct numbers in the range [0, n], 
# return the only number in the range that is missing from the array.

# Follow up: Could you implement a solution using only O(1) extra space complexity and O(n) runtime complexity?


nums = [3,0,1]

def missingNum(nums):
    n = len(nums)

    for i in range(n+1):
        if i not in nums:
            return i

print(missingNum(nums))


# class Solution(object):
#     def missingNumber(self, nums):
#         return sum(range(len(nums)+1)) - sum(nums)  

# class Solution:
#     def missingNumber(self, nums: List[int]) -> int:
#         n = len(nums)
#         return(int(n*(n+1)/2-sum(nums)))