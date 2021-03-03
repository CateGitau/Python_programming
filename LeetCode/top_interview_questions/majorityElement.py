'''
Given an array nums of size n, return the majority element.

The majority element is the element that appears more than ⌊n / 2⌋ times. 
You may assume that the majority element always exists in the array.
'''

nums = [3,2,3]

def majorityElement(nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        countDict = {}
    
        for i in nums:
            if i not in countDict:
                countDict[i] = 1
            else:
                countDict[i] += 1
        
        return max(countDict, key = countDict.get)

print(majorityElement(nums))