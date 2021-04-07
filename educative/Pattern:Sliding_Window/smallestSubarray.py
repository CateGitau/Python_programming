'''
Given an array of positive numbers and a positive number ‘S,’ 
find the length of the smallest contiguous subarray whose sum is greater than or equal to ‘S’.
Return 0 if no such subarray exists.

'''
import math

arr = [2,1,5,2,3,2]
S = 7

def smallestSub(arr, s):
    windowSum = 0
    windowStart = 0
    min_length = math.inf

    for windowEnd in range(0, len(arr)):
        windowSum += arr[windowEnd] #add the next element

        #shrink the window as small as possible until the windowSUm is smaller than s
        while windowSum >= s:
            min_length = min(min_length, windowEnd - windowStart + 1)
            windowSum -= arr[windowStart]
            windowStart += 1
    if min_length == math.inf:
        return 0
    return min_length


print(smallestSub(arr, S))


'''
The time complexity of the above algorithm will be O(N)
'''