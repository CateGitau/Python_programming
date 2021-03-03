'''
Given a non-empty array of integers nums, 
every element appears twice except for one. 
Find that single one.

Follow up: Could you implement a solution with a 
linear runtime complexity and without using extra memory?


'''

nums = [2,2,1]

def singleNumber(num):
    countDict = {}

    for i in nums:
        if i not in countDict:
            countDict[i] = 1
        else:
            countDict[i] +=1

    return min(countDict, key = countDict.get)

print(singleNumber(nums))