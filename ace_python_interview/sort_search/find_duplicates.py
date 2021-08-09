
#Brute force
def find_duplicates(lst):
    """
    Function to find duplicates in a given lst
    :param lst: A list of integers
    :return: A list of duplicate integers with no repetition
    """
    
    result = []  # A list to store duplicates
    
    for i in range(len(lst)):
        for j in range(i+1, len(lst)):  # Starting from i + 1
            if lst[i] == lst[j] and lst[i] not in result: 
                result.append(lst[i])

    return result


def find_duplicates2(lst):
    result = []

    seen = {} # dictionary to store already observed elements

    for x in lst: #traverse the list
        if x not in seen:
            seen[x] = 1
        else:
            if seen[x] == 1:
                result.append(x)
            seen[x] += 1
    return result

# Driver to test above code
if __name__ == '__main__':
    
    lst = [1, 2, 5, 1, 4, 2, 1, 1]
    
    result = find_duplicates2(lst)
    print (result)
    
    