'''
Implement a function find_max_prod(lst) that takes a list of numbers and returns a maximum product pair.
'''

# Decimal library to assign infinite numbers
from decimal import Decimal

#brute force approach
'''O(n^2)'''
def find_max_prod(lst):
    """
    Finds the pair having maximum product in a given list
    :param lst: A list of integers
    :return: A pair of integer
    """

    max_product = Decimal('-Infinity')
    max_i = -1
    max_j = -1

    for i in lst:
        for j in lst:
            if max_product < i * j and i is not j:
                max_product = i * j
                max_i = i
                max_j = j
    return max_i, max_j



#traversing the list once
def find_max_prod2(lst):
    """
    Finds the pair having maximum product in a given list
    :param lst: A list of integers
    :return: A pair of integer
    """

    max1 = lst[0]
    max2 = Decimal('-Infinity')


    min1 = lst[0]
    min2 = Decimal('Infinity')

    for number in lst:

        if number > max1:
            max2 = max1  # Second highest
            max1 = number  # First highest
        elif number > max2:
            max2 = number

        if number < min1:
            min2 = min1  # Second lowest
            min1 = number  # First lowest
        elif number < min2:
            min2 = number

    # Checking which pair has the highest product
    if max1 * max2 > min1 * min2:
        return max2, max1
    else:
        return min2, min1

 #Driver to test above code
if __name__ == '__main__':

    lst = [1, 3, 5, 2, 6]
    num1, num2 = find_max_prod2(lst)
    
    print (num1, num2)