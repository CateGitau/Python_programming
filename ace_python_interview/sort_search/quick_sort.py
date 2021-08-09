import random


def choose_pivot(left, right):
    """
    Function to choose pivot point
    :param left: Left index of sub-list
    :param right: right-index of sub-list
    """

    # Pick 3 random numbers within the range of the list
    i1 = left + random.randint(0, right - left)
    i2 = left + random.randint(0, right - left)
    i3 = left + random.randint(0, right - left)

    # Return their median
    return max(min(i1, i2), min(max(i1, i2), i3))


def partition(lst, left, right):
    """
    Partition the list on the basis of pivot
    :param left: Left index of sub-list
    :param right: right-index of sub-list
    """

    pivot_index = choose_pivot(left, right)  # Index of pivot

    lst[right], lst[pivot_index] = lst[pivot_index], lst[right]  # put the pivot at the end

    pivot = lst[right]  # Pivot
    i = left - 1  # All the elements less than or equal to the
    # pivot go before or at i

    for j in range(left, right):
        if lst[j] <= pivot:
            i += 1  # increment the index
            lst[i], lst[j] = lst[j], lst[i]

    lst[i + 1], lst[right] = lst[right], lst[i + 1]  # Putting the pivot back in place
    return i + 1


def quick_sort(lst, left, right):
    """
    Quick sort function
    :param lst: lst of unsorted integers
    :param left: Left index of sub-list
    :param right: right-index of sub-list
    """

    if left < right:
        # pi is where the pivot is at
        pi = partition(lst, left, right)

        # Separately sort elements before and after partition
        quick_sort(lst, left, pi - 1)
        quick_sort(lst, pi + 1, right)


# Driver code to test above
if __name__ == '__main__':

    lst = [5, 4, 2, 1, 3]
    quick_sort(lst, 0, len(lst) - 1)

    # Printing Sorted list
    print("Sorted list: ", lst)
