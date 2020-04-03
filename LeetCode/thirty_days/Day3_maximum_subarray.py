"""
Given an integer array nums, find the contiguous subarray 
(containing at least one number) which has the largest 
sum and return its sum.
"""

nums =  [-2,1,-3,4,-1,2,1,-5,4]


#not so optimal solution
# Brute Force search 
# Complexity of this algorithm is O(n^2)
def maxSubarray(nums):
    sums = min(nums)
    max_sum =min(nums)
    for w in range(1, len(nums)+1):
        for i in range(len(nums)-w+1):
            sums = sum(nums[i:i+w])
            if sums > max_sum:
                max_sum = sums
                
    return(max_sum)



#Katane's algorithm
#Optimal
# Complexity: O(n)

def maxSubarray2(nums):
    max_so_far  = min(nums)
    max_ending_here = 0
    for i in range(0, len(nums)): 
        max_ending_here = max_ending_here + nums[i] 
        if (max_so_far < max_ending_here): 
            max_so_far = max_ending_here 
  
        if max_ending_here < 0: 
            max_ending_here = 0   
    return max_so_far 


print(maxSubarray2(nums))