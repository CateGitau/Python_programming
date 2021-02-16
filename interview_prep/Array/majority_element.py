'''
Given an array nums of size n, return the majority element.

The majority element is the element that appears more than ⌊n / 2⌋ times. 
You may assume that the majority element always exists in the array.
'''

nums = [3,2,3]

def find_majority(nums):
    n = len(nums) // 2

    freq = {}

    for item in nums:
        if item in freq:
            freq[item] += 1
        else:
            freq[item] = 1

    return max(freq, key=freq.get)

print(find_majority(nums))


def majorityElement1(self, nums):
        nums.sort()
        return nums[len(nums)//2]
    
def majorityElement2(self, nums):
    m = {}
    for n in nums:
        m[n] = m.get(n, 0) + 1
        if m[n] > len(nums)//2:
            return n
        
def majorityElement(self, nums):
    candidate, count = nums[0], 0
    for num in nums:
        if num == candidate:
            count += 1
        elif count == 0:
            candidate, count = num, 1
        else:
            count -= 1
    return candidate
    