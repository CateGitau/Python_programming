
arr = [1,2,3,4,6]

target_sum = 6

def twoSum(arr, target_sum):
    left = 0
    right = len(arr) -1

    while(left < right):
        current_sum = arr[left]+ arr[right]

        if target_sum == current_sum:
            return [left, right]

        if target_sum < current_sum:
            right-=1
        else:
            left += 1

    return [-1,-1]

print(twoSum(arr, target_sum))

def twoSum2(arr, target_sum):
    for i in range(0, len(arr)):
        if target_sum-arr[i] in arr[i+1:]:
            return [i, arr.index(target_sum-arr[i])]

print(twoSum2(arr, target_sum))
        