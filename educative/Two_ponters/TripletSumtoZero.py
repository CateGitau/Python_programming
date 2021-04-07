'''
Given an array of unsorted numbers, 
find all unique triplets in it that add up to zero.
'''

arr = [-3, 0, 1, 2, -1, 1, -2]


# wrong solution but close
def tripleSum(arr):
    out = []
    for i in range(len(arr)):
        for j in range(len(arr[i+1:])):
            if -(arr[i]+arr[j]) in arr[j+1:]:
                out.append([arr[i], arr[j], -(arr[i]+arr[j])])
    return out

#print(tripleSum(arr))


#two pointer

def search_triplets(arr):
    arr.sort()
    triplets = []

    for i in range(len(arr)):
        # skip same element to avoid duplicate triplets
        if i > 0 and arr[i] == arr[i-1]:
            continue
        search_pair(arr, -arr[i], i+1, triplets)
    return triplets

def search_pair(arr, target_sum, left, triplets):
    right = len(arr) - 1
    while(left < right):
        current_sum = arr[left] + arr[right]
        if current_sum == target_sum:  # found the triplet
            triplets.append([-target_sum, arr[left], arr[right]])
            left += 1
            right -= 1
            while left < right and arr[left] == arr[left - 1]:
                left += 1  # skip same element to avoid duplicate triplets
            while left < right and arr[right] == arr[right + 1]:
                right -= 1  # skip same element to avoid duplicate triplets
        elif target_sum > current_sum:
            left += 1  # we need a pair with a bigger sum
        else:
            right -= 1  # we need a pair with a smaller sum

print(search_triplets(arr))
