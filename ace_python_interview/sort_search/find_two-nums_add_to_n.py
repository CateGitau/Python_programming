'''In this problem, you have to implement the find_sum(lst, n) 
function which will take a list lst and number n as inputs and return two numbers from the list that add up to n.'''

#my dumb solution
def find_summ(lst, n):
    for i in range(len(lst)):
        diff = n - lst[i]
        if diff in lst:
            return [lst[i], diff]

lst = [1, 21, 3, 14, 5, 60, 7, 6]
n = 81
print(find_summ(lst, n))


#brute force
'''O(n^2)'''
def find_sum_brute(lst, n):
    for i in range(len(lst)):
        for j in range(len(lst)):
            if lst[i] + lst[j] == n and i != j:
                return [lst[i], lst[j]]

# sorting the list using binary search
'''
O(nlogn)
'''
def binary_search(lst, item):
    """
    Binary Search helper function
    :param lst: A list of integers
    :param item: An item to be searched in the list
    """

    first = 0
    last = len(lst) - 1
    found = False
    
    while first <= last and not found:
        mid = (first + last) // 2
        
        if lst[mid] == item:
            found = mid
        else:
            if item < lst[mid]:
                last = mid - 1
            else:
                first = mid + 1
    
    return found


def find_sum(lst, n):
    """
    Function to find two number that add up to n
    :param lst: A list of integers
    :param n: The integer number n
    """

    lst.sort()

    for j in lst:
        index = binary_search(lst, n - j)
        if index:
            return [j, n - j]


# Driver to test above code
if __name__ == '__main__':
    
    print(find_sum([1, 2, 3, 4], 5))


#using a dictionary
'''
O(n)
'''
def find_sum_dict(lst, n):
    """
    Function to find two number that add up to n
    :param lst: A list of integers
    :param n: The integer number n
    """

    found_values = {}

    for ele in lst:
        try:
            found_values[n - ele]
            return [n-ele, ele]
        except:
            found_values[ele] = 0
            
# Driver to test above code

if __name__ == '__main__':

    print(find_sum_dict([1, 3, 2, 4], 6))
