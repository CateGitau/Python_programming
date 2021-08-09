'''
Binary search runs in O(log(n))
'''

def binary_search(lst, left, right, key):
    """
    Binary search function
    :param lst: lst of unsorted integers
    :param left: Left sided index of the list
    :param right: Right sided index of the list
    :param key: A key to be searched in the list
    """

    while left <= right:
        mid =  left + (right -left) //2

        #check if key is present at mid
        if lst[mid] == key:
            return mid
        
        # If key is greater, ignore left half
        elif lst[mid] < key:
            left = mid + 1

        # If key is smaller, ignore right half
        else:
            right = mid - 1

    # If we reach here, then the element was not present
    return -1

# Driver to test above code
if __name__ == '__main__':

    lst = [1, 2, 3, 10, 20, 40, 111, 244, 14444, 800000]
    key = 111

    # Function call
    result = binary_search(lst, 0, len(lst) - 1, key)

    if result != -1:
        print("Element is present at index:", result)
    else:
        print("Element is not present in the list")