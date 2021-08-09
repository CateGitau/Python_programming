'''
Time complexity is O(n^2)
because finding a minimum number in the list requires iterating over the entire list for each element of the given list. 
The quadratic time complexity makes it impractical for large inputs.
'''
def selection_sort(lst):
    """
    Selection sort function
    :param lst: List of integers
    """

    # Traverse through all lst elements
    for i in range(len(lst)):
        min_index = i
        for j in range(i+1, len(lst)):
            if lst[min_index] > lst[j]:
                min_index = j
                
        # Swap the found minimum element with the first element
        lst[i], lst[min_index] = lst[min_index], lst[i]



# Driver code to test above
if __name__ == '__main__':

    lst = [3, 2, 1, 5, 4]
    selection_sort(lst)  # Calling selection sort function

    # Printing Sorted lst
    print("Sorted lst: ", lst)