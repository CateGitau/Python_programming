def sort_binary_list(lst):
    """
    A function to sort binary list
    :param lst: A list containing binary numbers
    :return: A sorted binary list
    """
    
    size = len(lst)  # Store the size of list

    for i in range(size):
        for j in range(0, size - i - 1):
            if lst[j] > lst[j + 1]:
                lst[j], lst[j+1] = lst[j+1], lst[j]


if __name__ == '__main__':
    lst = [1, 0, 1, 0, 1, 1, 0, 0]
    sort_binary_list(lst)
    print(lst)

#swapping ones
def sort_binary_list2(lst):
    """
    A function to sort binary list
    :param lst: A list containing binary numbers
    :return: A sorted binary list
    """
    
    j = 0
    
    for i in range(len(lst)):
        if lst[i] < 1:  # Swapping with jth element if the number is less than 1
            lst[i], lst[j] = lst[j], lst[i]  # Swapping
            j = j + 1
    
    return lst


# Driver to test above code
if __name__ == '__main__':
    
    lst = [1, 0, 1, 0, 1, 0, 1, 0]
    result = sort_binary_list2(lst)
    
    print (result)