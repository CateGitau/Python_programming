"""
Given the array nums consisting of 2n elements in the form [x1,x2,...,xn,y1,y2,...,yn].

Return the array in the form [x1,y1,x2,y2,...,xn,yn].
"""

nums = [2,5,1,3,4,7]
n = 3



# def shuff_array(nums, n):
#     x = nums[:n]
#     y = nums[n:]

#     shuff = []
#     for i,j in zip(x, y):
#         shuff.append(i)
#         shuff.append(j)

#     return shuff

print(shuff_array(nums, n))
        
