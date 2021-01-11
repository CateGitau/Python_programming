"""
Given an array nums. 
We define a running sum of an array as runningSum[i] = sum(nums[0]…nums[i]).

Return the running sum of nums

"""



nums = [1,2,3,4]

def runninfSum(nums):
    runsums = []
    sums = 0
    for i in nums:
        sums+= i
        runsums.append(sums)
    return runsums

print(runninfSum(nums))



# nums = [1,2,3,4]

# def run_sum(nums):
#     sums = []

#     for i in range(len(nums)):
#         sums.append(sum(nums[:i+1]))

#     return sums


# print(run_sum(nums))

