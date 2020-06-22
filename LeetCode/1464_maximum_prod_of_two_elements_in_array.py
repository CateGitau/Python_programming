"""
Given the array of integers nums, you will choose two different indices i and j of that array.
Return the maximum value of (nums[i]-1)*(nums[j]-1)
"""

nums = [10,2,5,2]


def maxProduct(nums):
    
    maxim = 0
    for i in range(len(nums)):
        for j in range(len(nums)):
            if i != j:
                ans = ((nums[i]-1)*(nums[j]-1))
                if ans > maxim:
                    maxim = ans

    return maxim


print(maxProduct(nums))

