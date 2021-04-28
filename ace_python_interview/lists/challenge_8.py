# Right rotate List

'''
Implement a function which will rotate the given list by K. This means that the right most elements will appear at the left-most positions in the list and so on,
You only have to rotate the list by one element at a time
'''

lst = [10,20,30,40,50]
n = 3
#Manual Rotation
#O(n)
def right_rotate(lst, k):
    if len(lst) == 0:
        k = 0
    else:
        k = k % len(lst)
    rotatedList = []
    # get the elements from the end
    for item in range(len(lst) - k, len(lst)):
        rotatedList.append(lst[item])
    # get the remaining elements
    for item in range(0, len(lst) - k):
        rotatedList.append(lst[item])
    return rotatedList

print(right_rotate(lst, n))

# Pythonic rotation
def right_rotate(lst, k):
    # get rotation index
    if len(lst) == 0:
        k = 0
    else:
        k = k % len(lst)
    return lst[-k:] + lst[:-k]


print(right_rotate([10, 20, 30, 40, 50], abs(3)))