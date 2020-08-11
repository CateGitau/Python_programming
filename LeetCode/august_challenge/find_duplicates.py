'''
Given an array of integers, 1 ≤ a[i] ≤ n (n = size of array), some elements appear twice and others appear once.

Find all the elements that appear twice in this array.

Could you do it without extra space and in O(n) runtime?
'''
nums = [4,3,2,7,8,2,3,1]

def findDuplicates(nums):
    elem = []
    for num in nums:
        if nums[abs(num)-1] < 0:
            elem.append(abs(num))
        else:
            nums[abs(num) - 1] *= -1
    return elem


print(findDuplicates(nums))

