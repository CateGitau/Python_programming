"""
Given an integer array nums, find the contiguous subarray (containing at least one number) 
which has the largest sum and return its sum.
"""
nums =  [0,1,0,3,12]

def moveZeros2(nums):
    for i in range(len(nums)):
        counts = 0
        if nums[i] == 0:
            counts+= 1
            new_ = counts * [0]
            nums.remove(nums[i])
            nums.extend(new_)
    return(nums)

#Not optimal solution
def moveZeros(nums):
    for i in range(len(nums)):
        if nums[i] == 0:
            nums.remove(nums[i])
            nums.append(0)

    return(nums)


print(moveZeros2(nums))



