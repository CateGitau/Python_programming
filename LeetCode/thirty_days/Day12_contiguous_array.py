"""
Given a binary array, find the maximum length of a contiguous subarray with equal number of 0 and 1. 
"""

# Example 1:

# Input: [0,1]
# Output: 2
# Explanation: [0, 1] is the longest contiguous subarray with equal number of 0 and 1.

# Example 2:

# Input: [0,1,0]
# Output: 2
# Explanation: [0, 1] (or [1, 0]) is a longest contiguous subarray with equal number of 0 and 1.

# Note: The length of the given binary array will not exceed 50,000. 

nums = [0,0,1,0,0,0,1,1]
#nums = [1,0,0,1]


### not optimal, time taken to execute is long
def findMaxLength(nums):
    sub_arr = []
    for i in range(len(nums)+1):
        for j in range(i + 1, len(nums) + 1):
            subs = nums[i:j]
            zeros = 0
            ones = 0

            for m in subs:
                if m == 0:
                    zeros+= 1
                if m == 1:
                    ones += 1
            if zeros == ones:
                sub_arr.append(len(subs))

    if sub_arr:
        return max(sub_arr)
    else:
        return 0


def findMaxLength2(nums):
    dict = {}
    subarr, count = 0,0
    for i in range(len(nums)):
        if nums[i] == 1:
            count+= 1
        else:
            count += -1
        if count == 0:
            subarr = i+1
        if count in dict:
            subarr  =max(subarr, i-dict[count])
        else:
            dict[count] = i
    return subarr



print(findMaxLength2(nums))