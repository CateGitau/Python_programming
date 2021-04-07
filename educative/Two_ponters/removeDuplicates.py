'''
Given an array of sorted numbers, 

remove all duplicates from it. 
You should not use any extra space; after removing the duplicates in-place 
return the length of the subarray that has no duplicate in it.
'''

arr = [2,3,3,6,9,9]

def removeDuplicates(arr):
    next_non_duplicate = 1

    i = 1

    while(i < len(arr)):
        if arr[next_non_duplicate - 1] != arr[i]:
            arr[next_non_duplicate] = arr[i]
            next_non_duplicate+=1
        i+=1

    return next_non_duplicate

print(removeDuplicates(arr))



#Similar questions
'''
Given an unsorted array of numbers and a target ‘key’, remove all instances of 
‘key’ in-place and return the new length of the array.
'''

arr = [3, 2, 3, 6, 3, 10, 9, 3]
key = 3

def removeInstance(arr, key):
    nextElement = 0 #index of the next element which is not key

    for i in range(len(arr)):
        if arr[i] != key:
            arr[nextElement] = arr[i]
            nextElement += 1
    return nextElement

print(removeInstance(arr, key))
