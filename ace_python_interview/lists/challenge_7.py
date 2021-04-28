# Find the second Maximum Value in a List

'''
Implement a function which returns the second largest element in the list
'''

my_list = [9,2,3,6]


# Traversing the list twice
# Time complexity is O(2n)
def find_second_maximum(lst):
    first_max = float('-inf')
    second_max = float('-inf') 

    for num in lst:
        if num > first_max:
            first_max = num

    for num in lst:
        if num != first_max and num > second_max:
            second_max = num

    return second_max

print(find_second_maximum(my_list))

# One Traversal
# Time complexity is O(n)
def find_second_maximum2(lst):
    first_max = float('-inf')
    second_max = float('-inf') 

    for i in range(len(lst)):
        if lst[i] > first_max:
            second_max = first_max
            first_max = lst[i]

        elif lst[i] > second_max and second_max != first_max:
            second_max = lst[i]
    if second_max == float('-inf'):
        return
    else:
        return second_max

print(find_second_maximum2(my_list))

