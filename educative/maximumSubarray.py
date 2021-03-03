'''
Given an array of positive numbers and a positive number ‘k,’ 
find the maximum sum of any contiguous subarray of size ‘k’.
'''

arr = [2,1,5,1,3,2]
k = 3


#brute force way

def maxSub(arr, k):
    result = []

    for i in range(len(arr) - k+1):
        _sum = 0

        for j in range(i, i+k):
            _sum+= arr[j]

        result.append(_sum)
    return max(result)


print(maxSub(arr, k))


#another bruteforce way without using up space
def max_sub_array_of_size_k(k, arr):
    max_sum = 0
    window_sum = 0

    for i in range(len(arr) - k + 1):
        window_sum = 0
        for j in range(i, i+k):
            window_sum += arr[j]
            max_sum = max(max_sum, window_sum)
    return max_sum


#sliding window method

def maxSub2(arr, k):
    windowStart, windowSum = 0,0
    maxsum = 0
    for windowEnd in range(len(arr)):
        windowSum+= arr[windowEnd]

        if windowEnd >= k-1:
            maxsum = max(maxsum, windowSum)
            windowSum -= arr[windowStart]
            windowStart+=1
    return maxsum

print(maxSub2(arr, k))


'''
The time complexity of the above algorithm is O(N)
The algorithm runs in constant space O(1)
'''

