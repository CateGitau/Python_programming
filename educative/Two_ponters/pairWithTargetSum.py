'''
Given an array of sorted numbers and a target sum, 
find a pair in the array whose sum is equal to the given target.
'''

arr = [1,2,3,4,6]
target = 6

#time complexity = O(N) where N is the total number of elements in the given array

def targetSum(arr, target):
    left = 0
    right = len(arr) -1

    while (left < right):
        current_sum = arr[left] + arr[right]

        if target == current_sum:
            return [left, right]
        
        if target < current_sum:
            right-=1
        else:
            left+=1

    return [-1,-1]


print(targetSum(arr, target))


#Alternate approach using hashTable

def targetSum2(arr, target):
    nums = {}

    for i, num in enumerate(arr):
        if target - num in nums:
            return [nums[target-num], i]
        else:
            nums[arr[i]] = i
    return [-1,-1]

print(targetSum2(arr, target))

#Alternate approach 

def TwoSum(arr, target):
    for i in range(0, len(arr)):
        if target-arr[i] in arr[i+1:]:
            return [i, arr.index(target-arr[i])]

print(TwoSum(arr, target))



    
