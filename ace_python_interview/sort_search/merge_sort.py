def merge_sort(lst):
    """
    Merge sort function
    :param lst: lst of unsorted integers
    """
    if len(lst) > 1:
        mid = len(lst)// 2 #Mid of the list
        left = lst[:mid]
        right = lst[mid:]

        merge_sort(left)
        merge_sort(right)

        # Initializing the index variables
        i = 0
        j = 0
        k = 0

        # Copy data to temp lists left[] and right[]
        while i < len(left) and j < len(right):
            if left[i] < right[j]:
                lst[k] = left[i]
                i+=1
            else:
                lst[k] = right[j]
                j+=1
            k+=1
        # Checking if any element was left
        while i < len(left):
            lst[k] = left[i]
            i += 1
            k += 1

        # Checking if any element was right
        while j < len(right):
            lst[k] = right[j]
            j += 1
            k += 1 

# Driver code to test the above code
if __name__ == '__main__':

    lst = [3, 2, 1, 5, 4]
    merge_sort(lst)

    print("Sorted list is: ", lst)