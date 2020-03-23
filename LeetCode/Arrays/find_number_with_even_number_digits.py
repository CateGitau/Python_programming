"""
Given an array nums of integers, return how
many of them contain an even number of digits.
"""

nums = [12,345,2,6,7896]
def Findnumbers(nums):
    even = 0

    for i in nums:
        if len(str(i)) % 2 == 0:
            even += 1
    return even

print(Findnumbers(nums))