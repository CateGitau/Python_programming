def find_in(lst, number):
    """
    A function to find a number in a 2D list
    :param lst: A 2D list of integers
    :param number: A number to be searched in the 2D list
    :return: True if the number is found, otherwise False
    """

    # Write your code here!
    for i in range(len(lst)):
        for j in range(len(lst[i])):
            if lst[i][j] == number:
                return True
    return False
       


D_list  =[[10, 11, 12, 13],
           [14, 15, 16, 17],
           [27, 29, 30, 31],
           [32, 33, 39, 50]]

number = 29

print(find_in(D_list, number))



#Binary search
def find_in2(lst, number):
    """
    A function to find a number in a 2D list
    :param lst: A 2D list of integers
    :param number: A number to be searched in the 2D list
    :return: True if the number is found, otherwise False
    """

    # Total number of rows
    rows = len(lst)

    # If list has no rows
    if lst is None:
        return False

    # Total Number of cols
    cols = len(lst[0])

    # If list has no cols
    if cols == 0:
        return False

    i = 0
    j = rows - 1

    if rows > 1:
        while i <= j:
            mid = i + (j - i) // 2
            if number == lst[mid][cols - 1]:
                return True

            if number > lst[mid][cols - 1]:
                i = mid + 1
            else:
                j = mid - 1

        if number > lst[mid][cols - 1]:
            rows = mid + 1
        else:
            rows = mid
    else:
        rows = 0

    if rows >= len(lst):
        return False

    i = 0
    j = cols - 1

    while i <= j:
        mid = i + (j - i) // 2
        if number == lst[rows][mid]:
            return True

        if number > lst[rows][mid]:
            i = mid + 1
        else:
            j = mid - 1

    return False


# Driver to test above code
if __name__ == '__main__':

    lst = [
        [10, 11, 12, 13],
        [14, 15, 16, 17],
        [27, 29, 30, 31],
        [32, 33, 39, 50]
    ]

    # Example 1
    print(find_in2(lst, 30))

    # Example 2
    print(find_in2(lst, 100))
