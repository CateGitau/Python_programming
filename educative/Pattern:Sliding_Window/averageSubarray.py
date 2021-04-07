'''
Given an array, find the average of all contiguous subarrays of size ‘K’ in it.
'''

arr = [1, 3, 2, 6, -1, 4, 1, 8, 2]

k = 5

#bruteForce way which is O(n*k)
def averageSub(arr, k):
    result = []

    for i in range(len(arr)- k + 1):
        _sum=0

        for j in range(i, i+k):
            _sum+= arr[j]
        result.append(_sum/k)
    
    return result

#print(averageSub(arr, k))

#O(N) approach

def averageSub2(arr, k):
    result = []
    windowsum, windowstart = 0,0

    for windowend in range(len(arr)):
        windowsum += arr[windowend] #add the next element

        if windowend >= k - 1:
            result.append(windowsum/k) #calculate the average
            windowsum == arr[windowstart]#subtract the element that's going out
            windowstart+=1 #slide the window ahead
    return result 



print(averageSub2(arr, k))
