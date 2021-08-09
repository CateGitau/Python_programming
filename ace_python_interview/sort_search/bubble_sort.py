
'''
O(n^2)
'''

def bubble_sort(lst):
    """
    Bubble sort function
    :param lst: lst of unsorted integers
    """

    for i in range(len(lst)):
        for j in range(0, len(lst) - i - 1):
            if lst[j] > lst[j +1]:
                lst[j], lst[j+1] = lst[j+1], lst[j]

# Driver code to test above
if __name__ == '__main__':

    lst = [3, 2, 1, 5, 4]
    bubble_sort(lst)  # Calling bubble sort function

    print("Sorted list is: ", lst)