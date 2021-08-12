# Driver to test above code

def binary_search(lst, item):
    first = 0
    last = len(lst) - 1
    found = False

    while first <= last and not found:
        mid = (last + first) // 2

        if lst[mid] == item:
            found = mid

        else:
            if lst[mid] > item:
                first = mid + 1

            else:
                last = mid - 1

    return found

def find_sum(lst, n):

    lst.sort()

    for j in lst:
        index = binary_search(lst, n-j)
        if index:
            return [j, n-j]

    

if __name__ == '__main__':

    print(find_sum([1, 3, 2, 4], 6))