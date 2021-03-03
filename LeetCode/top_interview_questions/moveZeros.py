'''
Given an array nums, write a function to move all 0's 
to the end of it while maintaining the relative order of the non-zero elements.
'''

nums = [0,1,0,3,12]


def moveZeros(nums):
    

    for i in range(len(nums)):
        counts = 0
        if nums[i] == 0:
            counts+=1
            new_ = counts * [0]
            nums.remove(nums[i])
            nums.extend(new_)
    return nums

print(moveZeros(nums))
